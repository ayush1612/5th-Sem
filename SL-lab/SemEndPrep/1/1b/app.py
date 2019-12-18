from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)

app.secret_key = "secret"

@app.route("/",methods=['GET','POST'])
def index():
    try:
        balance = session['balance']
        count = session['count']
    except KeyError:
        balance = session['balance'] = 8000
        count = session['count'] = 0

    if request.method == 'GET':
        msg = ""
        return render_template('index.html',balance=balance,msg = msg,count=count)
    else:
        if request.form['action'] == 'Withdraw':
            if request.form['amt'] == '':
                msg = 'Enter an amount'
                return render_template('index.html',balance=balance,msg = msg,count=count)

            elif int(request.form['amt']) < 0:
                msg = 'Enter a positive amount'
                return render_template("index.html",msg=msg,balance=balance,count=count)
            elif session['count'] == 5:
                msg = 'No more transcations allowed'
                return render_template("index.html",msg=msg,balance=balance,count=count)

            else:
                msg = 'Amount Withdrawn'
                balance = session['balance'] - int(request.form['amt'])
                session['balance'] = balance
                session['count'] = session['count'] + 1
                count = session['count']
                return render_template("index.html",msg=msg,balance=balance,count=count)
        elif request.form['action'] == 'Deposit':
            if int(request.form['amt'])>10000:
                msg = 'Cannot deposit more than 10000'
                return render_template("index.html",msg=msg,balance=balance,count=count)
            else:
                msg = 'Amount Deposited'
                session['balance'] = session['balance'] + int(request.form['amt'])
                balance = session['balance']
                return render_template("index.html",msg=msg,balance=balance,count=count)

    session.clear()
if __name__ == '__main__':
    app.run(port='5005',debug=True)