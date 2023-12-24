import time
import random
import scratchattach as scratch3

while True:
	conn = scratch3.connect_tw_cloud("944067867")
	q = scratch3.get_tw_var("523967150", "1")
	conn.set_var("1", q)
	conn.set_var("2", q)
	conn.set_var("3", q)
	conn.set_var("4", q)
	conn.set_var("5", q)
	conn.set_var("6", q)
	conn.set_var("7", q)
	conn.set_var("8", q)
	conn.set_var("9", q)
