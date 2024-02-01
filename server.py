from flask import Flask, request, jsonify
from database import insert_user, delete_user_by_email, Check_user
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return jsonify({"server":"on"})



@app.route('/signin', methods=["POST"])
def signin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    res = Check_user(email=email, password=password)

    if res:
        return jsonify(res) 
    else:
        return jsonify({'name': "NONE"})


@app.route('/register', methods =["POST"])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    res = insert_user(name,email,password)

    return jsonify({'status': 200, 'message': 'User registered successfully'})



@app.route('/delete',methods =["DELETE"])
def delete():
    data = request.get_json()
    email = data.get('email')
    res = delete_user_by_email(email)
    if res:
        return jsonify({'message': '200'})
    else:
        return jsonify({'message': '404'})
    

    
if __name__ == '__main__':
    app.run(debug=True)
