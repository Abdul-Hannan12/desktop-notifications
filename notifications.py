import time
from plyer import notification

if __name__ == '__main__':
    title = input('enter the title of the notifications >> ')
    msg = input('enter the message of the notifications >> ')
    gap = int(input('enter the time (in seconds) for delay between sending notifications >> '))
    while True:
        notification.notify(
            title = title,
            message = msg,
            app_icon = "noti_icon.ico",
            timeout = 8
        )
        time.sleep(gap)
