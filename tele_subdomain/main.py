import Telebot
import readdomain
import threading

if __name__ == "__main__":
        threading.Thread(target=Telebot.main).start()
        threading.Thread(target=readdomain.main).start()