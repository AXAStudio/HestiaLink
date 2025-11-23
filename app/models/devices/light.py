from models.base import HardwareModule
from typing import Dict, Any

class LightModule(HardwareModule):
    """A simple light device with on/off and brightness control."""

    def __init__(self, device_id: str, name: str):
        super().__init__(device_id, name, device_type="light")
        self.is_on: bool = False
        self.brightness: int = 100  # 0-100

    def get_state(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "type": self.device_type,
            "is_on": self.is_on,
            "brightness": self.brightness,
        }

    def send_command(self, command: str, args: Dict[str, Any] = None):
        if command == "turn_on":
            self.is_on = True
        elif command == "turn_off":
            self.is_on = False
        elif command == "set_brightness":
            if args and "value" in args:
                self.brightness = max(0, min(100, args["value"]))
        else:
            raise ValueError(f"Unknown command '{command}' for LightModule")

    def tick(self, dt: float = 1.0):
        # Optional: simulate effects like fading
        pass
