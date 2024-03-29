from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")
 
@app.route('/search', methods = ["GET", "POST"])
def search():
    if request.method == 'POST':
        result = request.form.get('contents')
        if result != None:
            print(f"Data recieved as {result}")
        else:
            print("Data not found")
        return render_template('search.html', result=result)
    elif request.method == 'GET':
        return render_template('search.html', result=result)

@app.route("/jokes")
def jokes(): 
    from jokes import jokes
    jokes = jokes()
    return render_template("jokes.html", jokenumber = jokes[0], jokecontent = jokes[1])

@app.route("/template")
def template():
    return render_template("template.html")

if __name__ == '__main__':
    app.run(debug=True, port=500)