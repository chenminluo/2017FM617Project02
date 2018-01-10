# 2017FM617Project02 #
## Team5 Project02 ##
## 企劃書:
* **題目名稱**：手把手台新小知識
* **組員**：
</br>   羅宸旻 林惠雯 陳怡樺 洪志穎
* **動機**：
</br>   因本組組員全都是金融創新產業碩士專班，此專班是與台新銀行合作，我們希望建置一個line bot透過問答的方式讓大眾輕鬆了解關於台新銀行的資訊，手把手無時無刻帶您了解台新銀行。
* **計畫摘要**：
</br>   我們想利用問答方式，使眾人了解台新銀行的基本資料、辦理業務等等之資訊，透過層層對答最終顯示出使用者想了解的資訊。
* **分工**：
</br>   待議
## 實作過程:
* **12/24**
> 觀看阿肥LINE BOT影片介紹
</br> Youtube Demo Tutorial V1
</br> Youtube Demo V2
</br> 之後依照步驟，創建 LINE API
</br> App name : 理查小幫手

* **1/3**
> LINE BOT 實戰 ( 聊天篇 )
</br> http://www.oxxostudio.tw/articles/201701/line-bot-2.html
</br></br> LINE BOT 實戰 ( 原理篇 )
</br> http://www.oxxostudio.tw/articles/201701/line-bot.html
</br></br> 試玩LINE-BOT API  (Flask + Requests)
</br> https://becoder.org/python-flask-requests-line-bot-api/
</br></br> 研究整體流程
</br>和每個對於LINE-BOT的部屬還有敘述
</br>在原理篇中主要是研究對於基礎API的設置和了解在部屬上需要進行的步驟
</br>聊天篇則是提到了回覆同樣詞句與指令回覆內容的項目。
</br></br> Webduino - 用 LINE 開關燈 ( 智慧插座應用 )
</br> https://www.youtube.com/watch?time_continue=89&v=cK3calqizTs
</br> 另外也提到上方連結的額外應用

* **1/5**
>研究阿肥LINE-BOT中GITHUB介紹與和CODE
</br> 理解阿肥的程式分層還有定義式結構
</br> 發現程式主要分為有定義的爬蟲、網址的回覆與按鈕選單的接續
</br> 其中定義爬蟲選單主要有：
</br> def eyny_movie():　def apple_news():　def technews():　等
</br> 定義網址回覆的涵式主要為URITemplateAction()

* **1/6**
>規畫與畫分自己數狀階層和顯示模式

* **1/7**
>初步程式撰寫完成後
</br>嘗試架設上Heroku
</br>其中失敗多次
</br>也試著嘗試部屬上其他作者簡單的回覆範例探究問題來源
</br>但在推上heroku後網址出現application error
</br>在老師說明原因後改用ngrok測試
</br>但是在ngrok推成功之後
</br>LINE BOT仍然無法正常運作
</br>於是我們回頭開始研究其他面向
</br>發現是我組PYTHON程式碼有問題

* **1/8**
>之後將CODE下方之return(0)後才成功部屬
</br>但是還是無法顯現出我們想要的結果
</br>請教老師後發現是爬蟲上的問題
</br>理解老師說明原因: 因為伺服器端會辨識 request 是不是從 browser 來的，所以需要讓爬蟲偽裝成 browser。
</br></br> headers = {'User-Agent': '偽裝成的chrome'}
</br> r = requests.get(url, headers=headers)  ]]
</br>偽裝成chrome的參考網址http://www.useragentstring.com/pages/useragentstring.php

* **1/9**
>看過老師錄的影片過後
</br>花費約3至5小時修改
</br>但還是無法顯現出理想中的型態
</br>而爬蟲最終效果與其他方式無太大差異
</br>故使用用其他方式替代
</br></br>爬蟲採用Google Chrome套件
</br>XPath Helper
</br> https://chrome.google.com/webstore/detail/xpath-helper/hgimnogjllphhhkhlmebbmlgjoejdpjl?hl=zh-TW
</br>SelectorGadget
</br> https://chrome.google.com/webstore/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb?hl=zh-TW

* **1/10**
>最後確認程式碼
</br> LINE BOT 美化工作 ex.製作按鈕樣式
</br> 成功推上 HEROKU
</br> 製作PPT

## 實作結果:
![Mou icon](https://i.imgur.com/7WRVZ6k.png)
