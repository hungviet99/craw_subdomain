import telebot
import re
import config
import elasticdb
import craw_domain

bot = telebot.TeleBot(config.TOKEN_TELE)

@bot.message_handler(commands=["start"])
def send_devices(message):
    """Tạo lệnh start để hướng dẫn sử dụng 
    """
    bot.reply_to(message, "Nhập vào /domain <tên domain> " +
                        "để xem các subdomain. VD: /domain hungnv.com")

def main():
    @bot.message_handler(commands=["domain"])
    def send_subdomain(message):
        """Tạo lệnh để truyền vào domain từ telegram
        """
        domain = message.text[8:]
        sub_all = craw_domain.main(domain)
        if not sub_all:
            bot.send_message(config.CHAT_ID, "Domain no info !!")
        else:
            elasticdb.main(domain, sub_all)
            res = elasticdb.search_by_index_and_id(domain)
            res2 = res['_source']
            res2.update(sub_all)
            sub_all_1 = []
            for key, value in res2.items():
                sub_all_1.append(key)
            sub_all_cv = str(sub_all_1)
            if len(sub_all_cv) > 4096:
                """Nếu list domain lớn hơn 4096 ký tự
                """
                for x in range(0, len(sub_all_cv), 4096):
                    try:
                        bot.send_message(config.CHAT_ID, "Tìm thấy: " +
                                         str(len(sub_all_1)) +
                                         " subdomain" + '\n\n' +
                                         sub_all_cv[x:x+4096],
                                         parse_mode='Markdown')
                    except:
                        bot.send_message(config.CHAT_ID, "Tìm thấy: " +
                                         str(len(sub_all_1)) + 
                                         " subdomain" + '\n\n' +
                                         sub_all_cv[x:x+4096])
            else:
                """Nếu list domain nhỏ hơn 4096 ký tự
                """
                try:
                    bot.send_message(config.CHAT_ID, "Tìm thấy: " +
                                     str(len(sub_all_1)) + " subdomain" + '\n\n' +
                                     sub_all_cv, parse_mode='Markdown')
                except:
                    bot.send_message(config.CHAT_ID, "Tìm thấy :" +
                                     str(len(sub_all_1)) + " subdomain" + '\n\n' +
                                     sub_all_cv)
    bot.polling()