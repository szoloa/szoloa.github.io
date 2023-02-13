import requests
import base64
import os

def image_to_base64(image_path):
    with open(image_path, "rb") as file:
        base64_data = base64.b64encode(file.read())  # base64编码
    return base64_data

url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/plant?access_token="24.7768516969f8a53761de6dc1fe90ce91.2592000.1675319735.282335-29481336"'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json'
}

def plant(path):
    payload={
    'image' : image_to_base64(path)
    }
    r = requests.post(data=payload,headers=headers,url=url)
    return r.text

print(plant('./python/plant/南体 0001.jpg'))

'''
if __name__ == '__main__':
    list = os.listdir('./python/plant')
    for i in list:
        pjson = plant('./python/plant' + i)
'''