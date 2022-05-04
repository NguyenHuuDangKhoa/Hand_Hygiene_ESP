import network
import json

def setup_wifi(config_directory):
  """
  Setup wifi connection and return the network object, ssid and password.
  
  Example:
  sta_if, ssid, password = setup_wifi('./lib/config.json')
  
  """
  sta_if = network.WLAN(network.STA_IF) # create station interface
  with open("config.json") as file: # open config file
    config = json.load(file) # load config file and deserialize it into dictionary object
  return(sta_if, config.get("wifi", {}).get("ssid"), config.get("wifi", {}).get("password")) # return station interface and ssid and password from the config dict


def connect_wifi(sta_if, ssid, password):
  """
  Connect to wifi network with input ssid and password.
  
  Example:
  connect_wifi(sta_if, ssid, password)
  """
  sta_if.active(True) # activate station interface
  while not sta_if.isconnected():
    print('connecting to network...')
    sta_if.connect(ssid, password) # connect to network with ssid and password
    while not sta_if.isconnected():
      print('.')
      

def disconnect_wifi(sta_if):
  """_summary_
  Disconnect to the current wifi network
  
  Example:
  disconnect_wifi(sta_if)
  """
  sta_if.active(False) # deactivate station interface
  