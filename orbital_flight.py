from vessel import Vessel
from count_down import count_down
from gravity_turn_angle import get_gravity_turn_angle

import constants

def orbital_flight(desired_altitude: float, heading: float) -> None:
    vessel = Vessel("Orbital Flight Mode.")

    count_down()

    vessel.activate_next_stage()
    vessel.set_throttle(1)
    vessel.activate_next_stage()

    vessel.engage_auto_pilot()
    vessel.set_heading(heading)

    stage_separation_already_happened = False

    while vessel.get_apoapis_altitude() < desired_altitude:
        gravity_turn_angle = get_gravity_turn_angle(vessel.get_altitude() / constants.one_kilometer_in_meters)
        vessel.set_pitch(gravity_turn_angle)

        #TODO: try making stage separation better.
        #TODO: try making resource fetching better.
        if vessel.get_resources_in_decouple_stage(vessel.control.current_stage - 1).amount("LiquidFuel") == 0 and not stage_separation_already_happened:
            vessel.activate_next_stage()
            stage_separation_already_happened = True
    
    vessel.set_throttle(0)
    vessel.disengage_auto_pilot()
    vessel.activate_sas()