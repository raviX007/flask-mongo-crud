
from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify , request
from werkzeug.security import generate_password_hash 

app=Flask(__name__)



app.config['MONGO_URI'] = "mongodb://db:27017/Users"

mongo = PyMongo(app)
@app.route('/hello',methods=['GET'])
def hello():
    return "hello world"

@app.route('/user',methods=['POST'])
def post_user():
    _json = request.json
    _name=_json['name']
    _email=_json['email']
    _password=_json['password']
    if _name and _email and _password and request.method=='POST':
        _hashed_password = generate_password_hash(_password)
        
        user_data = {
            'name': _name,
            'email': _email,
            'password': _hashed_password
        }
        
        # Use insert_one to insert a single document
        result = mongo.db.user.insert_one(user_data)
        
        if result.inserted_id:
            response = jsonify({"message": "User added"})
            return response, 200
        else:
            return jsonify({"message": "Failed to add user"}), 500
    else:
        return not_found()
@app.route('/users')
def get_user():
    print("Inside get users",flush=True)
    users=mongo.db.user.find()
    resp=dumps(users)
    return resp

@app.route('/user/<id>')
def get_userById(id):
     user=mongo.db.user.find_one({'_id':ObjectId(id)})
     resp=dumps(user)
     return resp


@app.route('/user/<id>',methods=['PUT'])
def update_user(id):
    _id=id
    _json=request.json
    _name=_json['name']
    _email=_json['email']
    _password=_json['password']
    
    if _name and _email and _password and _id and request.method=='PUT':
        _hashed_password=generate_password_hash(_password)
        mongo.db.user.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},{'$set':{'name':_name, 'email':_email, 'password':_hashed_password}})
        resp=jsonify("User Updated")
        resp.status_code=200
        return resp
    else:
        return not_found()

@app.route('/user/<id>',methods=['DELETE'])   
def del_user(id):
    mongo.db.user.delete_one({'_id':ObjectId(id)})
    resp=jsonify("User Deleted")
    resp.status_code=200
    return resp
    
@app.errorhandler(404)
def not_found(error=None):
    message={
        'status':404,
        'message':'Not Found' + request.url
    }
    resp =jsonify(message)
    
    resp.status_code=404
    
    return resp

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0') 
    
    
