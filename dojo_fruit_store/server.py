from flask import Flask, render_template, request, redirect,session
import datetime
app = Flask(__name__) 
app.secret_key='This app is secret.' 

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():        
    print(request.form)
    
    session['first_name']= request.form['first_name']
    session ['last_name'] = request.form['last_name']
    session['strawberry'] = int(request.form ['strawberry'])
    session['raspberry'] = int(request.form['raspberry'])
    session['apple'] = int(request.form['apple'])
    session['student_id']= request.form['student_id']
    
    return redirect ("/info")

@app.route('/info')
def info():
    quantity=session['strawberry']+session['raspberry']+session['apple']
    return render_template("checkout.html", quantity = quantity, date_time=datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%p"))

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    