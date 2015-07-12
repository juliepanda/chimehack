from flask import Flask, render_template, request
import mail, MailContent, text, TextContent, secrets
# from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if request.method == "GET":
        return render_template('index.html')

@app.route('/sendmail', methods=['POST'])
def send_mail():
    if request.method == "POST":
        to_email_address = request.form['email']
        category = request.form['template']
        from_email_address = 'julie.yc.pan@gmail.com' # switch out to official email
        # update here to switch templates
        subject = MailContent.test_obj.subject
        content = MailContent.test_obj.content
        result = mail.send(to_email_address, from_email_address, subject, content)
        print str(result)
        return to_email_address

@app.route('/sendtext', methods=['POST'])
def send_text():
    if request.method == "POST":
        phone_number_to = request.form['number']
        category = request.form['template']
        # update here to switch templates
        content = TextContent.test_obj.content
        #print secrets.get_phone_number_from, phone_number_to, content
        result = text.send(secrets.get_phone_number_from(), phone_number_to, content)
        return result

def which_template(category):
    return

if __name__ == '__main__':
    app.debug = True
    app.run()
