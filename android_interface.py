import subprocess
import os

from tap_cordinates import Coordinates

def get_adb_path():
    return os.path.join(os.path.dirname(__file__), "tools", "adb", "adb")

class and_int:
    # Function to capture screenshot from the Android device
    def capture_screenshot(self):
        adb = get_adb_path()
        # Capture screenshot on the device and save it to /sdcard/screenshot.png
        subprocess.run([adb, "shell", "screencap", "-p", "/sdcard/screenshot.png"])
        
        # Pull the screenshot from the device to the computer
        subprocess.run([adb, "pull", "/sdcard/screenshot.png", "C:/Users/maxth/FGO_automate/FGO_AUTO"])
        print("took a screen shot")

    # Function to simulate tapping on the device screen
    def tap(self, coords):
        adb = get_adb_path()
        if coords:
            x, y = coords
            subprocess.run([adb, "shell", "input", "tap", str(x), str(y)])
            print(f"Tapping on ({x}, {y})")