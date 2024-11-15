from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello_world', methods=['GET'])
def sayHelloWorld():
    
    data ={
        1: "Hello World!"
    }
    
    return jsonify(data)

@app.route('/users/', methods=['GET'])
def returnUsersInfo():
    
    id = request.args.get('id')
    id = int(id)
    
    users = {
        1: {
            'name': 'Alex',
            'age': 20
        },
        2: {
            'name': 'John',
            'age': 35
        },
        3: {
            'name': 'Oxmoul',
            'age': 39
        }
    }

    return jsonify(users[id])


if __name__ == '__main__':
    app.run(debug=True)