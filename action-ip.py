#!/usr/bin/env python3

import os
from hermes_python.hermes import Hermes

def split_ip (ip):
    ip_arr = ip.split('.')

    msg = ""

    for part in range(4):
        for i in range (len(ip_arr[part])):
            msg += ip_arr[part][i] + " "
        if part < 3:
            msg += "punkt "
    
    return msg

def get_ip (hermes, message):
    msg = ""
    try:
        ipv4 = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]
        msg = "Meine Adresse lautet: " + split_ip(ipv4)
    except:
        try:
            ipv4 = os.popen('ip addr show wlan0').read().split("inet ")[1].split("/")[0]
            msg = "Meine Wehlahn Adresse lautet: " + split_ip(ipv4)
        except:
            msg = "Tut mir leid, das kann ich dir gerade selbst nicht sagen."

    hermes.publish_end_session(message.session_id, msg)

with Hermes("localhost:1883") as h:
    h \
        .subscribe_intent("tierlord:WieIstDeineIP", get_ip) \
        .start()