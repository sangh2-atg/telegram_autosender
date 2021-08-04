from function import Function_auto_chat
# to yushin
_function = Function_auto_chat()

http_api = '1743691725:AAHaDoY6dQlKjMfOM8XgqZaEgEfkk0ALw4c'
chat_id = '435858132'
text = 'hello world'

_function.send_url(http_api, chat_id, text)