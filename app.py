### Create a simple flask application

from unittest import result
from flask import Flask ,render_template, request,redirect,url_for

## create the flask app

app=Flask(__name__)

@app.route('/Welcome')
def Welcome():
    return " Welcome to Flash tutorial"

@app.route('/home')
def home():
    return " Welcome to home page"

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    return "the person is passes and score is "  +  str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person is failed and score is " + str(score)


@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        
        average_marks=(maths+science+history)/3
        
        if average_marks>=50:
            result-"success"
        else:
            result="fail"
            
        #return redirect(url_for(result,score=average_marks))
            
        
        return render_template('calculate.html',results=average_marks)



if __name__=='__main__':
    app.run()