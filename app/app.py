from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hola mundo!11!!</h1>"

@app.route("/index")
def index():
    titulo = "ñejeje"
    return render_template('index.html', titulo=titulo)

@app.route("/about-us")
def about_us():
    return render_template('about_us.html')

@app.route("/layout")
def layout():
    return render_template('layout.html')

def page_not_found(error):
    return render_template('error.html')

if __name__ == "__main__":
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, port=8080)


def suma(a,b):
    c=a+b
    return c

suma(5,5)