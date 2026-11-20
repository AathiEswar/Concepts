class Animals:
    def __init__(self,name):
        self.name = name


    def sayhi(self):
        print("hello",self.name)

animal = Animals("laber")

animal.sayhi()