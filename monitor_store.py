# coming from the core.py file, some functions are defined to keep this file clean
from core import TemperatureMonitor
import board

monitor = TemperatureMonitor(board.D5)
monitor.run()