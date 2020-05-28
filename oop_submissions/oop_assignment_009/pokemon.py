#Task-1
#inhertible classes
'''class Pokemon:
    sound=""
    magnitude=0
    Attack_by=""
    Pokemon_name=""
    def __init__(self, name, level=1):
        if name == "":
            raise ValueError("name cannot be empty")
        else:
            self._name=name
        
        if level<=0:
            raise ValueError("level should be > 0")
        else:
            self._level=level
        self._master=None
 #proptected attributes  
    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return self._level
#methods
    @property
    def master(self):
        if self._master==None:
              print("No Master")
        else:
            return self._master
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    def attack(self):
        print("{} attack with {} damage".format(self.Attack_by,self._level*self.magnitude))
    
    def __str__(self):
        return "{} - Level {}".format(self._name, self._level)
        
        
        
#Actions
class fly:
    flying=""
    @classmethod
    def fly(cls):
        print(cls.flying)

class run:
    runing=""
    @classmethod
    def run(cls):
        print(cls.runing)

class swim:
    swimming=""
    @classmethod
    def swim(cls):
        print(cls.swimming)



#pokenons
class Pikachu(Pokemon, run, fly):
    runing="Pikachu running"
    flying="Pikachu Flying"
    sound="Pika Pika"
    magnitude=10
    Pokemon_name="Pikachu"
    Attack_by="Electric"

class Squirtle(Pokemon, run, swim, fly):
    sound="Squirtle...Squirtle"
    flying="Squirtle Flying"
    magnitude=9
    Pokemon_name="Squirtle"
    Attack_by="Water"

class Pidgey(Pokemon, fly):
    sound="Pidgey...Pidgey"
    flying="Pidgey flying..."
    magnitude=5
    Pokemon_name="Pidgey"
    Attack_by="Air"
 
class Swanna(Pokemon, fly):
    sound="Swanna...Swanna"
    magnitude=9
    Pokemon_name="Swanna"
    Attack_by="Water"
    flying="Swanna flying..."
    def attack(self):
        super().attack()
        print("Air attack with {} damage".format(self.level*5))
  
class Zapdos(Pokemon, fly, swim):
    sound="Zap...Zap"
    magnitude=10
    Pokemon_name="Zapdos"
    flying="Zapdos flying..."
    Attack_by="Electric"
    def attack(self):
        super().attack()
        print("Air attack with {} damage".format(self.level*5))
    def fly(self):
        print("{} flying...".format(self.Pokemon_name))

#Task-2
class Island:
    island_list=[]
    def __init__(self, name, max_no_of_pokemon, total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        self.island_list.append(self)
    
    @property
    def name(self):
        return self._name
    
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    @classmethod
    def get_all_islands(cls):
        return cls.island_list
        
        
    def add_pokemon(self, pokemon_obj):
        if  self._pokemon_left_to_catch+1 > self._max_no_of_pokemon:
            print("Island at its max pokemon capacity")
        else:
            self._pokemon_left_to_catch +=1
            
            
            
    def __str__(self):
        return "{} - {} pokemon - {} food".format(self._name, self._pokemon_left_to_catch, self._total_food_available_in_kgs)

#Task-3
class Trainer(Island, Pokemon):
    def __init__(self, name):
         self._name=name
         self._experience=100
         self._max_food_in_bag=10*self._experience
         self._food_in_bag=0
         self._current_island=None
         self.pokemon_list=[]
    @property
    def name(self):
        return self._name
    
    @property
    def experience(self):
        return self._experience
    
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    
    @property
    def food_in_bag(self):
        return self._food_in_bag
    
    def move_to_island(self, island):
        self._current_island=island
            
    @property
    def current_island(self):
        if self._current_island == None:
            print("You are not on any island")
        else:
            return self._current_island    
    
    def total_food_available_in_kgs(self):
        return self.current_island._total_food_available_in_kgs
    
    def collect_food(self):
        if self._current_island == None:
            print("Move to an island to collect food")
        elif self._current_island._total_food_available_in_kgs < self._max_food_in_bag:
            self._food_in_bag = self._current_island._total_food_available_in_kgs
            self._current_island._total_food_available_in_kgs = 0
            
        elif self._food_in_bag < self._max_food_in_bag:
            self._food_in_bag = self._max_food_in_bag
            self.current_island._total_food_available_in_kgs  -=self._food_in_bag
    
    def catch(self, pokemon_obj):
        if self._experience >= 100*pokemon_obj._level:
            self._experience +=pokemon_obj._level*20
            print("You caught {}".format(pokemon_obj._name))
            self.pokemon_list.append(pokemon_obj)
            pokemon_obj._master=self
        else:
            print("You need more experience to catch {}".format(pokemon_obj.name))
    def get_my_pokemon(self):
        return self.pokemon_list
    
        
    def __str__(self):
        return self._name'''
        
'''my_pikachu1 = Pikachu(name="Ryan", level=1)
my_pikachu2 = Pikachu(name="surya", level=2)
my_Squirtle1 = Squirtle(name="surya", level=2)
my_Squirtle1 = Squirtle(name="surya", level=2)
print(my_pikachu1.name)
my_pikachu1.run()
my_pikachu1.fly()
my_pikachu1.run()
my_Squirtle1.fly()
my_Squirtle1.run()

my_pikachu = Pikachu(name="Ryan", level=1)
my_pikachu1 = Pikachu(name="su", level=1)
my_pikachu.run()
my_pikachu1.run()
my_pikachu1.fly()
my_pikachu.fly()'''

class Todo:
    def __init__(self, task):
        '''self.discription=discription'''
        self.is_completed = False
        self.content=task
    def project(self):
       self.is_completed=True
       print('{} task completed'.format(self.content))
       
class Task_due_date(Todo):
    def __init__(self, task, time=0):
        self.is_completed = False
        self.content=task
        self.time=time
    
       

if __name__=="__main__":
    con=input()
    time=input()   

obj=Todo(con)        
obj1= Task_due_date(con,time);
obj.project()
print(obj1.time)

















































''' super().__init__(task)
        self.is_completed=false
        self.content=task'''