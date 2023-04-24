# krcert_to_telegram   
## 1. 사전 설치 파일   
```python
pip install feedparser   
pip install python-telegram-bot   
pip install telegram   
```

## 2. Telegram Bot Token 확인
### 1) 텔레그램 실행
### 2) Botfather 추가 및 Bot Token 발급
#### - 우상단 돋보기 클릭
![Search_botfather_01](https://user-images.githubusercontent.com/95232424/234058538-fd23dc30-5590-44e9-ac3e-9388df5e9505.jpg)

#### - botfather 검색 및 추가
![Search_botfather_02](https://user-images.githubusercontent.com/95232424/234058373-3dfb6c7b-eb30-4dfe-8493-5b99bf4ad7f3.jpg)

#### - Bot Token 발급 및 이름 정하기 (bot 이름 끝에는 무조건 "\_bot"이 붙음 ex) rkd -> rkd_bot)
```
/newbot
```
![Start_bot_01](https://user-images.githubusercontent.com/95232424/234059705-3c31e2ae-fd5b-42e8-bb98-96f83face695.jpg)

#### - Bot Token 확인
![Bot_Token_ID](https://user-images.githubusercontent.com/95232424/234057346-837f3307-fdec-45ca-8e45-6a45d9e5c0ef.jpg)

## 3. Telegram Channel ID 확인 
### 1) 채널 만들기
#### - 채널 생성 -> bot 추가 -> 관리자로 승격 (보안 공지 알람방에 관리자만 메세지 보내도록 하기 위함)
#### - bot 추가 후 채널 내 메세지 발생
![Send_Message](https://user-images.githubusercontent.com/95232424/234063960-18f5a1af-c13c-4543-b013-8df7fa479f9c.jpg)


#### - 메세지 발생 후 아래의 url로 채널 id확인
```html
https://api.telegram.org/bot[BOT_TOKEN]/getUpdates
```

#### - 결과 값 확인
```json
{"ok":true,"result":[{"update_id":123456789,
"channel_post":{"message_id":900,"author_signature":"rkd","sender_chat":{"id":-1234567890123,"title":"Rkd-test","type":"channel"},"chat":{"id":-1234567890123,"title":"Rkd-test","type":"channel"},"date":1682354709,"text":"."}}]}
```

#### - 결과 값 내 "id" 값 확인 ex) "-1234567890123"
```json
"sender_chat":{"id":-1234567890123,"title":"Rkd-test","type":"channel"}
```

