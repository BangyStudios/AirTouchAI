from enum import Enum

class Models(Enum):
    AirTouch4 = 0

"""
Creates a new Air Conditioner Controller object

"""
class Controller:
    """Constructor for the Air Conditioner Controller object"""
    def __init__(self, model, host) -> None:
        self.model: Models = model
        self.host: str = host

        """Initiates the appropriate API/driver(s) depending on the model"""
        if (self.model == Models.AirTouch4):
            from apis.airtouch4.airtouch import AirTouch, AirTouchStatus
            self.api: AirTouch = AirTouch(self.host)

        pass

    """Returns the current temperature(s) for room(s)"""
    def get_temperature(self) -> int:
        pass


controller: Controller = Controller(Models.AirTouch4, "192.168.0.10")