import  pymysql.cursors
import sys
import json
import craw_domain

#connect tới database
try:
    conn = pymysql.connect(host='localhost',
                            user='subuser',
                            password="Subdomain2020@"  
                            database="craw_domain", 
                            port=3306)
except Exception as ex:
    print("Error connecting: " + str(ex))
    sys.exit(1)
cur = conn.cursor()

def select_db(cur, domain):
    """Lấy ra dữ liệu của subdomain từ Mysql
    """
    try:
        sub_in_mysql= {}
        cur.execute("SELECT subdomain from subdomain where domain ='{}'".format(domain))
        myresult = cur.fetchall()
        for ele in myresult:
            for sub in ele:
                converts = json.loads(sub)
                for key, value in converts.items():
                    sub_in_mysql[key] = value
    except Exception as ex:
        print("Error Selecting: " + str(ex))
    return sub_in_mysql

def insert_db(cur, mydomain, sub_all):
    """Ghi dữ liệu vào Mysql
    """
    cur.execute("INSERT INTO subdomain (domain, subdomain) values ('"+mydomain+"','"+sub_all+"')")
    conn.commit()
    return

def update_db(cur, mydomain, sub_js):
    """Cập nhật dữ liệu vào mysql
    """
    cur.execute("UPDATE subdomain SET subdomain='"+sub_js+"' WHERE domain='"+mydomain+"'")
    conn.commit()
    return

def main():
    """Xử lý dữ liệu
    Nếu không có dữ liệu trong database thì ghi luôn vào database
    Nếu có dữ liệu cũ thì cập nhật dữ liệu rồi ghi vào database
    """
    mydomain = craw_domain.domain
    sub_all = craw_domain.main()
    sub_in_mysql = select_db(cur, mydomain)
    if sub_in_mysql == {}:
        sub_all = json.dumps(sub_all)
        insert_db(cur, mydomain, sub_all)
    else:
        for key, value in sub_all.items():
            if key in sub_in_mysql and value != sub_in_mysql[key]:
                sub_in_mysql.pop(key)
                sub_in_mysql[key] = value
            elif key not in sub_in_mysql:
                sub_in_mysql[key] = value
        sub_js = json.dumps(sub_in_mysql)
        update_db(cur, mydomain, sub_js)
    return sub_in_mysql
