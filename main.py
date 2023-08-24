'''import time
import scratchattach as scratch3
session = scratch3.login("TheBurgerFollower", "TheBurger")
while True:
    project = session.connect_project("884084370")
    project.post_comment(content="#MakeScratchBurgerAgain")'''

import time
import scratchattach as scratch3

session = scratch3.ScratchSession()
session.login("TheBurgerFollower", "TheBurger")

while True:
    try:
        project = session.connect_project("884084370")
        project.post_comment("#MakeScratchBurgerAgain")
    except scratch3.ScratchConnectionError:
        print("Failed to connect to Scratch project. Retrying in 5 seconds...")
        time.sleep(5)
