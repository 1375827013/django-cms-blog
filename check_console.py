import requests
import time

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"
headers = {"Authorization": f"Token {PA_API_TOKEN}"}

consoles_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/"
response = requests.get(consoles_url, headers=headers)

if response.status_code == 200:
    consoles = response.json()
    if consoles:
        console_id = consoles[0]['id']
        print(f"控制台 ID: {console_id}")
        
        output_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/{console_id}/get_latest_output/"
        r = requests.get(output_url, headers=headers)
        if r.status_code == 200:
            print("\n--- 控制台输出 ---")
            print(r.json().get("output", "无输出"))
        else:
            print(f"获取输出失败: {r.text}")
