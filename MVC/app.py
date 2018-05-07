# coding = utf-8

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()



'''
运行python app.py，Flask 自带的 Server 在端口5000上监听：

$ python app.py 
* Running on http://127.0.0.1:5000/
1. 打开浏览器，输入首页地址http://localhost:5000/：
2. 输入首页地址http://localhost:5000/signin,会显示登陆表单
3. 输入预设的用户名admin和口令password，登录成功：
   输入其他错误的用户名和口令，登录失败：
'''