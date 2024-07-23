from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",method=["GET"，"POST"])
def index():
    return(render_template("index.html"))
    
@app.route("/main",method=["GET"，"POST"])
def index():
    r=request.form.get("q")
    return(render_template("main.html",r=r))

if __name__ == "__main__":
    app.run()

