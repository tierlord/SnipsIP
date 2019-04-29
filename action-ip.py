#!/usr/bin/env python3

import socket
from hermes_python.hermes import Hermes

def get_ip (hermes, message):
    msg = ""
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("IP : ",host_ip)
        msg = "Meine Adresse lautet: " + host_ip
    except:
        msg = "Tut mir leid, das kann ich dir gerade selbst nicht sagen."
        print("Unable to get Hostname and IP") 

    hermes.publish_end_session(message.session_id, msg)

with Hermes("localhost:1883") as h:
    h \
        .subscribe_intent("tierlord:WieIstDeineIP", get_ip) \
        .start()