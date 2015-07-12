class EmailContent:
    def __init__(self, name):
        self.name = name
        self.subject = 'Default Subject'
        self.content = 'Default Content'
test_obj = EmailContent('Test')
test_obj.subject = 'cool test subject'
test_obj.content = 'cool test content'

template1 = EmailContent('temp1')
template1.subject = 'cool test subject 1'
template1.content = 'cool test content 1'

template2 = EmailContent('temp2')
template2.subject = 'cool test subject 2'
template2.content = 'cool test content 2'

template3 = EmailContent('temp1')
template3.subject = 'cool test subject 3'
template3.content = 'cool test content 3'
