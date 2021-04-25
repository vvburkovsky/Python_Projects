#!/bin /bash

cd /usr/bin/Telegram_bot #Bot Directory
uci show wireless.radio0 | egrep 'txpower'\|'disabled' | tr -d \' > status_wifi.txt #Create File
sleep 1s

#поиск строки в файле и назначение переменной:
wifi_on=$(grep -w 'wireless.radio0.disabled=0' status_wifi.txt) 
wifi_off=$(grep -w 'wireless.radio0.disabled=1' status_wifi.txt)
min=$(grep -w 'wireless.radio0.txpower=3' status_wifi.txt)
max=$(grep -w 'wireless.radio0.txpower=21' status_wifi.txt)

#замена строк:
if [[ $wifi_off == 'wireless.radio0.disabled=1' ]]
    then
        uci show wireless.radio0 | egrep 'disabled' | tr -d \' > status_wifi.txt
        grep -r -l 'wireless.radio0.disabled=1' status_wifi.txt | xargs sed -i 's/wireless.radio0.disabled=1/WIFI_ВЫКЛ/g'

elif [[ $wifi_on == 'wireless.radio0.disabled=0' ]]
    then
        grep -r -l 'wireless.radio0.disabled=0' status_wifi.txt | xargs sed -i 's/wireless.radio0.disabled=0/WIFI_ВКЛ/g'
fi

if [[ $min == 'wireless.radio0.txpower=3' ]]
    then
        grep -r -l 'wireless.radio0.txpower=3' status_wifi.txt | xargs sed -i 's/wireless.radio0.txpower=3/Мощность 1 %/g'

elif [[ $max == 'wireless.radio0.txpower=21' ]]
    then
        grep -r -l 'wireless.radio0.txpower=21' status_wifi.txt | xargs sed -i 's/wireless.radio0.txpower=21/Мощность 100 %/g'
fi