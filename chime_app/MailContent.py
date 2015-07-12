class EmailContent:
    def __init__(self, name):
        self.name = name
        self.subject = 'Default Subject'
        self.content = 'Default Content'

test_obj = EmailContent('Test')
test_obj.subject = 'mail test subject'
test_obj.content = 'mail test content'

template1 = EmailContent('rapeJoke-oops')
template1.subject = 'mail test subject 1'
template1.content = 'mail test content 1'

template2 = EmailContent('compSituation-oops')
template2.subject = 'mail test subject 2'
template2.content = 'mail test content 2'

template3 = EmailContent('ignoreSign-oops')
template3.subject = 'mail test subject 3'
template3.content = 'mail test content 3'

template4 = EmailContent('rapeJoke-ouch')
template4.subject = 'mail test subject 1'
template4.content = 'mail test content 1'

template5 = EmailContent('compSituation-ouch')
template5.subject = 'mail test subject 2'
template5.content = 'mail test content 2'

template6 = EmailContent('ignoreSign-ouch')
template6.subject = 'mail test subject 3'
template6.content = 'mail test content 3'
