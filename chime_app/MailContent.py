# -*- coding: utf-8 -*-

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
template1.content = '<html><body><div class="container" style="width: 750px; font-family: "Helvetica", sans-serif;"><div style="color: #776f6d;"></div><div style="border-bottom: 3px solid #f0532d; font-weight: regular"></div><div style="padding-bottom: 15px; border-bottom: 3px solid #fdb740; font-weight: regular"></div><div style="font-family: "Helvetica", sans-serif; line-height: 32px; padding-bottom: 25px;"><h3 color: #f0532d;>Hey there, yesterday, people noticed that you made a joke or comment that made light of rape. 80% of college-aged men report being uncomfortable when women are belittled or mistreated, but it can be hard for them to recognize which actions count as mistreating women, or creating a hostile environment. Your friend(s) sent this message to give you a heads up that your comment fell under that category, and to help you be part of creating a more welcoming environment in the future.</h3></div><div class="container" style="padding-bottom: 15px; padding-top: 15px;"><h4 style="color:#776f6d; text-transform: uppercase;">Why Is This A Problem?</h4><p style="color:#776f6d; line-height: 24px;">Making light of sexual assault and rape contributes to an environment in which these behaviors are considered acceptable, and survivors feel unsupported. Sexual assault is never acceptable and survivors should always be supported. Even if the intent is not to directly threaten anybody, joking about the subject implicitly tells those around you that rape is no big deal, which may lead others to feel justified in assault behavior, or to underplay its severity.</p></div><div class="container" style="padding-bottom: 15px;"><h4 style="color:#776f6d; text-transform: uppercase;">What You Can Do</h4><p style="color:#776f6d; line-height: 24px;">In the future, lead by example and avoid using sexual assault and violence as a punchline. We can think of lots of topics that are both funny, and nonthreatening, and we’re sure you can too. Go one step further and speak out when you see others making rape or assault jokes. Remember that your voice can be a powerful part of changing the attitudes of those around you, but if you don’t feel comfortable calling someone out in person, send them an anonymous message like this one at thinktwiceforchange.com.</p><p style="color:#776f6d; line-height: 24px;">If you would like to learn more about creating supportive environment, ending violence against women, and the ins-and-outs of the rape culture that makes these jokes seem ok, check out some of these resources:</p></div></div></body></html>'

template2 = EmailContent('compSituation')
template2.subject = 'mail test subject 2'
template2.content = 'mail test content 2'

template3 = EmailContent('ignoreSign')
template3.subject = 'mail test subject 3'
template3.content = 'mail test content 3'
