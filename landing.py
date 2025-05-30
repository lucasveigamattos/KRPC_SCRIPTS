import time
import math
from vessel import Vessel

def landing(center_mass_height) -> None:
    vessel = Vessel("Landing.")
    vessel.set_flight_reference_frame(vessel.orbit.body.reference_frame)

    acceleration = vessel.orbit.body.surface_gravity

    vessel.activate_sas()

    time.sleep(0.1)

    vessel.control.sas_mode = vessel.connection.space_center.SASMode.retrograde

    altitude = vessel.get_altitude_above_surface()
    landing_started = False

    while altitude > center_mass_height:
        altitude = vessel.get_altitude_above_surface()
        
        if vessel.orbit.body.has_atmosphere:
            landing_started = landing_burn_body_with_atmosphere(center_mass_height, acceleration, landing_started, vessel)
        else:
            landing_started = landing_burn_body_without_atmosphere(center_mass_height, acceleration, landing_started, vessel)
    
    vessel.set_throttle(0)

def landing_burn_body_with_atmosphere(center_mass_height, acceleration, landing_started, vessel):
    altitude = vessel.get_altitude_above_surface()

    velocity = vessel.flight.vertical_speed
    mass = vessel.vessel.mass
    weight_force = mass * acceleration

    desired_acceleration = (4 - math.pow(velocity, 2)) / (2 * (altitude - center_mass_height)) # 4, 2: Número mágico no cógio hehe: remover depois.
    resulting_force = mass * desired_acceleration

    engines_force = weight_force - resulting_force

    desired_throttle = abs(engines_force) / vessel.vessel.max_thrust

    if (desired_throttle > 0.4 or landing_started): # 0.8: Número mágico no cógio hehe: remover depois.
        landing_started = True
        vessel.set_throttle(desired_throttle)

    if (altitude <= 350): # 350: Número mágico no cógio hehe: remover depois.
        vessel.control.gear = True
        vessel.control.sas_mode = vessel.connection.space_center.SASMode.radial
    
    return landing_started

def landing_burn_body_without_atmosphere(center_mass_height, acceleration, landing_started, vessel):
    altitude = vessel.get_altitude_above_surface()

    horizontal_velocity = vessel.flight.horizontal_speed
    vertical_velocity = vessel.flight.vertical_speed

    mass = vessel.vessel.mass
    weight_force = mass * acceleration

    desired_vertical_acceleration = (4 - math.pow(vertical_velocity, 2)) / (2 * (altitude - center_mass_height))
    resulting_vertical_force = mass * desired_vertical_acceleration

    desired_horizontal_acceleration = (0 - math.pow(horizontal_velocity, 2)) / (2 * (altitude - 500)) # 0, 2, 500: Número mágico no cógio hehe: remover depois.
    resulting_horizontal_force = mass * desired_horizontal_acceleration

    composed_resulting_force = math.sqrt(math.pow(resulting_vertical_force, 2) + math.pow(resulting_horizontal_force, 2))
    engines_force = weight_force - composed_resulting_force

    desired_throttle = abs(engines_force) / vessel.vessel.max_thrust

    if (desired_throttle > 0.8 or landing_started): # 0.8: Número mágico no cógio hehe: remover depois.
        landing_started = True
        vessel.set_throttle(desired_throttle)

    if (altitude <= 350): # 350: Número mágico no cógio hehe: remover depois.
        vessel.control.gear = True
        vessel.control.sas_mode = vessel.connection.space_center.SASMode.radial
    
    return landing_started