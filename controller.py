import asyncio
from api.airtouch import AirTouch, AirTouchStatus

"""
Creates a new Air Conditioner Controller object
"""
class Controller:
    """Constructor for the Air Conditioner Controller object"""
    def __init__(self, model, host):
        self.host = host
        self.api = AirTouch(host)
        asyncio.run(self.api.UpdateInfo())

    """Update information using API"""
    def get_info(self):
        asyncio.run(self.api.UpdateInfo())

    """Returns the current temperature(s) for room(s)"""
    def get_temperature(self) -> None:
        #TODO Add API to return global temperature
        pass

    """Sets the AC mode i.e. ['Cool', 'Fan', 'Dry', 'Heat', 'Auto']"""
    def set_mode(self, ac, mode):
        asyncio.run(self.api.SetCoolingModeForAc(0, mode))

controller: Controller = Controller("192.168.0.37")
controller.get_info()