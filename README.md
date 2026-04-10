# Django-DALLE-linebot-Render
# 一個使用Django框架和圖像生成AI DALLE，創造一個linebot的專案，快速建置於平台Render。
# 源於pyfbsdk59/Django-DALLE-linebot-Render https://github.com/pyfbsdk59/Django-DALLE-linebot-Render
# 修改更新至可使用


<div align="center">
  <img src="demo/demo1.png" width="300"/>
</div>

<div align="center">
  <img src="demo/demo2.png" width="300"/>
</div>

<div align="center">
  <img src="demo/demo3.png" width="300"/>
</div>

#### 1. 本專案屬在Render上，在Render網站中，選擇新增「Web Services」，可用github帳號匯入此專案，可先fork到自己的帳號，然後設定自己的名稱和選擇免費free方案。記得按下方「Advanced」，設定環境變數。


<div align="center">
  <img src="demo/demo1r.png" width="600"/>
</div>

<div align="center">
  <img src="demo/demo2r.png" width="700"/>
</div>

#### 2. 必須在Render的Environment Variables設定3個環境變數，分別是OPENAI_API_KEY<img width="354" height="81" alt="image" src="https://github.com/user-attachments/assets/f10fb7bf-0531-4818-a264-f1015748e987" />
和CHANNEL_SECRET<img width="382" height="81" alt="image" src="https://github.com/user-attachments/assets/5e804839-f558-43ea-8eba-01c67659aaad" />
和CHANNEL_ACCESS_TOKEN<img width="528" height="81" alt="image" src="https://github.com/user-attachments/assets/4ca10f87-e200-4c57-8538-dc82f236b967" />
。然後開始部屬，可能要花上一些時間。成功後複製自己的URL貼到line developer的Webhook URL來做設定和測試。例如：

https://xxx.onrender.com/

<div align="center">
  <img src="demo/demo3r1.png" width="700"/>
</div>

### 3. 注意Start Command要改為 gunicorn config.wsgi:application 來啟動。



