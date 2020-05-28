class Deer:
    sound="Buck Buck"
    lives_in="Breathe in air"
    food_countity=2
    #deer_count=0
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        self._breed=breed
        if required_food_in_kgs>0:
            self._required_food_in_kgs=required_food_in_kgs
        else:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        if age_in_months == 1:
            self._age_in_months=age_in_months
        else:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
    
    @property
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    @property
    def age_in_months(self):
        return self._age_in_months
    
    
    '''def d_count(self):
        self.deer_count -=1'''
        

    def grow(self):
        self._age_in_months +=1
        self._required_food_in_kgs +=self.food_countity
     
    def make_sound(self):
        print(self.sound)
    
    def breathe(self):
        print(self.lives_in)
        
    

class Lion(Deer):
    sound="Roar Roar"
    food_countity=4
    
    @classmethod
    def hunt(cls, class_name):
        return class_name.deer_count
        

class Shark(Deer):
    sound="Shark Sound"
    lives_in="Breathe oxygen from water"
    food_countity=8
    
    
class GoldFish(Deer):
    sound="Hum Hum"
    lives_in="Breathe oxygen from water"
    food_countity=0.2
    
    
class Snake(Deer):
    sound="Hiss Hiss"
    food_countity=0.5
    
class Zoo(Deer):
    animals_count=0
    #zoo_list_o_animals=[]
    deer_count=0
    zoo_list_of_animals_classAtt=[]
    def __init__(self):
        self._reserved_food_in_kgs=0
        self.zoo_list_of_animals=[]
    
    def add_food_to_reserve(self, weight):
        self._reserved_food_in_kgs +=weight
    
    def add_animal(self, animal_name):
        self.animals_count +=1
        self.zoo_list_of_animals.append(animal_name)
        self.zoo_list_of_animals_classAtt.append(animal_name)
    
    def count_animals(self):
        return len(self.zoo_list_of_animals)
       
    @classmethod
    def count_animals_in_given_zoos(cls, class_name):
       return len(class_name.zoo_list_of_animals)
     
    @staticmethod
    def count_animals_in_all_zoos():
        return len(Zoo.zoo_list_of_animals_classAtt)
       
    @staticmethod
    def a_count_de(self):
        self.animals_count -=1
    
    def feed(self, name):
        if self._reserved_food_in_kgs>0:
            self._reserved_food_in_kgs -=name.required_food_in_kgs
            name.grow()
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
      
 
#zoo=Zoo()
nehru_zoological_park = Zoo()
surya_park=Zoo()
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
nehru_zoological_park.add_animal(lion)
nehru_zoological_park.add_animal(gold_fish)
nehru_zoological_park.add_animal(deer)
nehru_zoological_park.add_animal(deer)
surya_park.add_animal(deer)
surya_park.add_animal(lion)
surya_park.add_animal(gold_fish)
#print(Zoo.count_animals_in_given_zoos(surya_park))
#print(Zoo.count_animals_in_given_zoos(nehru_zoological_park))
#print(surya_park.count_animals())
print(lion.hunt(nehru_zoological_park))
print(surya_park.count_animals())
print(nehru_zoological_park.count_animals())
#print(zoo.count_animals())
print(Zoo.count_animals_in_all_zoos())
print(Zoo.count_animals_in_given_zoos([nehru_zoological_park]))
