# routers/devices.py

from fastapi import APIRouter, HTTPException
from app.main import manager  # import singleton manager

router = APIRouter()

@router.get("/")
def list_devices():
    return manager.all_devices()

@router.get("/{device_id}")
def get_device(device_id: str):
    device = manager.get(device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device.get_state()

@router.post("/{device_id}/command")
def send_command(device_id: str, payload: dict):
    device = manager.get(device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    try:
        device.send_command(payload["command"], payload.get("args"))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return device.get_state()
