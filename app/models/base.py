from abc import ABC, abstractmethod
from typing import Dict

class HardwareModule(ABC):
    """
    Base class for all hardware modules.
    Every module must implement get_state and send_command.
    tick() is optional for simulation updates.
    """

    def __init__(self, id: str, name: str, device_type: str):
        self.id = id
        self.name = name
        self.device_type = device_type

    @abstractmethod
    def get_state(self) -> Dict:
        """Return a dictionary representing the current state of the device."""
        pass

    @abstractmethod
    def send_command(self, command: str, args: Dict = None):
        """Send a command to the device."""
        pass

    def tick(self, dt: float = 1.0):
        """
        Optional simulation tick.
        dt = timestep in seconds.
        """
        pass
