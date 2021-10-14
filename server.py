from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def checkerboard():
    return render_template('index.html')

@app.route("/<int:number>")
def number(number):
    return render_template('index.html', int=number)

@app.route("/<int:number>/<string:color>")
def colors(number, color):
    return render_template('index.html', int=number, color=color)

if __name__=="__main__":
    app.run(debug=True)
