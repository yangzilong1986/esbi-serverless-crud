import sys, os
import json

sys.path.append('utils')
import mysql_connect

def update_user(event, context):
    conn = mysql_connect.connect()
    params = json.loads(event['body'])
    user_id = event['pathParameters']['user_id']
    if data_is_valid(params, user_id):
      try:
          with conn.cursor() as cursor:
              sql = "UPDATE `user` set `first_name` = %s, `last_name` = %s, `username` = %s, `mobile` = %s, `site_id` = %s where id = %s;"
              args = (params['first_name'], params['last_name'], params['username'], params['mobile'], params['site_id'], user_id)
              cursor.execute(sql, args)
              conn.commit()
              status_code = 200
              body = {
                  "message": "User updated successfully"
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
        "message": "Please enter valid data"
      }
      return {
        "statusCode": 400,
        "body": json.dumps(body)
      }

def data_is_valid(params, user_id):
    try:
        if(user_id and params["first_name"] and params["last_name"] and params["username"] and params["mobile"] and params["site_id"]):
            return True
        else:
            return False
    except:
        return False