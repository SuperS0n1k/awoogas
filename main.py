import os
import sys
import os.path
import scratchattach as scratch3
from scratchattach import Encoding
from time import sleep
session = scratch3.Session(".eJxVj09LxDAQxb9Lzru1adP82ZvCIoIoKyKsl5I0s21sm6xtSkHxuzuBXvY2vN-8N29-yTLD5PUI5ECeoAVv92RHar3Erk6odhaJLBitFFWIIsyxCaF3ybGGqQd7azC66TEGadLAR9fo6ILPNjBnb3AdNvFhW8bcgEMyGW5yLqlgcGHCKJVLxS0wWQpmBdOHs_-0r8d39_Eou-9n6tyyxuMp8lM3Y8wQWuf37opJtMxoXmVMZVSVqeOgfbvoNhXHUztiv1AIdXQj_ASf5PsRJmx29wJrfcbfbj_r9NzhEq8ELXKry8pyqS9SGKBc5rIoKBeSScsFGF0y8vcPFb9wDQ:1q0MP5:DkmPc69uXm8-Z1d64NWZaTaGNfo", username="iegend-")
conn = session.connect_cloud('930033180') #add your remixed project ID
variables = scratch3.get_cloud('930033180') #add your remixed project ID 
conn = session.connect_cloud('843162693') #add Original Project ID

def run_forever():
        try:
                while True:
		conn = session.connect_cloud('843162693') #add Original Project ID
		conn.set_var(key, var)
		print(var)
        except Exception:
                print("error")
                handle_exception()
                run_forever()
	
def handle_exception():
        # code here
        pass
    
run_forever()
