from flask import Flask, render_template, request
# import mail.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        data = request.data
        return str(data) + ' SUCCESS FROM THE BACKEND'
    if request.method == "GET":
        return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
