class Deer:
    sound="Buck Buck"
    lives_in="Breathe in air"
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        self.breed=breed
        if required_food_in_kgs>0:
            self.required_food_in_kgs=required_food_in_kgs
        else:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        if age_in_months == 1:
            self.age_in_months=age_in_months
        else:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
    
    """@property
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    @property
    def age_in_months(self):
        return self._age_in_months"""
    
    
        
    def grow(self):
        self.age_in_months +=1
        self.required_food_in_kgs +=2
        
    def make_sound(self):
        print(self.sound)
    
    def breathe(self):
        print(self.lives_in)
@def foo():
    doc = "The foo property."
    def fget(self):
        return self._foo
    def fset(self, value):
        self._foo = value 
class Lion(Deer):
    sound="Roar Roar"
    def grow(self):
        self.age_in_months +=1
        self.required_food_in_kgs +=4
        

class Shark(Deer):
    sound="Shark Sound"
    lives_in="Breathe oxygen from water"
    def grow(self):
        self.age_in_months +=1
        self.required_food_in_kgs +=8
        
class GoldFish(Deer):
    sound="Hum Hum"
    #lives_in="Breathe oxygen from water"
    def grow(self):
        self.age_in_months +=1
        self.required_food_in_kgs +=0.2
        
class Snake(Deer):
    sound="Hiss Hiss"
    def grow(self):
        self.age_in_months +=1
        self.required_food_in_kgs +=0.5

class Zoo(Deer):
    animals_count=0
    def __init__(self):
        self.reserved_food_in_kgs=0
    
    def add_food_to_reserve(self, weight):
        self.reserved_food_in_kgs +=weight
    
    def add_animal(self, animal_name):
        self.animals_count +=1
    
    def count_animals(self):
       return self.animals_count
    
    def feed(self, name):
        self.reserved_food_in_kgs -=name.required_food_in_kgs
        name.grow()
      
 

nehru_zoological_park = Zoo()
surya_park = Zoo()
nehru_zoological_park.add_food_to_reserve(10000000)
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
nehru_zoological_park.add_animal(lion)
nehru_zoological_park.add_animal(gold_fish)
surya_park.add_animal(gold_fish)
print(nehru_zoological_park.count_animals())
print(surya_park.count_animals())