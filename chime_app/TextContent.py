class TextContent:
    def __init__(self, name):
        self.name = name
        self.content = 'Default Content'
test_obj = TextContent('Test')
test_obj.content = 'cool test content'

template1 = TextContent('temp1')
template1.content = 'cool test content 1'

template2 = TextContent('temp2')
template2.content = 'cool test content 2'

template3 = TextContent('temp1')
template3.content = 'cool test content 3'
