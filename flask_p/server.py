import re
from turtle import color
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def boxes():
    return render_template('index.html', num=1, color='blue')

@app.route('/play/<int:num>')
def boxes_two(num):
    return render_template('index.html', num=num, color='aqua')

@app.route('/play/<int:num>/<string:color>')
def boxes_three(num, color):
    return render_template('index.html', num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)