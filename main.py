import os
import math
import krpc

from orbital_flight import orbital_flight

def landing():
    connection = krpc.connect(name = "Landing.")
    vessel = connection.space_center.active_vessel

    acceleration = vessel.orbit.body.surface_gravity

    vessel.control.sas = True
    vessel.control.sas_mode = connection.space_center.SASMode.retrograde

    while True:
        altitude = vessel.flight(vessel.orbit.body.reference_frame).surface_altitude

        if (altitude <= 4000):
            velocity = vessel.flight(vessel.orbit.body.reference_frame).vertical_speed
            mass = vessel.mass
            weight_force = mass * acceleration

            desired_acceleration = (4 - math.pow(velocity, 2)) / (2 * (altitude - 3))
            resulting_force = mass * desired_acceleration

            engines_force = weight_force - resulting_force
            desired_throttle = engines_force / vessel.max_thrust

            vessel.control.throttle = desired_throttle

            if (altitude <= 350):
                vessel.control.gear = True
                #vessel.control.sas_mode = connection.space_center.SASMode.radial
            
            if (altitude <= 3):
                vessel.control.throttle = 0
                print(f"touch down speed: {velocity}")
                print("landing sequence finished.")
                break

print("Orbital flight (0).")
print("Landing (1).")
flight_mode = input("Choose flight mode: ")

os.system("cls")

match flight_mode:
    case "0":
        altitude = float(input("Apoapis altitude in meters: "))
        heading = float(input("Choose heading: "))

        os.system("cls")
        
        orbital_flight(altitude, heading)
    case "1":
        landing()
    case _:
        print("Unknown flight mode, please, choose a valid option next time.")