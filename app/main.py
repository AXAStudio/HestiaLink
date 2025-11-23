from fastapi import FastAPI
from routers import devices
from services.device_manager import DeviceManager
from services.module_loader import auto_load_devices

app = FastAPI(title="HestiaHub API")
manager = DeviceManager()

auto_load_devices(manager)

app.include_router(devices.router, prefix="/devices", tags=["devices"])
