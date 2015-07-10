import sendgrid, secrets

sg = sendgrid.SendGridClient(secrets.get_api_username, secrets.get_api_password)
message = sendgrid.Mail()

message.add_to("test@sendgrid.com")
message.set_from("you@youremail.com")
message.set_subject("Sending with SendGrid is Fun")
message.set_html("and easy to do anywhere, even with Python")

sg.send(message)
