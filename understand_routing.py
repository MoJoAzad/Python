from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def hello(name):
    print(name)
    return "Hi, "+ name

@app.route('/repeat/<int:num>/<string:username>')
def repeat(num, username):
    return f"{num*username}"

if __name__=="__main__":

    app.run(debug=True)

