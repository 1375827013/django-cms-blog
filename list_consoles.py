import requests

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"
headers = {"Authorization": f"Token {PA_API_TOKEN}"}

consoles_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/"
response = requests.get(consoles_url, headers=headers)

if response.status_code == 200:
    consoles = response.json()
    print(f"找到 {len(consoles)} 个控制台")
    for console in consoles:
        print(f"  - ID: {console['id']}, 名称: {console.get('name', 'N/A')}")
else:
    print(f"获取控制台失败: {response.text}")
