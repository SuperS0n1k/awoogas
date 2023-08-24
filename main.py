import scratchattach as scratch3

session = scratch3.login("TheBurgerFollower", "TheBurger")
print(session.session_id)

user = scratch3.get_user("scratchcat")
while True:
    user.follow()
    user.unfollow()
    
