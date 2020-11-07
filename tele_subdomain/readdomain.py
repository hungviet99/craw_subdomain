import craw_domain
import telebot
import elasticdb
import config
import sys

bot = telebot.TeleBot(config.TOKEN_TELE)

def main():
    """
    Đọc file opendns-top-domains.txt để lấy tên các domain 
    """
    f = open("/opt/craw_subdomain/tele_subdomain/opendns-top-domains.txt", "r")
    for domain in f:
        """
        Sử dụng tên domain để tìm các subdomain
        """
        sub_all = craw_domain.main(domain)
        if not sub_all:
            bot.send_message(config.CHAT_ID, "Scan domain " + domain + " no info !!")
        else: 
            a = elasticdb.main(domain, sub_all)
            bot.send_message(config.CHAT_ID, "Scan domain " + domain + " success !!")
    return