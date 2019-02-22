import pymysql.cursors


conn = pymysql.connect(host='192.168.1.37', user='zlf', passwd='', db='a',
                       cursorclass=pymysql.cursors.DictCursor)
curs = conn.cursor()
