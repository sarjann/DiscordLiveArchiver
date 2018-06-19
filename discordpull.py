import mysql.connector
from datetime import datetime




config = {
    'user': 'root1',
    'password': 'REDACTED',
    'host': 'localhost',
    'database': 'disc'
}



def store(postids,channelids,channels,users,messages):

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    add_discord = ("INSERT INTO discord "
                   "(postid,channelid,channel,username,message,datetime)"
                   "VALUES (%(postid)s, %(channelid)s,%(channel)s, %(username)s, %(message)s, %(datetime)s)")

    a = (int(postids) / 4194304) + 1420070400000
    datetimes = datetime.fromtimestamp(int(str(a)[:10]))

    data_discord = {
        'postid': postids,
        'channelid': channelids,
        'channel': str(channels),
        'username': str(users),
        'message': str(messages),
        'datetime': datetimes,
    }

    cursor.execute(add_discord,data_discord)

    cnx.commit()

    cursor.close()

    cnx.close()





