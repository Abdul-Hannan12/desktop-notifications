import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="This is a notification!",
            message="I am an expert developer and I am flexing my development skills by sending useless notifications.",
            # app_icon="F:\\programming\\Python\\My Python Practice\\noti_icon.ico",
            app_icon="noti_icon.ico",
            timeout=8
        )
        time.sleep(6)
        # time.sleep(60*60)
