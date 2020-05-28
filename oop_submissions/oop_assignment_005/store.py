class Item():
    def __init__(self, name, price, category):
        self._name=name
        self._category=category
        if price<=0:
            raise ValueError("Invalid value for price, got {}".format(price))
        else:
            self._price=price
            
    def __str__(self):
        return f'{self._name}@{self._price}-{self._category}'
        
    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
        
    @property
    def price(self):
        return self._price
        
class Query():
    def __init__(self, field, operation, value):
        k=["EQ", "IN", "GT", "GTE", "LT", "LTE", "STARTS_WITH", "ENDS_WITH", "CONTAINS"]
        self._field=field
        self._operation=operation
        self._value=value
        
        if self._operation not in k:
            raise ValueError("Invalid value for operation, got random")
        
    def __str__(self):
        return f'{self.field} {self.operation} {self.value}'
        
    @property
    def field(self):
        return self._field
    
    @property
    def operation(self):
        return self._operation
    
    @property
    def value(self):
        return self._value

class Store():
    def __init__(self):
        self.items_list = []
        self.items_none_str = []
    
    def add_item(self, item):
        self.items_none_str.append(item)
        item=str(item)
        self.items_list.append(item)

#filter
    def filter(self, query):
        obj=Store()
        if query.operation == "IN":
            for i in self.items_none_str:
                if  i.category in query.value or i.name in query.value or i.price in query.value:
                    obj.add_item(i)

        elif query.operation == "EQ":
            for i in self.items_none_str:
                if i.name == query.value or i.category == query.value or i.price == query.value:
                    obj.add_item(i)
        
        elif query.operation == "GT":
            for i in self.items_none_str:
                if i.price > query.value:
                    obj.add_item(i)
        
        elif query.operation == "GTE":
            for i in self.items_none_str:
                if i.price >= query.value:
                    obj.add_item(i)
                    
        elif query.operation == "LT":
            for i in self.items_none_str:
                if i.price < query.value:
                    obj.add_item(i)
        
        elif query.operation == "LTE":
            for i in self.items_none_str:
                if i.price <= query.value:
                    obj.add_item(i)
        
        elif query.operation == "STARTS_WITH":
            for i in self.items_none_str:
                if i.name.startswith(query.value) or i.category.startswith(query.value):
                    obj.add_item(i)

        elif query.operation == "ENDS_WITH":
            for i in self.items_none_str:
                if i.name.endswith(query.value) or i.category.endswith(query.value):
                    obj.add_item(i)
        
        elif query.operation == "CONTAINS":
            for i in self.items_none_str:
                if (query.field == "name" and query.value in i.name) or (query.field == "category" and query.value in i.category):
                    obj.add_item(i)
                    
        return obj                
                    
# Exclude
    def exclude(self, query):
        result=Store()
        x=self.filter(query)
        for i in self.items_list:
            if i not in x.items_list:
                result.add_item(str(i))
        return result
    
    def count(self):
        return len(self.items_list)

            
    def __str__(self):
        if len(self.items_list)>0:
            return "\n".join(self.items_list)
        else:
            return "No items"
            
            
            
            
store = Store()  
item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item)  
item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item)  
item = Item(name="Butter", price=10, category="Grocery")  
store.add_item(item)  
query = Query(field="category", operation="IN", value=["Food"])  
print(query.operation)
results = store.filter(query)  
print(results)  