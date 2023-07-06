import slackweb

class slack:
    class webhook:
        def __init__(self,url) -> None:
            self.url = url
        def notify(self,text):
            slack = slackweb.Slack(url=self.url)
            return slack.notify(text=text)