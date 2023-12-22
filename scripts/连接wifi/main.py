import pywifi
import time
from pywifi import const

def autoConnectWifi():
    wifi = pywifi.PyWiFi()
    inter = wifi.interfaces()[0]
    # inter.disconnect()
    # time.sleep(3)
    if inter.status() == const.IFACE_DISCONNECTED:
        f = pywifi.Profile()
        f.ssid = "ewell-work"
        f.key = "ewellyh9500"
        f.auth = const.AUTH_ALG_OPEN
        f.cipher = const.CIPHER_TYPE_CCMP
        f.akm.append(const.AKM_TYPE_WPA2PSK)
        inter.remove_all_network_profiles()
        temp_p = inter.add_network_profile(f)
        inter.connect(temp_p)
        time.sleep(3)
        if inter.status() == const.IFACE_CONNECTED:
            print("连接成功")
            return True
        else:
            return False
    else:
        print("已连接")
        return True

if __name__ == "__main__":
    autoConnectWifi()

