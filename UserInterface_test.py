from flask import Flask , redirect , url_for,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("nader.html")

@app.route("/<num_players>")
def start(num_players):
    return f"{num_players} your ass get your ass back to home screen"

@app.route('/description')
def test():
    return redirect("https://monopolynerd.com/online-monopoly-simulator/")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/pornhub')
def pornhub():
    return redirect("https://me.me/i/why-are-you-that-horny-9615a7eeb02f4dd89d653089991f7f66")

@app.route('/play')
def play():
    return render_template("play.html")




if __name__ == "__main__":
    app.run()