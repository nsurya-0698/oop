from car import Car
import math
class RaceCar(Car):
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self._nitro=0

    
    def accelerate(self):
        if self._is_engine_started==True:
            if self._nitro>0:
                self._current_speed += (self._acceleration+math.ceil((self._acceleration*30)/100))
                self._nitro -=10
            else:
                self._current_speed +=self._acceleration
            if self._current_speed>self._max_speed:
                self._current_speed=self._max_speed
        elif self._is_engine_started==False:
            print("Start the engine to accelerate")
            #return "Start the engine"
    @property
    def nitro(self):
        return self._nitro
    

    def apply_brakes(self):
        if self._current_speed>=(self._max_speed//2):
            self._nitro +=10
       # self._current_speed -=self._tyre_friction
        #if self._current_speed<0:
         #   self._current_speed=0 
        super().apply_brakes()
    
    
    