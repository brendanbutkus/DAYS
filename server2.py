from flask import Flask, render_template, request, redirect,session #when you use session, you need to set up a secret key in order for it to work
app = Flask(__name__)
app.secret_key = "keepitsecret"  #this cookie allows the server to remember us

@app.route("/")
def index():
    if "voters" not in session:
        session["voters"] = []
    if "total_votes" not in session:
        session["total_votes"] = 0
    if "votes" not in session:
        session["votes"] = {"Toy Story":0, "The Incredibles":0, "Monsters Inc":0}
    return render_template("index.html")



@app.route("/vote", methods=["POST"]) #absolutely do not render template on POST method
def vote():
    temp_user = {
        "name":request.form["name"],
        "age":request.form["age"],
        "movie":request.form["movie"]
    }
    session["voters"].append(temp_user) #in python when you append a session, the change will vanish after you leaver
    session.modified = True
    session["total_votes"] += 1
    # session["votes"]["Toy Story"] +=1
    session ["votes"][temp_user["movie"]] += 1
    return redirect("/results")

    # session["name"] = request.form["name"]
    # session["age"] = request.form["age"]
    # session["movie"] = request.form["movie"]
    # print("Here is the form info:")
    # print(request.form)
    # print(request.form["name"])
    # print(request.form["age"])
    # print(request.form["movie"])
    return redirect("/results")

@app.route("/results")
def results():
    return render_template("results.html", voters=session["voters"])
    # name=session["name"],age=session["age"],movie=session["movie"])

@app.route("/clear") 
def clear():
    session.clear()
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)
