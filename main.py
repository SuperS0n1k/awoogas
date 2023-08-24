'''import time
import scratchattach as scratch3
session = scratch3.login("TheBurgerFollower", "TheBurger")
while True:
    project = session.connect_project("884084370")
    project.post_comment(content="#MakeScratchBurgerAgain")'''

import time
import scratchattach as scratch3
session = scratch3.login("TheBurgerFollower", "TheBurger")
project = session.connect_project("884084370")
while True:
    project.love()
    project.unlove()
    project.favorite()
    project.unfavorite()
