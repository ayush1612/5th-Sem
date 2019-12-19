from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)

app.secret_key = 'secret'

@app.route("/",methods=['GET','POST'])
def index():
    try:
        balance = session['balance']
        count = session['count']
    except KeyError:
        balance = session['balance'] = 8000
        count = session['count'] = 0

    if request.method == 'GET':
        return render_template("index.html",balance=balance,count=count,msg='')
    
    elif request.method == 'POST':
        try:
            amt = int(request.form['amt'])
        except ValueError:
            amt = 0
        if request.form['actions'] == 'Withdraw':

            if amt<0:
                msg = 'Enter a positive amount'
            elif amt>5000:
                msg = 'Cannot withdraw more than 5000 at once'
            elif count == 5:
                msg = 'Sorry, no more transactions allowed!'
            else:
                balance = balance - amt
                session['balance'] = balance
                count += 1
                session['count'] = count
                msg = 'Succesfully Withdrawn'

            return render_template('index.html',balance = balance,msg = msg,count = count)

        elif request.form['actions'] == "Deposit":

            if amt<0:
                msg = 'Enter a positive amount'
            elif count == 5:
                msg = 'Sorry, exceeded  transactions!'
            else:
                balance = session['balance'] = balance + amt
                count += 1
                session['count'] = count
                msg = 'Successfully Deposited'
            
            return render_template("index.html",balance=balance,count=count,msg=msg)
        
if __name__ == '__main__':
    app.run(debug=True,port='5050')

session.clear()