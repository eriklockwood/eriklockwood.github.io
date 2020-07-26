from flask import Flask, render_template
app = Flask(__name__)


# index, data, and comparison routes
@app.route("/")
def index():

    return render_template("index.html")

@app.route("/data")
def data():
    
    return render_template("data.html")

@app.route("/comparison")
def comparison():
    
    return render_template("comparison.html")


#visual routes (can these be consolidated into 1 route with parameters?)
@app.route("/visual1")
def visual1():
    num = 1
    return render_template("visual.html", num=1)

@app.route("/visual2")
def visual2():
    num = 2
    return render_template("visual.html", num=2)

@app.route("/visual3")
def visual3():
    num = 3
    return render_template("visual.html", num=3)

@app.route("/visual4")
def visual4():
    num = 4
    return render_template("visual.html", num=4)


if __name__ == "__main__":
    app.run(debug=True)
