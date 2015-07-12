# chimehack
Should probably add our slides content here.

### Requirements
Clone the repo:
`git clone https://github.com/ycp217/chimehack.git`

You got to install flask to run this.
```
pip install Flask
pip install sendgrid
pip install flask-script
pip install mongoengine
pip instaall flask_mongoengine
```

Run this by:
`python app.py`

Make your own `secrets.py`:
```
def get_api_username():
  return YOUR_SENDGRID_USERNAME

def get_api_password():
  return YOUR_SENDGRID_PASSWORD

def get_nexmo_key():
    return YOUR_NEXMO_KEY

def get_nexmo_secret():
    return YOUR_NEXMO_SECRET
```
