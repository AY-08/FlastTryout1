import requests


data = {
    "userid":"1",
    "username":"a1rch4ana1",
    "useremail":"1a1rch4ana@gmail.com",
    "password":"123ch4ana@1234"
}

updatedata = {
    
    "username":"archyadav345"
    
}
r1 = requests.post('http://127.0.0.1:5000/create',json=data)
print("create :",r1.status_code)

r2 = requests.get('http://127.0.0.1:5000/read')
print("read :",r2.status_code)

#id= "1"
r3= requests.put('http://127.0.0.1:5000/update/1',json=updatedata)
print("update :",r3.status_code)


r4 = requests.delete('http://127.0.0.1:5000/delete/4')
print("delete :",r4.status_code)