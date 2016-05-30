from flask import Flask, render_template
app = Flask(__name__)

print('FROM WEB.PY')


@app.route("/")
@app.route("/user/<name>")
def hello(name=None):
    if name is not None:
        name = str.capitalize(name[0:1]) + name[1:100]
        return render_template("index.html", name=name)
    else:
        return render_template("index.html")


# Error Handlers
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404


if __name__ == "__main__":
    # app.debug = True
    # app.run('localhost', 3000, debug=True)
    app.run(debug=True)
