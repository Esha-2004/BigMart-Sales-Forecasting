from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

with open("traindmodel.pkl", mode="rb")  as file:
    linreg = pickle.load(file)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calc",methods=["GET","POST"])
def salecalc():
    c1=int(request.form.get("a"))
    c2=int(request.form.get("b"))
    c3=int(request.form.get("c"))
    c4=int(request.form.get("d"))
    c5=int(request.form.get("e"))
    c6=int(request.form.get("f"))
    c7=int(request.form.get("g"))
    c8=int(request.form.get("h"))
    c9=int(request.form.get("i"))
    c10=int(request.form.get("j"))

    yp=linreg.predict([[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]])[0]
    return render_template("index.html", sales=yp)


@app.route("/bye")
def byee():
    return "Byeee"

if __name__=="__main__":
    app.run(debug=True)