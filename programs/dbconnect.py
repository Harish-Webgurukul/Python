import MySQLdb

def connection():
    conn=MySQLdb.connect(host='localhost',
                         user='root',
                         passwd='password',
                         db='blog')
    c = conn.cursor()

    return c, cursor()

if __name__=='__main__':
    c, conn = connection()
    print('It worked')
