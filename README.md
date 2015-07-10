# chimehack
Should probably add our slides content here.

### Requirements
Clone the repo:
`git clone https://github.com/ycp217/chimehack.git`

You got to install flask to run this.

`pip install Flask`

`pip install sendgrid`

Run this by:
`python app.py`

Make your own `secrets.py`:
```
def get_api_username():
  return YOUR_SENDGRID_USERNAME

def get_api_password():
  return YOUR_SENDGRID_PASSWORD
```
