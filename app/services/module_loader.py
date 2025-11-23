import importlib
import pkgutil
from pathlib import Path
from models.base import HardwareModule
from services.device_manager import DeviceManager

def auto_load_devices(manager: DeviceManager, package="models.devices"):
    """
    Automatically finds all HardwareModule subclasses in devices folder
    and registers them in the DeviceManager.
    """
    package_obj = importlib.import_module(package)
    package_path = Path(package_obj.__file__).parent

    for _, module_name, _ in pkgutil.iter_modules([str(package_path)]):
        full_module_name = f"{package}.{module_name}"
        module = importlib.import_module(full_module_name)

        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type) and issubclass(attr, HardwareModule) and attr is not HardwareModule:
                device_id = attr_name.lower()
                if manager.get(device_id):
                    continue
                device_instance = attr(device_id=device_id, name=attr_name)
                manager.register(device_instance)
                print(f"Auto-registered device: {device_id}")
