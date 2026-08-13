#simple class
class Dog :
    pass

d1 = Dog()
d2 = Dog()
print(type(d1))
print(d1==d2)
print(d1 is d2)
a=4
b=4
print(a==b)
print(a is b)




#on peux aouter des attribut a un objet mais ce nest pas la bonne methode de faire ca 
d1.name ="haw haw"
d1.age = 4

print(d1.name)

#avec la bonne methode de crier un constructeur 



#crier data set
class Dataset:
    def __init__(self,name:str ,num_samples:int)->None:
        self.name = name
        self.num_samples = num_samples
    
        
train_set = Dataset("imageNet/train",1_281_167)
test_set = Dataset("imageNet/test",50_000)

print(train_set.name,train_set.num_samples)
print(test_set.name,test_set.num_samples)



class Dataset2:
    def __init__(self,name:str ,num_samples:int)->None:
        self.name = name
        self.num_samples = num_samples
    def describe(self)->None:
        print(f"le name de dataset:{self.name} et le nombre de samples est:{self.num_samples}")
    def is_large(self,threshold:int=100_000)->bool:
        return self.num_samples > threshold






if __name__ == "__main__":
    dset = Dataset2("COCO",330_000)
    dset.describe()
    print(dset.is_large(500_000))