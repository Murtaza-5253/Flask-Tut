
from flask import Flask, request as rq, render_template

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "Hello, World!"


@app.route("/")
def home():
    return render_template("one.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/add')
def add():

    x = int(rq.args['x'])
    y = int(rq.args['y'])
    z = x+y
    return "Addition is {}".format(z)


@app.route('/ascii')
def ascii():
    strTable = "<html><head><style>table {background-color: aliceblue; width: 100%; text-align: center; text-decoration: dashed;}</style></head><table><tr><th>Char</th><th>Ascii</th><tr>"
    for num in range(33, 48):
        symb = chr(num)
        strraw = "<tr><td>"+str(symb)+"</td><td>"+str(num)+"</td></tr>"
        strTable = strTable+strraw
    strTable = strTable+"</table></html>"
    hs = open("ascitable.html", 'w')
    hs.write(strTable)
    return strTable


app.run(debug=True)
