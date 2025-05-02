import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gravity_turn_angle import get_gravity_turn_angle

assert get_gravity_turn_angle(0) == 90, "Altitude below 1km should have a 90 degree angle in gravity turn."
assert get_gravity_turn_angle(0.1) == 90, "Altitude below 1km should have a 90 degree angle in gravity turn."
assert get_gravity_turn_angle(0.9) == 90, "Altitude below 1km should have a 90 degree angle in gravity turn."
assert get_gravity_turn_angle(1) == 90, "Start altitude, gravity turn angle should be 90."
assert get_gravity_turn_angle(15) == 45, "Middle atmosphere altitude, gravity turn angle should be 45."
assert get_gravity_turn_angle(70) == 0, "Start Vacuum altitude, gravity turn angle should be 0."