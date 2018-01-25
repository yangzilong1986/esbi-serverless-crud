import sys, os
import json

sys.path.append('utils')
import mysql_connect

def delete_user(event, context):
    conn = mysql_connect.connect()
    params = event['pathParameters']
    if data_is_valid(params):
        try:
            with conn.cursor() as cursor:
                sql = "delete from `user` where id = %s;"
                cursor.execute(sql, params['user_id'])
                conn.commit()
                status_code = 200
                body = {
                    "message": "User deleted successfully"
                }
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
    else:
        body = {
            "message": "Please enter valid data"
        }
        return {
            "statusCode": 400,
            "body": json.dumps(body)
        }

def data_is_valid(params):
    try:
        if(params["user_id"]):
            return True
        else:
            return False
    except:
        return False