from flask import Flask, render_template, request
import mail

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        to_email_address = request.form['email']
        from_email_address = 'julie.yc.pan@gmail.com'
        subject = 'this is from flask'
        content = 'i got here yay!'
        result = mail.send(to_email_address, from_email_address, subject, content)
        return to_email_address
    if request.method == "GET":
        return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
