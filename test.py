import requests


# data = {
#     "username":"archana",
#     "useremail":"archanaya@gmail.com",
#     "password":"archanaya@1234"
# }


# r = requests.post('http://127.0.0.1:5000/create',json=data)
# print(r.json())


r = requests.get('http://127.0.0.1:5000/read')
print(r.json())