from flask import Flask, redirect, render_template, request,session

app = Flask(__name__)

app.secret_key = 'secret'

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html",res=0)
    
    elif request.method == 'POST':
        res = 0
        price = {
            'eggs':5,
            'milk':12,
            'bread':15
        }
        for item in ['eggs','milk','bread']:
            if item not in session:
                session[item] = int(request.form[item])
            else:
                session[item] += int(request.form[item])
            res = res + session[item]*price[item]
        return render_template('index.html',res=res)

if __name__ == '__main__':
    app.run(port="5050",debug=True)