class EmailContent:
    def __init__(self, name):
        self.name = name
        self.subject = 'Default Subject'
        self.content = 'Default Content'
test_obj = EmailContent('Test')
test_obj.subject = 'cool test subject'
test_obj.content = 'cool test content'

