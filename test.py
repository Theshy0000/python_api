import requests
domainName='47.102.143.4:5000'

# a=requests.get('http://47.102.143.4:5000/users')
# print(a.text)
def post_josn():
    url = 'http://'+domainName+'/register'
    data = {
        "username": "李哥",
        "password": "dda"}
    headers = {'Content-Type': 'application/json;charset=UTF-8'}  # 请求头
    a = requests.request("post", url, json=data, headers=headers)
    return a.text


print(post_josn())


def post_value():
    url = 'http://'+domainName+'/values'
    data = {
        "values1": "李哥",
        "values2": "dda222sdsad"}
    a = requests.request("post", url, data=data)
    return a.text


print(post_value())


def post_from():
    url = 'http://'+domainName+'/form'
    data = {
        "form1": "李哥",
        "form2": "ddas"}
    a = requests.request("post", url, data=data)
    return a.text

print(post_from())


def delete():
    data=12
    url = 'http://'+domainName+'/delete/'+str(data)
    a = requests.request("delete", url)
    return a.text

print(delete())

def put():
    url = 'http://'+domainName+'/put'
    data = {
        "put1": "李哥",
        "put2": "dda222sdsad"}
    a = requests.request("put", url, data=data)
    return a.text

print(put())

ex={
  "code": 200,
  "msg": "恭喜，注册成功！"
}

