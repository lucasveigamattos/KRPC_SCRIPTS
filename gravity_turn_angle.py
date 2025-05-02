import math
import constants

def get_gravity_turn_angle(altitude: float) -> float:
    if (altitude < constants.gravity_turn_start_altitude):
        return 90

    #How to make a smooth transition between those two functions?
    if (altitude <= constants.middle_atmosphere_altitude):
        return constants.up_target_pitch - abs(math.log(altitude, math.e) * constants.middle_target_pitch / math.log(constants.middle_atmosphere_altitude, math.e))
    else:
        return constants.up_target_pitch - abs(math.log(altitude, math.e) * constants.up_target_pitch / math.log(constants.vacuum_start_altitude, math.e))