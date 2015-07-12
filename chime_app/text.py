import requests, secrets, urllib

def test():
    return 'THIS IS THE TEXTING MODULE'

def send(from_number, to_number, text):
    '''send SMS via Nexmo service'''
    text = urllib.quote_plus(text)
    r = requests.get('https://rest.nexmo.com/sms/json?' + 'api_key=' + secrets.get_nexmo_key() + '&api_secret=' + secrets.get_nexmo_secret() + '&from=' + from_number + '&to=' + to_number + '&text=' + text)
    return r.text

