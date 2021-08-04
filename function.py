import requests
# to yushin
class Function_auto_chat:
    def send_url(self, api, id, text):
        url = f'https://api.telegram.org/bot{api}/sendMessage?chat_id={id}&text={text}'
        requests.post(url)