from crypt import methods
from enum import unique
from flask import Flask,request,make_response,jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite3'

db = SQLAlchemy(app)



class User(db.Model):
    userid=db.Column(db.Integer, primary_key= True, unique=True)
    username = db.Column(db.String,primary_key= True)
    useremail = db.Column(db.String)
    password = db.Column(db.String)



@app.route('/create',methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return make_response(jsonify({"Message":"Check the fields entered"}),404)

    userid = data['userid']
    username = data['username']
    useremail= data['useremail']
    password = data['password']
    user = User(userid=userid,username=username,useremail=useremail,password=password)

    db.session.add(user)
    db.session.commit()
    db.session.close()

    return make_response(jsonify({"Message":"Created sucessfully"},200))

    
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
            "userid":user.userid,
            "username":user.username,
            "useremail":user.useremail,
            "password":user.password
        }
            

        )

    return make_response(jsonify(userlist))


@app.route('/update/<int:userid>', methods=["PUT"])
def update_username(userid):
    #userid = request.args.get('userid')
    upatedata = request.get_json()
    usernameupdate = upatedata['username']
    print("put userid",userid)
    print("put json update data",upatedata)
    querydata = db.session.query(User).filter(User.userid==userid).all()
    
    print("put data ",querydata)
    if not querydata:
        return make_response(jsonify({"Message":"Check your userid"},404))
    for data in querydata:
        setattr(data,"username",usernameupdate)
    db.session.commit()
    
    return make_response(jsonify({"Message":"Put data updated sucessfully"}),200)

    


@app.route('/delete/<int:id>', methods=['DELETE'])
def deleteuser(id):
    querydata = db.session.query(User).filter(User.userid==id).all()
    print("querydata",querydata)
    if not querydata:
        return make_response(jsonify({"Message":"Check your id"}),404)

    for user in querydata:
        print("user",user)
        db.session.delete(user)
    
    db.session.commit()

    return make_response(jsonify({"Message":"Data has been deleted"}),200)    



if __name__ =='__main__':
    db.create_all()
    app.run(port = 5000, debug=True)

