from flask import Flask, render_template, request
import mail, MailContent, text, TextContent, secrets
# from flask.ext.mongoengine import MongoEngine

application = Flask(__name__)

@application.route('/', methods=['GET'])
def index():
    if request.method == "GET":
        return render_template('index.html')

@application.route('/sendmail', methods=['POST'])
def send_mail():
    if request.method == "POST":
        to_email_address = request.form['email']
        category = request.form['template']
        severity = request.form['severity']
        from_email_address = 'julie.yc.pan@gmail.com' # switch out to official email
        # update here to switch templates
        selected_template = which_MailContent_obj(category, severity)
        subject = selected_template.subject
        content = selected_template.content
        result = mail.send(to_email_address, from_email_address, subject, content)
        print str(result)
        return to_email_address

@application.route('/sendtext', methods=['POST'])
def send_text():
    if request.method == "POST":
        phone_number_to = request.form['number']
        category = request.form['template']
        severity = request.form['severity']
        # update here to switch templates
        selected_template = which_TextContent_obj(category, severity)
        content = selected_template.content
        result = text.send(secrets.get_phone_number_from(), phone_number_to, content)
        # result = 'test'
        return result

def which_MailContent_obj(category, severity):
    if severity == 'oops':
        if category == 'rapeJoke':
            return MailContent.template1
        elif category == 'compSituation':
            return MailContent.template2
        elif category == 'ignoreSign':
            return MailContent.template3
    elif severity == 'ouch':
        if category == 'rapeJoke':
            return MailContent.template4
        elif category == 'compSituation':
            return MailContent.template5
        elif category == 'ignoreSign':
            return MailContent.template6
    return

def which_TextContent_obj(category, severity):
    if severity == 'oops':
        if category == 'rapeJoke':
            return TextContent.template1
        elif category == 'compSituation':
            return TextContent.template2
        elif category == 'ignoreSign':
            return TextContent.template3
    elif severity == 'ouch':
        if category == 'rapeJoke':
            return TextContent.template4
        elif category == 'compSituation':
            return TextContent.template5
        elif category == 'ignoreSign':
            return TextContent.template6
    return

if __name__ == '__main__':
    application.debug = False
    application.run()
