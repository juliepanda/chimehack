import sendgrid, secrets

sg = sendgrid.SendGridClient(secrets.get_api_username(), secrets.get_api_password())
message = sendgrid.Mail()

message.add_to("ycp217@nyu.edu")
message.set_from("julie.yc.pan@gmail.com")
message.set_subject("Hi from Chimehack flask app")
message.set_text("ALOHA THERE <3 <3 <3")

status, msg = sg.send(message)

print status, msg
