import requests

def broadcast(token:str,messages:dict[str],uuid:str=None,timeout:int=10):
    ch_token = token
    line_notify_api = 'https://api.line.me/v2/bot/message/broadcast'
    headers = [{'Content-Type': 'application/json'},{'Authorization': f'Bearer {ch_token}'},{'X-Line-Retry-Key':uuid}]
    data = {"messages":messages}
    return requests.post(line_notify_api, headers = headers, data = data,timeout=timeout)
def get_quota(token:str,timeout:int=10):
    api="https://api.line.me/v2/bot/message/quota"
    headers={"Authorization": f"Bearer {token}"}
    return requests.get(api,headers=headers,timeout=timeout)