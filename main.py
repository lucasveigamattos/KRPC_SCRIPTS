import os

from orbital_flight import orbital_flight
from landing import landing

def orbital_flight_case() -> None:
    altitude = float(input("Apoapis altitude in meters: "))
    heading = float(input("Choose heading: "))

    os.system("cls")
    
    orbital_flight(altitude, heading)

print("Orbital flight (0).")
print("Landing (1).")
flight_mode = input("Choose flight mode: ")

os.system("cls")

match flight_mode:
    case "0":
        orbital_flight_case()
    case "1":
        landing()
    case _:
        print("Unknown flight mode, please, choose a valid option next time.")