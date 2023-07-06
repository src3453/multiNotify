import pymsteams

class msTeams:
    class webhook:
        def __init__(self,webhook_url) -> None:
            self.url = webhook_url
        def notify(self,title:str,text:str):
            teams_obj = pymsteams.connectorcard(self.url)
            teams_obj.title(title)
            teams_obj.text(text)
            return teams_obj.send()