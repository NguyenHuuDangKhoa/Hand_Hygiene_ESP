import wifi
sta_if, ssid, password = wifi.setup_wifi('./lib/config.json')

wifi.connect_wifi(sta_if, ssid, password)