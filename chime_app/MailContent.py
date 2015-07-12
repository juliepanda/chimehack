# -*- coding: utf-8 -*-

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
template1.content = '<html><body><div class="container" style="width: 750px; font-family: "Helvetica", sans-serif;"><div style="color: #776f6d;"></div><div style="border-bottom: 3px solid #f0532d; font-weight: regular"></div><div style="padding-bottom: 15px; border-bottom: 3px solid #fdb740; font-weight: regular"></div><div style="font-family: "Helvetica", sans-serif; line-height: 32px; padding-bottom: 25px;"><h3 color: #f0532d;>Hey there, yesterday, people noticed that you made a joke or comment that made light of rape. 80% of college-aged men report being uncomfortable when women are belittled or mistreated, but it can be hard for them to recognize which actions count as mistreating women, or creating a hostile environment. Your friend(s) sent this message to give you a heads up that your comment fell under that category, and to help you be part of creating a more welcoming environment in the future.</h3></div><div class="container" style="padding-bottom: 15px; padding-top: 15px;"><h4 style="color:#776f6d; text-transform: uppercase;">Why Is This A Problem?</h4><p style="color:#776f6d; line-height: 24px;">Making light of sexual assault and rape contributes to an environment in which these behaviors are considered acceptable, and survivors feel unsupported. Sexual assault is never acceptable and survivors should always be supported. Even if the intent is not to directly threaten anybody, joking about the subject implicitly tells those around you that rape is no big deal, which may lead others to feel justified in assault behavior, or to underplay its severity.</p></div><div class="container" style="padding-bottom: 15px;"><h4 style="color:#776f6d; text-transform: uppercase;">What You Can Do</h4><p style="color:#776f6d; line-height: 24px;">In the future, lead by example and avoid using sexual assault and violence as a punchline. We can think of lots of topics that are both funny, and nonthreatening, and we’re sure you can too. Go one step further and speak out when you see others making rape or assault jokes. Remember that your voice can be a powerful part of changing the attitudes of those around you, but if you don’t feel comfortable calling someone out in person, send them an anonymous message like this one at thinktwiceforchange.com.</p><p style="color:#776f6d; line-height: 24px;">If you would like to learn more about creating supportive environment, ending violence against women, and the ins-and-outs of the rape culture that makes these jokes seem ok, check out some of these resources:</p></div></div></body></html>'

template2 = EmailContent('compSituation-oops')
template2.subject = 'mail test subject 2'
template2.content = '<html><body><div class="container" style="width: 750px; font-family: "Helvetica", sans-serif;"><div style="color: #776f6d;"></div><div style="border-bottom: 3px solid #f0532d; font-weight: regular"></div><div style="padding-bottom: 15px; border-bottom: 3px solid #fdb740; font-weight: regular"></div><div style="font-family: "Helvetica", sans-serif; line-height: 32px; padding-bottom: 25px;"><h3 color: #f0532d;>Hey there, yesterday, 5 people noticed that you discussed plans to use alcohol or drugs to lower women’s inhibitions, to isolate women at a party or social outing, or to otherwise target women and lower their defenses to increase yours or your friend’s chances of having sex.</h3></div><div class="container" style="padding-bottom: 15px; padding-top: 15px;"><h4 style="color:#776f6d; text-transform: uppercase;">Why Is This A Problem?</h4><p style="color:#776f6d; line-height: 24px;">Planning to target women at parties and lower their inhibitions with alcohol or drugs is a form of sexual assault. 80% of college age men report being uncomfortable when women are belittled or mistreated, but they do not step up in part because it can be hard for them to recognize which actions count as mistreatment, or creating a hostile environment. Having sex with someone without receiving enthusiastic affirmative consent is rape, and intoxicated, threatened, or pressured people are not in a position to give affirmative consent to sex or sex acts. It’s part of your responsibility to identify situations in which sexual assault are likely to occur and prevent them whenever possible. If something seems like a bad idea, it probably is, and you should speak up.</p><p style="color:#776f6d; line-height: 24px;">Prioritizing your status with other men or the image of your masculinity over womens comfort comes at the direct expense of womens safety. Even if you do not feel like you are personally threatening a woman, your actions can create an environment in which it is easy and acceptable to mistreat women in general. They tell those around you that ignoring women’s agency is ok with you, which can allow others to feel justified in harassment and rape, and perpetrate rape culture. And remember that if you felt uncomfortable in this situation, and unable to speak out, you are not the only person in your group who understands that this is wrong- someone sent you this message didn’t they?</p></div><div class="container" style="padding-bottom: 15px;"><h4 style="color:#776f6d; text-transform: uppercase;">What You Can Do</h4><p style="color:#776f6d; line-height: 24px;">In the future, lead by example and make sure the women at your parties are treated as equals there to have fun, not as sexual object for hosts and other party-goers to take advantage of. Speak out when you hear others planning to make women vulnerable. Remember that your voice can be a powerful part of changing the attitudes of those around you, but if you don’t feel comfortable calling someone out in person, send them an anonymous message like this one at thinktwiceforchange.com.</p><p style="color:#776f6d; line-height: 24px;">If you would like to learn more about creating supportive environment, ending violence against women, affirmative consent and the definition of rape, and the ins and out of the rape culture that makes these plans and practices seem ok, check out some of these resources:</p></div></div></body></html>'

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
