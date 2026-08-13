#This is a classic gotcha: m1.framework = "tensorflow" does NOT modify
#the shared class attribute. It creates a brand-new instance attribute
#on m1 that happens to have the same name and now hides the class one
#whenever you look it up through m1.

#create CLass
class Model:
    #class attribute
    framework = "pytorch"
    def __init__(self,name :str)->None: 
        self.name=name #object attribute

        
    def printing(self)->None:
        print(f"the name of the model is {self.name} ")
        
m1 = Model("resnet")
m2 = Model("bert")



print(m1.framework)
print(m2.framework)

#changing framework via class 
Model.framework = "jax"

print(m1.framework)
print(m2.framework)

#a new object attribute has been created (has priority )
m1.framework = "tensorflow"

print(m1.framework)
print(m2.framework)






#Regerstry class
class BuggyRegistry:
    #class attribute
    items :list[str] = []
    def add(self,item:str)->None:
        self.items.append(item)


a = BuggyRegistry()
b = BuggyRegistry()
a.add("modelA")
b.add("modelB")
print(a.items)

#iterable  ne crier pas une nouvelle variable (append)
# and no iterable


#crier une nouvelle class fixedRegistry object attribute (items)method called Add qui affecter une valeur dans items 

class fixedRegistry:
    #object attribute
    def __init__(self)->None:
        self.items:list[str] = []
    
    def add(self,item:str)->None:
        self.items.append(item)
        
a = fixedRegistry()
b = fixedRegistry()
a.add("modelA")
b.add("modelB")
print(a.items)