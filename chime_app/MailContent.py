class EmailContent:
    def __init__(self, name):
        self.name = name
        self.subject = 'Default Subject'
        self.content = 'Default Content'
test_obj = EmailContent('Test')
test_obj.subject = 'mail test subject'
test_obj.content = 'mail test content'

template1 = EmailContent('rapeJoke')
template1.subject = 'mail test subject 1'
template1.content = 'mail test content 1'

template2 = EmailContent('compSituation')
template2.subject = 'mail test subject 2'
template2.content = 'mail test content 2'

template3 = EmailContent('ignoreSign')
template3.subject = 'mail test subject 3'
template3.content = 'mail test content 3'
