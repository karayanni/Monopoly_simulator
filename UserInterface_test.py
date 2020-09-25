from flask import Flask , redirect , url_for,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/<num_players>")
def start(num_players):
    return f"{num_players} your ass get your ass back to home screen"

@app.route('/description')
def test():
    return redirect("https://monopolynerd.com/online-monopoly-simulator/")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/nader')
def nader():
    return redirect("https://www.facebook.com/nader.karayanni")

@app.route('/simulate')
def simulate():
    return render_template("simulate.html")




if __name__ == "__main__":
    app.run()