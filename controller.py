import asyncio
from api.airtouch4pyapi import AirTouch
"""
Creates a new Air Conditioner Controller object
"""
class Controller:
    def __init__(self, host):
        """Constructor for the Air Conditioner Controller object"""
        self.host = host
        self.api = AirTouch(host)
        asyncio.run(self.api.UpdateInfo())

    def get_info(self):
        """Update information using API"""
        asyncio.run(self.api.UpdateInfo())

    def get_temperature(self) -> None:
        """Returns the current temperature(s) for room(s)"""
        #TODO Add API to return global temperature
        pass

    def set_mode_ac(self, ac, mode):
        """Sets the AC mode i.e. ['Cool', 'Fan', 'Dry', 'Heat', 'Auto']"""
        asyncio.run(self.api.SetCoolingModeForAc(ac, mode))
        
    def set_fan_ac(self, ac, fan):
        """Sets the AC fan i.e. ['Auto', 'Low', 'Medium', 'High']"""
        asyncio.run(self.api.SetFanSpeedForAc(ac, fan))
        
    def set_power_ac(self, ac, power):
        """Toggles the AC power on=1 or off=0"""
        if (power):
            asyncio.run(self.api.TurnAcOn(ac))
        else:
            asyncio.run(self.api.TurnAcOff(ac))