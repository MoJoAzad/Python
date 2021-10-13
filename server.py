from flask import Flask, render_template
app=Flask(__name__)

@app.route("/play")
def play():
    return render_template('index.html',int=3)

@app.route("/play/<int:number>")
def mod(number):
    return render_template('index.html',int=number)

@app.route("/play/<int:number>/<string:color>")
def color(number, color):
    return render_template('index.html',int=number, color=color)

if __name__=="__main__":
    app.run(debug=True)