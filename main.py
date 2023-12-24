import time
import random
import scratchattach as scratch3

while True:
	conn = scratch3.connect_tw_cloud("944067867")
	var = scratch3.get_tw_var("523967150", "1")
	conn.set_var("1", var)
	conn.set_var("2", var)
	conn.set_var("3", var)
	conn.set_var("4", var)
	conn.set_var("5", var)
	conn.set_var("6", var)
	conn.set_var("8", var)
	conn.set_var("9", var)
	conn = scratch3.connect_tw_cloud("523967150")
	var = scratch3.get_tw_var("944067867", "1")
	conn.set_var("1", var)
	conn.set_var("2", var)
	conn.set_var("3", var)
	conn.set_var("4", var)
	conn.set_var("5", var)
	conn.set_var("6", var)
	conn.set_var("8", var)
	conn.set_var("9", var)
