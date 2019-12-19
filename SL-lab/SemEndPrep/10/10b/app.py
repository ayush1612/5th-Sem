from flask import Flask, redirect, render_template, request, session
import re
import time

app = Flask(__name__)

app.secret_key='secret'

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html",msg='')

    elif request.method == "POST":
        usn = request.form['student-usn']
        dob = request.form['student-dob']
        m1 = int(request.form['student-marks1'])
        m2 = int(request.form['student-marks2'])
        m3 = int(request.form['student-marks3'])
        
        try:
            time.strptime(request.form['student-dob'],"%d/%m/%Y")
        except ValueError:
            return render_template("index.html",msg='Invalid Date. Use DD/MM/YYYY')
        
        if re.match('^[1][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$',request.form['student-usn']):
            avg = (m1 + m2 + m3)/3.0
            msg = "Succesfully Registered. Average Marks = " + str(avg)

        else:
            msg = "Invalid USN"
        return render_template("index.html",msg=msg)

if __name__ == '__main__':
    app.run(debug=True,port='5050')