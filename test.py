import requests
from flask import jsonify

headers = {'Content-Type':'application/json','cache-control':'no-cache'}

payload = "{\n\t\"username\": \"test03\",\n\t\"password\":\"test3\",\n\t\"useremail\":\"user3@test.com\"}"


dataload ="{\n\t\"username\": \"test user 2\"}"

#dataload ={'username':'labtest'}
# print("payloads",payload)
# r1 = requests.post('http://127.0.0.1:5000/create',data=payload,headers=headers)
# print("create :",r1.status_code)

r2 = requests.get('http://127.0.0.1:5000/read')
print("read :",r2.status_code)

#id= "1"
r3= requests.put('http://127.0.0.1:5000/update/2',data=dataload,headers=headers)
print("update :",r3.status_code)


# r4 = requests.delete('http://127.0.0.1:5000/delete/2')
# print("delete :",r4.status_code)