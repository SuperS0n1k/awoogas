'''import time
import scratchattach as scratch3
session = scratch3.login("TheBurgerFollower", "TheBurger")
while True:
    project = session.connect_project("884084370")
    project.post_comment(content="#MakeScratchBurgerAgain")'''

import time
import scratchattach as scratch3
session = scratch3.login("TheBurgerFollower", "TheBurger")
while True:
    user = session.connect_user("griffpatch")
    time.sleep(1)
    user.follow()
    time.sleep(1)
    user.post_comment("Become A Follower")
    time.sleep(1)
    user.unfollow()
    time.sleep(1)
