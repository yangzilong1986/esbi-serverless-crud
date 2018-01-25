import sys

sys.path.append('../utils')
import utils.constants as constants
import utils.pymysql as pymysql

def connect():
    try:
        connection = pymysql.connect(constants.RDS_HOST, user=constants.RDS_USER, passwd=constants.RDS_PASSWD, db=constants.DATABASE, connect_timeout=5)
        return connection
    except:
        return 0

connect()