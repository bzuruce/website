from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.errorhandler(404) 
def error404(e): return render_template("/error/404.html")

@app.errorhandler(400) 
def error400(e): return render_template("/error/400.html")

@app.errorhandler(401) 
def error401(e): return render_template("/error/401.html")

@app.errorhandler(403) 
def error403(e): return render_template("/error/403.html")

@app.errorhandler(410) 
def error410(e): return render_template("/error/410.html")

@app.errorhandler(405)
@app.errorhandler(406)
@app.errorhandler(408)
@app.errorhandler(409)
@app.errorhandler(410)
@app.errorhandler(410)
@app.errorhandler(411)
@app.errorhandler(412)
@app.errorhandler(413)
@app.errorhandler(414)
@app.errorhandler(415)
@app.errorhandler(416)
@app.errorhandler(417)
@app.errorhandler(418)
@app.errorhandler(422)
@app.errorhandler(423)
@app.errorhandler(424)
@app.errorhandler(428)
@app.errorhandler(429)
def error4XX(e): return render_template("/error/4XX.html", e=e)

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
if __name__ == "__main__":
    app.run(debug=False, port=441)