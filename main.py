'''import time
import scratchattach as scratch3
session = scratch3.login("TheBurgerFollower", "TheBurger")
while True:
    project = session.connect_project("884084370")
    project.post_comment(content="#MakeScratchBurgerAgain")'''
'''session = scratch3.login("BurgerArmy1", "TheBurger")
    user = session.connect_user("griffpatch")
    time.sleep(1)
    user.post_comment("Become A Follower")
    time.sleep(1)
'''

import time
import scratchattach as scratch3
from random import randint
iteratons = 1
while True:
    session = scratch3.login("qsefthukl", "qsefthuk")
    '''user = session.connect_user("griffpatch")
    user.post_comment(str(randint(1,999999999999999999999999)))
    iteratons = iteratons + 1
    time.sleep(1)'''
    project = session.connect_project("911931288")
    project.love()
    project.unlove()
    project.favorite()
    project.unfavorite()
    project.post_view()
