from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
   return """<h1><font color='red'>Hello World!</font></h1>
   <form metod='GET' action='/About'>
   <br/>
   <font size='+8' color='red'>This is Home Page.</font>
   <br/>
   <button type='submit' name='about' height='100' width='100'>
   About
   </button>
   </form>
   """


@app.route("/About")
def about():
   return """<h1><font color='red'>This is About Page</font></h1>
   <form metod='GET' action='/'>
   <br/><br/>
   <button type='submit' name='home'>
   Home
   </button>
   </form>
   """
app.run()