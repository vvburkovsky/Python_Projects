def state ():
    file = open('/usr/bin/Telegram_bot/status_wifi.txt', encoding='utf-8')
    lines = file.read().splitlines()    
    try:
        line1 = str (lines[0])
        line2 = str (lines[1])
        status = (line1 + '\n' + line2)
        return status
    except:
        return line1
    file.close()