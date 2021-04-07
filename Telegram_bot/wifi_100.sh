#!/bin /bash

# Set WiFi power to max
uci set wireless.radio0.txpower=21 #Driver default

wifi reload
sleep 1s
uci commit wireless; wifi
