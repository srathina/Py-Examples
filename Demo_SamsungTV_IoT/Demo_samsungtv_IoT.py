import samsungtvws

#Connect the tv and get the token
tvr = samsungtvws.SamsungTVWS(host = '192.168.1.67', port = 8002, token_file = "tk.txt")

APP_NAME = "YouTube"

#test with poweron and home
tvr.shortcuts().power()
# tvr.shortcuts().home()

#get the list of apps installed and its ids.
resp = tvr.app_list()
resp_len = len(resp)
for item in range(0,resp_len):
    if(resp[item]['name'] == APP_NAME):
        app_id = resp[item]['appId']
    print("AppID:",resp[item]['appId'], "AppName:" ,resp[item]['name'])
    print()

#open netflix
tvr.rest_app_run(app_id)

#close netflix
# tvr.rest_app_close(app_id)

#app status
status = tvr.rest_app_status(app_id)
print(status)

