#!/usr/bin/env python3

import netifaces as ni
from hermes_python.hermes import Hermes

def get_ip (hermes, message):
    msg = ""
    try: 
        ni.ifaddresses('eth0')
        ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        print("IP : ", ip)
        msg = "Meine Adresse lautet: " + ip
    except:
        msg = "Tut mir leid, das kann ich dir gerade selbst nicht sagen."
        print("Unable to get Hostname and IP") 

    hermes.publish_end_session(message.session_id, msg)

with Hermes("localhost:1883") as h:
    h \
        .subscribe_intent("tierlord:WieIstDeineIP", get_ip) \
        .start()