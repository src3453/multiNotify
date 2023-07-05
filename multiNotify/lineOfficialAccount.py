import requests
class lineOfficialAccount:
    def __init__(self,token:str,timeout:int=10) -> None:
        self.token = token
        self.timeout = timeout

    def broadcast(self,messages:dict[str],uuid:str=None):
        ch_token = self.token
        line_notify_api = 'https://api.line.me/v2/bot/message/broadcast'
        headers = [{'Content-Type': 'application/json'},{'Authorization': f'Bearer {ch_token}'},{'X-Line-Retry-Key':uuid}]
        data = {"messages":messages}
        return requests.post(line_notify_api, headers = headers, data = data,timeout=self.timeout)
    def get_quota(self):
        api="https://api.line.me/v2/bot/message/quota"
        headers={"Authorization": f"Bearer {self.token}"}
        return requests.get(api,headers=headers,timeout=self.timeout)