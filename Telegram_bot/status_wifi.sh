#!/bin /bash
uci show wireless.radio0 | egrep 'txpower'\|'disabled' | tr -d \' > status_wifi.txt #Create File

sleep 1s

wifi_on=$(grep -w 'wireless.radio0.disabled=0' status_wifi.txt)
wifi_off=$(grep -w 'wireless.radio0.disabled=1' status_wifi.txt)
min=$(grep -w 'wireless.radio0.txpower=3' status_wifi.txt)
max=$(grep -w 'wireless.radio0.txpower=21' status_wifi.txt)


#echo $min
#echo $wifi_on
#echo $wifi_off

if [[ $wifi_on == 'wireless.radio0.disabled=0' ]]
    then
        #echo $wifi_on
        grep -r -l 'wireless.radio0.disabled=0' status_wifi.txt | xargs sed -i 's/wireless.radio0.disabled=0/WIFI_On/g'
fi

if [[ $wifi_off == 'wireless.radio0.disabled=1' ]]
    then
        #echo $wifi_off
        uci show wireless.radio0 | egrep 'disabled' | tr -d \' > status_wifi.txt
        grep -r -l 'wireless.radio0.disabled=1' status_wifi.txt | xargs sed -i 's/wireless.radio0.disabled=1/WIFI_Off/g'
fi
if [[ $min == 'wireless.radio0.txpower=3' ]]
    then
        #echo 'mini'
        grep -r -l 'wireless.radio0.txpower=3' status_wifi.txt | xargs sed -i 's/wireless.radio0.txpower=3/Мощность 1 %/g'
fi

if [[ $max == 'wireless.radio0.txpower=21' ]]
    then
        grep -r -l 'wireless.radio0.txpower=21' status_wifi.txt | xargs sed -i 's/wireless.radio0.txpower=21/Мощность 100 %/g'
fi



#grep -r -l 'wireless.radio0.disabled' status_wifi.txt | xargs sed -i 's/wireless.radio0.disabled/WIFI_On/g'
#grep -r -l 'wireless.radio0.disabled='1'' status_wifi.txt | xargs sed -i 's/wireless.radio0.disabled='1'/WIFI_Off/g'