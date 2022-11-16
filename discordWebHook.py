import requests, json

def send(webhook_url: str,text: str,embeds:dict=None):
    webhook_url  = webhook_url
    main_content = {'content': text,'embeds': embeds}
    headers      = {'Content-Type': 'application/json'}

    response     = requests.post(webhook_url, json.dumps(main_content), headers=headers)
    return response