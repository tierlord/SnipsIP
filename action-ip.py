#!/usr/bin/env python3

import os
from hermes_python.hermes import Hermes

def get_ip (hermes, message):
    msg = ""
    try:
        ipv4 = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]
        msg = "Meine Adresse lautet: " + ipv4
    except:
        try:
            ipv4 = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]
            msg = "Meine Adresse lautet: " + ipv4
        except:
            msg = "Tut mir leid, das kann ich dir gerade selbst nicht sagen."

    return hermes.publish_end_session(message.session_id, msg)

with Hermes("localhost:1883") as h:
    h \
        .subscribe_intent("tierlord:WieIstDeineIP", get_ip) \
        .start()