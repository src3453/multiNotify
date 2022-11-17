import requests

def notify(token:str,notification_message:str,file:bytes=None,timeout:int=10):
    line_notify_token = token
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data, files = file, timeout=timeout)
