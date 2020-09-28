from flask import Flask , redirect , url_for,render_template,request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/<num_players>")
def start(num_players):
    return f"{num_players} zb"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/simulate')
def simulate():
    return render_template("simulate.html")



@app.route('/simulate',methods = ['POST'])
def get_num_of_steps():
    num_of_steps = request.form['num_of_steps']
    starting_cash = request.form['starting_cash']
    num_of_players = request.form.get('selected_num_players')
    print(num_of_steps,starting_cash)
    return render_template("monopoly.html")
    #return render_template("test.html",num_of_steps=num_of_steps,starting_cash=starting_cash,num_of_players=num_of_players)




if __name__ == "__main__":
    app.run(debug=True)