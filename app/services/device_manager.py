from typing import Dict, Type
from models.base import HardwareModule

class DeviceManager:
    """
    Central registry for all HardwareModules.
    Supports registering, retrieving, listing, and ticking devices.
    """

    def __init__(self):
        self.devices: Dict[str, HardwareModule] = {}

    def register(self, device: HardwareModule):
        if device.id in self.devices:
            raise ValueError(f"Device with ID {device.id} is already registered.")
        self.devices[device.id] = device

    def get(self, device_id: str) -> HardwareModule | None:
        return self.devices.get(device_id)

    def all_devices(self):
        return [d.get_state() for d in self.devices.values()]

    def tick_all(self, dt: float = 1.0):
        """Call tick() on all devices (simulation step)."""
        for device in self.devices.values():
            device.tick(dt)
