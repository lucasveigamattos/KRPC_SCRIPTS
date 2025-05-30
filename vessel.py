from krpc import connect

#Is this class good enough?
class Vessel:
    def __init__(self, connection_name: str) -> None:
        self.connection = connect(connection_name)
        self.vessel = self.connection.space_center.active_vessel
        self.flight = self.vessel.flight()
        self.control = self.vessel.control
        self.auto_pilot = self.vessel.auto_pilot
        self.orbit = self.vessel.orbit
    
    def activate_sas(self) -> None:
        self.control.sas = True

    def activate_next_stage(self) -> None:
        self.control.activate_next_stage()
    
    def engage_auto_pilot(self) -> None:
        self.auto_pilot.engage()
    
    def disengage_auto_pilot(self) -> None:
        self.auto_pilot.disengage()
    
    def get_altitude(self) -> float:
        return self.flight.mean_altitude
    
    def get_altitude_above_surface(self) -> float:
        return self.flight.surface_altitude

    def get_apoapis_altitude(self) -> float:
        return self.orbit.apoapsis_altitude
    
    def get_resources_in_decouple_stage(self, stage: int):
        return self.vessel.resources_in_decouple_stage(stage)

    def set_flight_reference_frame(self, reference_frame) -> None:
        self.flight = self.vessel.flight(reference_frame)
    
    def set_throttle(self, throttle: float) -> None:
        self.control.throttle = throttle
    
    def set_heading(self, heading: float) -> None:
        self.auto_pilot.target_heading = heading
    
    def set_pitch(self, pitch: float) -> None:
        self.auto_pilot.target_pitch = pitch