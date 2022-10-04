
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/hello/<name>")
def user(name):
    return f"<h1>Čia mano naujas puslapis. Labas, {name}</h1>"

@app.route("/logika")
def logika():
    lyginiai = []
    for x in range(11):
        if x % 2 == 0:
            lyginiai.append(x)
    return render_template('logika.html', skaiciai=lyginiai)

@app.route("/vardai")
def vardai():
    vardai = ['Jonas', 'Antanas', 'Petras']
    return render_template('vardai.html', vardai=vardai)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        vardas = request.form['vardas']
        pavarde = request.form['pavarde']
        return render_template('greetings.html', vardas=vardas, pavarde=pavarde)
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)