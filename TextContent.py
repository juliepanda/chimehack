class TextContent:
    def __init__(self, name):
        self.name = name
        self.content = 'Default Content'
test_obj = TextContent('Test')
test_obj.content = 'text test content'

template1 = TextContent('temp1')
template1.content = 'Yesterday, someone noticed that you made a joke about rape. A friend sent this message to give you a heads that it created a hostile environment for women. For more info about why this makes people uncomfortable, or what you can do to help make women safer, visit thinktwiceforchange.com/rapejokes'

template2 = TextContent('temp2')
template2.content = 'Yesterday, someone noticed that you made a joke about rape. A friend sent this message to give you a heads that it created a hostile environment for women. For more info about why this makes people uncomfortable, or what you can do to help make women safer, visit thinktwiceforchange.com/rapejokes'

template3 = TextContent('temp1')
template3.content = 'Yesterday, someone noticed that you made a joke about rape. A friend sent this message to give you a heads that it created a hostile environment for women. For more info about why this makes people uncomfortable, or what you can do to help make women safer, visit thinktwiceforchange.com/rapejokes'

template4 = TextContent('rapeJoke-ouch')
template4.content = 'Yesterday, someone noticed that you made a joke about rape. A friend sent this message to give you a heads that it created a hostile environment for women. For more info about why this makes people uncomfortable, or what you can do to help make women safer, visit thinktwiceforchange.com/rapejokes'

template5 = TextContent('compSituation-ouch')
template5.content = 'Yesterday, someone noticed that you made a joke about rape. A friend sent this message to give you a heads that it created a hostile environment for women. For more info about why this makes people uncomfortable, or what you can do to help make women safer, visit thinktwiceforchange.com/rapejokes'

template6 = TextContent('ignoreSign-ouch')
template6.content = 'Yesterday, someone noticed that you made a joke about rape. A friend sent this message to give you a heads that it created a hostile environment for women. For more info about why this makes people uncomfortable, or what you can do to help make women safer, visit thinktwiceforchange.com/rapejokes'
