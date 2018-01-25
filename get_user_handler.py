import sys, os
import json

sys.path.append('utils')
import mysql_connect

def get_user(event, context):
    conn = mysql_connect.connect()
    params = event['pathParameters']
    with conn.cursor() as cursor:
        sql = "select `id`,`first_name`, `last_name`,`username`,`mobile`, `site_id` from `user` where id = %s;"
        cursor.execute(sql, params['user_id'])
        result = cursor.fetchone()
        conn.commit()
        headers = ['id', 'first_name', 'last_name', 'username', 'mobile', 'site_id']
        user_data = dict(zip(headers, result))
        status_code = 200
        body = {
            "data": user_data
        }
    try:
        pass    
    except:
        status_code = 403
        body = {
            "message": "Something went wrong please try again"
        }
    finally:
        if(conn):
            conn.close()
        return {
                "statusCode": status_code,
                "body": json.dumps(body)
            }