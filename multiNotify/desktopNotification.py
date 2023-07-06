from plyer import notification

class toast:
    def __init__(self) -> None:
        pass
    def notify(self,title:str="",message:str="",app_name:str="",app_icon:str="",timeout:int=10,ticker:str="",toast:bool=False):
        notification.notify(title=title, message=message, app_name=app_name, app_icon=app_icon, timeout=timeout, ticker=ticker, toast=toast)



