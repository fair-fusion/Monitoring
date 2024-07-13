from core import TemperatureMonitor
import board

monitor = TemperatureMonitor(board.D5)
monitor.run()