from flask import Flask, render_template , request , redirect

from firebase import firebase  
firebase = firebase.FirebaseApplication('https://atchaya-26935-default-rtdb.firebaseio.com/', None)   


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a5d4c874253a4fb1e5d2c345e40c3ad5d8b06b509105601f754d8a26b59933bb'

@app.route("/")
def index():
   return render_template("index.html")


@app.route("/slot_book", methods=('GET', 'POST'))
def slot_book():
   if request.method == 'POST':
      data = {}
      data["name"] = request.form['name']
      data["email"] = request.form['email']
      data["phone"] = request.form['phone']
      data["date"] = request.form['date']
      data["time"] = request.form['time']
      data["people"] = request.form['people']
      data["message"] = request.form['message']
      result = firebase.post('/slots',data)
      return "OK"

@app.route("/contact", methods=('GET', 'POST'))
def contact():
   if request.method == 'POST':
      data = {}
      data["name"] = request.form['name']
      data["email"] = request.form['email']
      data["subject"] = request.form['subject']
      data["message"] = request.form['message']
      result = firebase.post('/contact',data) 
      return "OK"


if __name__ == '__main__':
   app.run(debug = True)