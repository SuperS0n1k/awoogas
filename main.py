import time
import scratchattach as scratch3
session = scratch3.Session(".eJxVj8FugzAQRP_F54Qa2wGcW3KI1EqtSltV6cmyzQIuYCMwQk3Vf68tccltNTuz--YXLTNMVg6AjuijhfMyNTBdXN-7FSa0Q0IuvhXRJEwVPGlaUMrzjISdh9lr5zoTw6ubOqjuE0rqDmyMRQ2sN1p642yyLebkDcZ-E8-bOdx1YYghVmHIVYqpUozkBU8xo5RWrMql5EofS3wtS9H48faYvn7un5_e-x8nuDpddTjTu8bYvRkjNU1SfEgYTwihkbGXtllkE8HDqx2qvoPghDcD3JyN8mmAKZA9vMAqvkK3-2atnNtgqjGtsdQ1xlRmoBQnAS_jrMCFJkWe1cUBa0UY-vsHQ2B0xQ:1qZBNX:LCf299hoqH-WxNqS7b-3hT2ogxo", username="TheBurgerFollower")
while True:
    time.sleep(5)
    project = session.connect_project("884084370")
    project.post_comment(content="#MakeScratchBurgerAgain")
