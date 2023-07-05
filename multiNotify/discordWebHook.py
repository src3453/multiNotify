import requests
import json

class discord:
    class webhook:
            def __init__(self,url:str,timeout:int=10) -> None:
                self.url = url
                self.timeout=timeout
            def send(self,text:str,embeds:dict=None):
                main_content = {'content': text,'embeds': embeds}
                headers      = {'Content-Type': 'application/json'}

                response     = requests.post(self.url, json.dumps(main_content), headers=headers,timeout=self.timeout)
                return response