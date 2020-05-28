from car import Car
class Truck(Car):
    def __init__(self,color, max_speed, acceleration,tyre_friction,max_cargo_weight):
        super().__init__(color, max_speed, acceleration,tyre_friction)
        self._max_cargo_weight=max_cargo_weight
        self._is_engine_started=False
        self._Total_load=0
    
    def start_engine(self):
        self._is_engine_started=True
    
    def stop_engine(self):
        self._is_engine_started=False
    @property
    def Total_load(self):
        return self._Total_load
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
    
    def load(self, load_weight):
        if load_weight>0:
            if (self._is_engine_started==False and self._current_speed==0) or (self._is_engine_started==True and self._current_speed==0):
                if self._Total_load+load_weight<=self._max_cargo_weight:
                    self._Total_load +=load_weight
                else:
                    print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
            else:
                print("Cannot load cargo during motion")
        else:
            raise ValueError("Invalid value for cargo_weight")
    
    def unload(self, load_weight):
        if load_weight>0:
            if (self._is_engine_started==False and self._current_speed==0)  or (self._is_engine_started==True and self._current_speed==0):
                if self._Total_load-load_weight>=0:
                    self._Total_load -=load_weight
                else:
                    self._Total_load=0
            else:
                print("Cannot unload cargo during motion")
        else:
            raise ValueError("Invalid value for cargo_weight")
    

            
    