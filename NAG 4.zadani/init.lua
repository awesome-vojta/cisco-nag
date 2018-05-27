print('init.lua ver 1.2')
wifi.setmode(wifi.STATION)
print('set mode=STATION (mode='..wifi.getmode()..')')
print('MAC: ',wifi.sta.getmac())
print('chip: ',node.chipid())
print('heap: ',node.heap())

-- konfigurace wifi, v zavorce je zapsano 
-- jmeno wifi acces pointu a jeho SSID heslo
wifi.sta.config("Trablsutink","trablwifi")
wifi.sta.connect()
print(wifi.sta.status())
print(wifi.sta.getip())
tmr.delay(1000000)
