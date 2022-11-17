import requests
import json

def send(webhook_url: str,text: str,embeds:dict=None,timeout:int=10):
    main_content = {'content': text,'embeds': embeds}
    headers      = {'Content-Type': 'application/json'}

    response     = requests.post(webhook_url, json.dumps(main_content), headers=headers,timeout=timeout)
    return response