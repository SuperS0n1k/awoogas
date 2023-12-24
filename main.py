import time
import random
import scratchattach as scratch3

while True:
	conn = scratch3.connect_tw_cloud("944067867")
	q = scratch3.get_tw_var("523967150", "1")
	w = scratch3.get_tw_var("523967150", "2")
	e = scratch3.get_tw_var("523967150", "3")
	r = scratch3.get_tw_var("523967150", "4")
	t = scratch3.get_tw_var("523967150", "5")
	y = scratch3.get_tw_var("523967150", "6")
	u = scratch3.get_tw_var("523967150", "7")
	i = scratch3.get_tw_var("523967150", "8")
	o = scratch3.get_tw_var("523967150", "9")
	conn.set_var("1", q)
	conn.set_var("2", w)
	conn.set_var("3", e)
	conn.set_var("4", r)
	conn.set_var("5", t)
	conn.set_var("6", y)
	conn.set_var("7", u)
	conn.set_var("8", i)
	conn.set_var("9", o)
