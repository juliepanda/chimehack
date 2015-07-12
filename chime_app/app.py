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
        selected_template = which_MailContent_obj(category)
        subject = selected_template.subject
        content = selected_template.content
        result = mail.send(to_email_address, from_email_address, subject, content)
        print str(result)
        return to_email_address

@app.route('/sendtext', methods=['POST'])
def send_text():
    if request.method == "POST":
        phone_number_to = request.form['number']
        category = request.form['template']
        # update here to switch templates
        selected_template = which_TextContent_obj(category)
        content = selected_template.content
        result = text.send(secrets.get_phone_number_from(), phone_number_to, content)
        return result

def which_MailContent_obj(category):
    if category == 'rapeJoke':
        return MailContent.template1
    elif category == 'compSituation':
        return MailContent.template2
    elif category == 'ignoreSign':
        return MailContent.template3
    return

def which_TextContent_obj(category):
    if category == 'rapeJoke':
        return TextContent.template1
    elif category == 'compSituation':
        return TextContent.template2
    elif category == 'ignoreSign':
        return TextContent.template3
    return

if __name__ == '__main__':
    app.debug = True
    app.run()
