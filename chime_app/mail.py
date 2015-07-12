import sendgrid, secrets

def test():
    return 'THIS IS THE SENDGRID MODULE'

def send(to_email_address, from_email_address, subject, content):
    '''Send email through Sendgrid'''
    sg = sendgrid.SendGridClient(secrets.get_sendgrid_username(), secrets.get_sendgrid_password())
    message = sendgrid.Mail()
    message.add_to(to_email_address)
    message.set_from(from_email_address)
    message.set_subject(subject)
    message.set_html(content)

    status, msg = sg.send(message)
    return {'status': status, 'msg': msg}

