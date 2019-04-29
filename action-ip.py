#!/usr/bin/env python3

import socket
from hermes_python.hermes import Hermes

def get_ip (hermes, message):
    msg = ""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        msg = "Meine Adresse lautet: " + ip
    except:
        msg = "Tut mir leid, das kann ich dir gerade selbst nicht sagen."

    hermes.publish_end_session(message.session_id, msg)

with Hermes("localhost:1883") as h:
    h \
        .subscribe_intent("tierlord:WieIstDeineIP", get_ip) \
        .start()