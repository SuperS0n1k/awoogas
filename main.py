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
iteratons = 1
while True:
    session = scratch3.login("DownWithST1", "DownWithSTs")
    user = session.connect_user("griffpatch")
    user.post_comment("Down with the ST. This message has been delivered " + str(iteratons) + " times. ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴄᴏꜰꜰᴇᴇ.")
    iteratons = iteratons + 1
    session = scratch3.login("DownWithST2", "DownWithSTs")
    user = session.connect_user("griffpatch")
    user.post_comment("Down with the ST. This message has been delivered " + str(iteratons) + " times. ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴄᴏꜰꜰᴇᴇ.")
    iteratons = iteratons + 1
    time.sleep(1)
