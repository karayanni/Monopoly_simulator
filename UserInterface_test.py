from flask import Flask , redirect , url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("nader.html")

@app.route("/<num_players>")
def start(num_players):
    return f"wtf man?, {num_players}"

@app.route('/black')
def test():
    return redirect("https://www.google.com/search?q=why+are+you+so+horney&rlz=1C1CHBF_enUS877US878&oq=why&aqs=chrome.0.69i59j46j35i39j46j0j46l2.2103j0j4&sourceid=chrome&ie=UTF-8")


if __name__ == "__main__":
    app.run()