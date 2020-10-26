import  pymysql.cursors
import sys
import json
import craw_domain

try:
    conn = pymysql.connect(host='localhost',
                            user='root',  
                            database="craw_domain", 
                            port=3306)
except Exception as ex:
    print("Error connecting: " + str(ex))
    sys.exit(1)

cur = conn.cursor()

def select_db(cur, domain):
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
    cur.execute("DELETE  FROM subdomain WHERE domain='{}'".format(mydomain))
    cur.execute("INSERT INTO subdomain (domain, subdomain) values ('"+mydomain+"','"+sub_all+"')")
    conn.commit()

if __name__ == "__main__":
    sub_all = craw_domain.main()
    mydomain = craw_domain.domain
    sub_in_mysql = select_db(cur, mydomain)
    if sub_in_mysql == {}:
        sub_js = json.dumps(sub_all)
        insert_db(cur, mydomain, sub_js)
    else:
        for key, value in sub_all.items():
            if key in sub_in_mysql and value != sub_in_mysql[key]:
                sub_in_mysql.pop(key)
                sub_in_mysql[key] = value
            elif key not in sub_in_mysql:
                sub_in_mysql[key] = value
        sub_js = json.dumps(sub_in_mysql)
        insert_db(cur, mydomain, sub_js)
