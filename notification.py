import time
from plyer import notification

def Notification():
     notification.notify(
        title = "Drink water",
        message = "Please , stop working take five minute rest and Drink water",
        app_icon = "image/image.ico",
        timeout =  5
    )
    
