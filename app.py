from crypt import methods
from enum import unique
from flask import Flask,request,make_response,jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite3'

db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String, unique=True)
    useremail = db.Column(db.String)
    password = db.Column(db.String)



@app.route('/create',methods=['POST'])
def create_user():
    data = request.get_json()
    print("data request",data)
    if not data:
        return make_response(jsonify({"Message":"Check the fields entered"}),404)
    username = data['username']
    useremail= data['useremail']
    password = generate_password_hash(data['password'],method='sha256')


    user = User(username=username,useremail=useremail,password=password)

    db.session.add(user)
    db.session.commit()
    db.session.close()

    # return make_response(jsonify({"Message":"Created sucessfully"},200))
    return make_response(jsonify({"Created sucessfully": data},200))

    
@app.route('/read', methods=['GET'])
def readall_users():
    data= User.query.all()
    print(data)
    if not data :
        return make_response(jsonify({"Message":"List of users empty"}),404)
    userlist =[]    
    for user in data:
        print("user",type(user))
        userlist.append({
            
            "username":user.username,
            "useremail":user.useremail,
            "password":user.password
        }
            

        )

    return make_response(jsonify(userlist))


@app.route('/update/<int:id>', methods=["PUT"])
def update_username(id):
 
    upatedata = request.get_json()
    usernameupdate = upatedata['username']
    print("put userid",id)
    print("put json update data",upatedata)
    querydata = db.session.query(User).filter(User.id==id).all()
    
    print("put data ",querydata)
    if not querydata:
        return make_response(jsonify({"Message":"Check your userid"},400))
    for data in querydata:
        setattr(data,"username",usernameupdate)
    db.session.commit()
    
    return make_response(jsonify({"Message":"Put data updated sucessfully"}),200)

    


@app.route('/delete/<int:id>', methods=['DELETE'])
def deleteuser(id):
    querydata = db.session.query(User).filter(User.id==id).all()
    print("querydata",querydata)
    if not querydata:
        return make_response(jsonify({"Message":"Check your user id"}),204)

    for user in querydata:
        print("user",user)
        db.session.delete(user)
    
    db.session.commit()

    return make_response(jsonify({"Message":"Data has been deleted"}),200)    



if __name__ =='__main__':
    db.create_all()
    app.run(port = 5000, debug=True)

