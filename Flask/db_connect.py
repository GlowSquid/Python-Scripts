# Requires Flask-MySQLdb

import MySQLdb

def connection():
    conn = MySQLdb.connect(host='<localhost>', user='<username>', passwd='<password>')

    c=conn.cursor()

    return c, conn

if __name__ == '__main__':
    c,conn = connection()
    print('Complete')
