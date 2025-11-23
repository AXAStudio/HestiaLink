# HestiaLink API

HestiaHub is a modular, plug-and-play Home Automation Simulator built with FastAPI.  
It allows you to simulate and control various smart devices via a RESTful API, with support for fully self-contained device modules.

## Features

- **Dynamic Device Loading**  
  Drop a new device module into `models/devices/` and it is automatically registered with the API without additional configuration.

- **Abstract Base Device Interface**  
  All devices inherit from `HardwareModule` (ABC), ensuring a consistent interface:
  - `get_state()`
  - `send_command()`
  - Optional `tick()` for simulation

- **Self-Contained Modules**  
  Each device can contain its own internal logic, including motors, sensors, and simulation logic.

- **Simulation Ready**  
  Supports periodic updates with `tick()` for simulating gradual changes, such as motor movement or temperature adjustment.
