class Car:
    horn="Beep Beep"
    def __init__(self, color="red", max_speed=0, acceleration=0, tyre_friction=0):
        self._color=color
        if max_speed>0:
            self._max_speed=max_speed
        else:
            raise ValueError("Invalid value for max_speed")
        if acceleration>0:
            self._acceleration=acceleration
        else:
            raise ValueError("Invalid value for acceleration")
        if tyre_friction>0:
            self._tyre_friction=tyre_friction
        else:
            raise ValueError("Invalid value for tyre_friction")
        self._is_engine_started=False
        self._current_speed=0
    #@property
    def start_engine(self):
        self._is_engine_started=True
    #@property
    def stop_engine(self):
        self._is_engine_started=False
       # self._current_speed=0
    
    def accelerate(self):
        if self._is_engine_started==True:
            self._current_speed +=self._acceleration
            if self._current_speed>self._max_speed:
                self._current_speed=self._max_speed
        elif self._is_engine_started==False:
            print("Start the engine to accelerate")
            #return "Start the engine"
            
    @property
    def is_engine_started(self):
        return self._is_engine_started
    @property
    def color(self):
        return self._color
    @property
    def max_speed(self):
        return self._max_speed
    @property
    def acceleration(self):
        return self._acceleration
    @property
    def tyre_friction(self):
        return self._tyre_friction
    @property
    def current_speed(self):
        return self._current_speed
    
    #@property
    def apply_brakes(self):
        #if self._current_speed>=self._tyre_friction:
        self._current_speed -=self._tyre_friction
        if self._current_speed<0:
         #   raise ValueError("Invalid value for tyre_friction")
            self._current_speed=0 
    #@property
    def sound_horn(self):
        if self._is_engine_started==True:
            print(self.horn)
            #return "Beep Beep"
        else:
            print("Start the engine to sound_horn")
            #return "Start the engine to sound_horn"
    
    
    