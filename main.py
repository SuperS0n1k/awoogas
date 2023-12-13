import time
import random
import scratchattach as scratch3
while True:
	session = scratch3.login("SBThelper2", "qsefthi")
	user = session.connect_user("ceebee")
	time.sleep(1)
	user.post_comment("["+ str(random.randint(1,999999)) +"]")
	time.sleep(1)
	session = scratch3.login("SBThelper3", "qsefthi")
	user = session.connect_user("paddle2see")
	time.sleep(1)
	user.post_comment("["+ str(random.randint(1,999999)) +"]")
	time.sleep(1)
	session = scratch3.login("SBThelper4", "qsefthi")
	user = session.connect_user("zinnea")
	time.sleep(1)
	user.post_comment("["+ str(random.randint(1,999999)) +"]")
	time.sleep(1)
