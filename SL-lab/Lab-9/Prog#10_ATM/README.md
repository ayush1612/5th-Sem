## TO REMEMBER

1. import flask

```
pip install flask
```

`you can check the library by using the following commands`

```
python3
>> import flask

```

---

2. PORT already in use

```
ps -af|grep python
kill <id>
```

---


```
 to know which process is running -> look at the 
            |
            V
root      6795  5206  0 09:59 pts/0    00:00:00 sudo python3 application.py
root      6796  6795  0 09:59 pts/0    00:00:00 python3 application.py
root      6959  6796  0 09:59 pts/0    00:00:00 /usr/bin/python3 application.py
sem5a     7105  5602  0 10:03 pts/14   00:00:00 grep --color=auto python
```
---

<strong>So in the above process we will do the following steps to find and delete the process</strong>

```
ps -af|grep python
kill 6795
```

---

### How is the program running?

```
Few things to know:
* A server is something where your backend runs.
* Backend is the part of the program where you can make requests and send response to your webpage.
* Request can be a GET or POST (others to know:PUT,DELETE etc.)
```

1. You run the file `application.py` by the following command in the terminal.`sudo python3 application.py`
2. It shows the following output
```
 Debug mode: on
 * Running on http://localhost:80/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```
<strong> What just happened? </strong><br>
3. The file `application.py` ran and went to this line 

```
if __name__ == '__main__':
	app.run(host='localhost', port=80, debug=True)
```
- because of `debug = True` you are able to get the errors as well as u don't need to start the server again and again.
- the port is 80.

Now press Ctrl and click on this line `http://localhost:80/`, you will be redirected to the page.
