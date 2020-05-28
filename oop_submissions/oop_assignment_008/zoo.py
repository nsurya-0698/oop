class animals:
    sound=""
    increased_food_in_kgs=""
    inhales=""
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
    def age_in_months(self):
        return self._age_in_months
    
    @property
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    
    @classmethod
    def breathe(cls):
        print(cls.inhales)
    
    def grow(self):
        self._age_in_months +=1
        self._required_food_in_kgs +=self.increased_food_in_kgs

class Hunting:
    no_animals=""
    dish=""
    def hunt(self, animal_obj):
        dish_count=0
        for i in animal_obj.animals_list:
            if self.dish in str(type(i)):
                dish_count +=1

        if dish_count == 0:
            print("No {} to hunt".format(self.no_animals))
        else:
            for i in animal_obj.animals_list:
                if self.dish in str(type(i)):
                    animal_obj.animals_list.remove(i)
                    break
        
    
        
class Deer(animals):
    sound="Buck Buck"
    increased_food_in_kgs=2
    inhales="Breathe in air"

class Lion(animals, Hunting):
    sound="Roar Roar"
    increased_food_in_kgs=4
    inhales="Breathe in air"
    no_animals="deers"
    dish="Deer"

class Shark(animals,Hunting):
    sound="Shark Sound"
    increased_food_in_kgs=8
    inhales="Breathe oxygen from water"
    no_animals="GoldFish"
    dish="GoldFish"

class GoldFish(animals):
    sound="Hum Hum"
    increased_food_in_kgs=0.2
    inhales="Breathe oxygen from water"

class Snake(animals, Hunting):
    sound="Hiss Hiss"
    increased_food_in_kgs=0.5
    inhales="Breathe in air"
    no_animals="deers"
    dish="Deer"


class Zoo(animals):
    count=0
    def __init__(self):
        self._reserved_food_in_kgs=0
        self.animals_list=[]
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    def add_food_to_reserve(self, food_weight):
        self._reserved_food_in_kgs +=food_weight
    
    def add_animal(self, animal_name):
        self.animals_list.append(animal_name)
        Zoo.count +=1
    
    def count_animals(self):
        return int(len(self.animals_list))
        
    def feed(self, animal_obj):
        if self._reserved_food_in_kgs>0:
            self._reserved_food_in_kgs -=animal_obj._required_food_in_kgs
            animal_obj.grow()
  
    @classmethod
    def count_animals_in_all_zoos(cls):
        return (cls.count)
    
    @staticmethod
    def count_animals_in_given_zoos(list_obj=[]):
        c=0
        for i in list_obj:
            #k=i.count_animals()
            #print(k)
            c +=i.count_animals()
        return c
        
        
        



zoo=Zoo()
nehru_zoological_park = Zoo()

lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
nehru_zoological_park.add_animal(deer)
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=5)
nehru_zoological_park.add_animal(deer)
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
nehru_zoological_park.add_animal(deer)

nehru_zoological_park.add_animal(lion)


zoo.add_animal(lion)
zoo.add_animal(deer)

#print(nehru_zoological_park.count_animals())
#print(Zoo.count_animals_in_all_zoos())

#print(Zoo.count_animals_in_given_zoos([nehru_zoological_park]))
lion.hunt(nehru_zoological_park)
print(nehru_zoological_park.count_animals())
