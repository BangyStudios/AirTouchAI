import controller
import time

controller = controller.Controller("192.168.0.14")
mode_current = None

while True:
    with open("/home/icb/Code/Enphase-Tools/data/temp.txt", "r") as solar_net:
        power_net = int(solar_net.read())
    if (power_net > 5000):
        if (mode_current != "Cool"):
            controller.set_mode_ac(0, "Cool")
            controller.set_fan_ac(0, "Auto")
            mode_current = "Cool"
            print("Cool")
    elif (power_net < -1000):
        if (mode_current != "Fan"):
            controller.set_mode_ac(0, "Fan")
            mode_current = "Fan"
            print("Fan")
    time.sleep(10)