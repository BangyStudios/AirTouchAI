import controller
import solar

controller = controller.Controller("192.168.0.14")
solar_crawler = solar.Crawler()
solar_calculator = solar.Calculator()

while True:
    solar.update_data()
    if (solar_calculator.get_net(solar.get_data()) > 4000):
        controller.set_mode_ac(0, "Cool")
        controller.set_fan_ac("Auto")
    elif (solar_calculator.get_net(solar.get_data()) < -1000):
        controller.set_mode_ac(0, "Fan")
    else:
        pass