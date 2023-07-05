import requests
class lineNotify:
    def __init__(self,token:str,timeout:int=10) -> None:
        self.token = token
        self.timeout=timeout
    def notify(self,notification_message:str,file:bytes=None) -> requests.Response:
        line_notify_token = self.token
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        data = {'message': f'message: {notification_message}'}
        r = requests.post(line_notify_api, headers = headers, data = data, files = file, timeout=self.timeout)
        return r
