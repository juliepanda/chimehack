class TextContent:
    def __init__(self, name):
        self.name = name
        self.content = 'Default Content'
test_obj = TextContent('Test')
test_obj.content = 'text test content'

template1 = TextContent('temp1')
template1.content = 'text test content 1'

template2 = TextContent('temp2')
template2.content = 'text test content 2'

template3 = TextContent('temp1')
template3.content = 'text test content 3'

template4 = TextContent('rapeJoke-ouch')
template4.content = 'mail test content 1'

template5 = TextContent('compSituation-ouch')
template5.content = 'mail test content 2'

template6 = TextContent('ignoreSign-ouch')
template6.content = 'mail test content 3'
