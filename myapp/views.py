from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, ImageSendMessage, TextSendMessage

import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")

line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
parser = WebhookParser(os.getenv("CHANNEL_SECRET"))


class DalleService:
    def generate_image_url(self, prompt: str) -> str:
        response = openai.Image.create(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url"
        )
        return response["data"][0]["url"].strip()


dalle_service = DalleService()


@csrf_exempt
def callback(request):
    print("=== callback hit ===")
    print("method:", request.method)

    if request.method != "POST":
        return HttpResponseBadRequest("POST only")

    signature = request.META.get("HTTP_X_LINE_SIGNATURE")
    if not signature:
        print("missing X-Line-Signature")
        return HttpResponseForbidden("Missing signature")

    body = request.body.decode("utf-8")
    print("body:", body)

    try:
        events = parser.parse(body, signature)
        print("events count:", len(events))
    except InvalidSignatureError as e:
        print("InvalidSignatureError:", str(e))
        return HttpResponseForbidden("Invalid signature")
    except LineBotApiError as e:
        print("LineBotApiError:", str(e))
        return HttpResponseBadRequest("Line API error")
    except Exception as e:
        print("Unexpected parse error:", str(e))
        return HttpResponseBadRequest("Parse error")

    if not events:
        print("empty events -> return 200")
        return HttpResponse("OK")

    for event in events:
        if isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
            user_text = event.message.text.strip()
            print("user_text:", user_text)

            try:
                image_url = dalle_service.generate_image_url(user_text)
                print("image_url:", image_url)

                line_bot_api.reply_message(
                    event.reply_token,
                    ImageSendMessage(
                        original_content_url=image_url,
                        preview_image_url=image_url
                    )
                )

            except Exception as e:
                print("OpenAI or reply error:", repr(e))
                try:
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=f"圖片生成失敗：{str(e)}")
                    )
                except Exception as reply_error:
                    print("fallback reply error:", repr(reply_error))

    return HttpResponse("OK")
