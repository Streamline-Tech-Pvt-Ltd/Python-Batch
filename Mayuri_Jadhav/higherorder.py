#map for square in higher order function
# l1=[1,2,3,4,5,6]
# res=map(lambda a:a*a,l1)
# print(tuple(res))

#abstraction example in oop
class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
        var=self.name+" "+self.model
        print(var)
    class Engine:
        def __init__(self,engine_type):
            self.engine_type=engine_type
            print("Engine type:",self.engine_type)