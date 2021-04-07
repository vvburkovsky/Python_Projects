#!/bin /bash

# Set WiFi power to min
uci set wireless.radio0.txpower=3

wifi reload
sleep 1s
uci commit wireless; wifi