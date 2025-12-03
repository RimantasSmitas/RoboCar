"""AILights.py

Controls 8 LEDs on a Raspberry Pi.

Behavior:
- All LEDs are ON by default.
- Repeatedly choose 5 unique LEDs at random and turn them OFF.
- Each chosen LED stays off for a random duration between 1 and 5 seconds,
  then it is turned back ON (durations are independent per LED).
- Runs in a background thread so other code can execute concurrently.

If running on a non-Raspberry Pi system this script falls back to a
simulated GPIO implementation that logs state changes to the console.
"""
import RPi.GPIO as GPIO
from time import sleep
import time
import random
import threading
import sys

try:
	import RPi.GPIO as GPIO
	REAL_GPIO = True
except Exception:
	REAL_GPIO = False

#if not REAL_GPIO:
	# Minimal fake GPIO for development/testing on non-Pi machines
#	class FakeGPIO:
#		BCM = 'BCM'
#		HIGH = 1
#		LOW = 0

#		def __init__(self):
#			self._state = {}

#		def setmode(self, mode):
#			print(f"[FakeGPIO] setmode({mode})")

#		def setup(self, pin, mode, initial=None):
#			self._state[pin] = initial if initial is not None else self.HIGH
#			print(f"[FakeGPIO] setup(pin={pin}, mode={mode}, initial={self._state[pin]})")

#		def output(self, pin, val):
#			self._state[pin] = val
##			label = 'ON' if val == self.HIGH else 'OFF'
#			print(f"[FakeGPIO] pin {pin} -> {label}")

#		def cleanup(self):
#			print("[FakeGPIO] cleanup()")

#	GPIO = FakeGPIO()


# --- Configuration ---
# Adjust these GPIO pin numbers for your wiring. Using BCM numbering by default.
PINS = [17, 27, 22, 23, 24, 25, 5, 6]
ALL_ON = True  # initial default: LEDs ON

# Global control flag for background thread
_running = False
_thread = None
_lock = threading.Lock()


def setup_gpio():
	GPIO.setmode(GPIO.BCM)
	for pin in PINS:
		initial = GPIO.HIGH if ALL_ON else GPIO.LOW
		GPIO.setup(pin, GPIO.OUT, initial=initial)


def turn_on(pin):
	GPIO.output(pin, GPIO.HIGH)


def turn_off(pin):
	GPIO.output(pin, GPIO.LOW)


def schedule_turn_on(pin, delay):
	def worker():
		time.sleep(delay)
		turn_on(pin)
	t = threading.Thread(target=worker)
	t.daemon = True
	t.start()


def main_loop():
	print("Starting AILights main loop. Press Ctrl+C to stop.")
	# Ensure all LEDs are ON initially
	for pin in PINS:
		turn_on(pin)

	try:
		while _running:
			# pick 5 unique indices from the 8 LEDs
			indices = random.sample(range(len(PINS)), 5)
			for i in indices:
				pin = PINS[i]
				# turn the LED off
				turn_off(pin)
				# schedule it to turn back on after a random time 1..5 seconds
				duration = random.uniform(1.0, 5.0)
				schedule_turn_on(pin, duration)
			# small pause before next selection to avoid busy looping
			time.sleep(0.5)

	except Exception as e:
		print(f'Error in AILights main loop: {e}')
	finally:
		GPIO.cleanup()


def start():
	"""Start the AILights background thread."""
	global _running, _thread
	with _lock:
		if _running:
			print('AILights is already running.')
			return
		_running = True
		print('AILights starting. Raspberry Pi GPIO available:', REAL_GPIO)
		if not REAL_GPIO:
			print('Running in simulated mode (no RPi.GPIO).')
		setup_gpio()
		_thread = threading.Thread(target=main_loop, daemon=False)
		_thread.start()
		print('AILights background thread started.')


def stop():
	"""Stop the AILights background thread."""
	global _running, _thread
	with _lock:
		if not _running:
			print('AILights is not running.')
			return
		_running = False
	if _thread:
		_thread.join(timeout=5.0)
		print('AILights stopped.')


if __name__ == '__main__':
	try:
		start()
		# Keep the main thread alive
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		print('\nReceived KeyboardInterrupt — stopping AILights.')
		stop()

