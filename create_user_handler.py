import sys, os
import json
import logging

sys.path.append('utils')
import mysql_connect

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def create_user(event, context):
    conn = mysql_connect.connect()
    params = json.loads(event['body'])
    if data_is_valid(params):
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO user (id, first_name, last_name, username, mobile, site_id) VALUES (%s,%s,%s,%s,%s,%s);"
                args = (params['id'], params['first_name'], params['last_name'], params['username'], params['mobile'], params['site_id'])
                cursor.execute(sql, args)
                conn.commit()
                status_code = 200
                body = {
                    "message": "User created successfully"
                }
                return {
                    "statusCode": status_code,
                    "body": json.dumps(body)
                }
        except:
            status_code = 403
            body = {
                "message": "Something went wrong please try again"
            }
        finally:
            conn.close()
            return {
                    "statusCode": status_code,
                    "body": json.dumps(body)
                }
    else:
        body = {
                "message": "Please enter valid data."
            }
        return {
                    "statusCode": 400,
                    "body": json.dumps(body)
                }

def data_is_valid(params):
    try:
        if(params["id"] and params["first_name"] and params["last_name"] and params["username"] and params["mobile"] and params["site_id"]):
            return True
        else:
            return False
    except:
        return False