class TagCloud:

    def __init__(self):
        self.__dictionary = {}

    def add(self,inputKey):
        self.__dictionary[inputKey.lower()] = self.__dictionary.get(inputKey.lower(),0)+1


    def getItem(self,inputKey):
        print(self.__dictionary.get(inputKey,0))

    def __iter__(self):
        return iter(self.__dictionary)

    def __setitem__(self,key,value):
        self.__dictionary[key] = value


p1 = TagCloud()

p1.add("SaLaM")

p1.add("SAlAM")

p1.add("SALAM")
print(p1._TagCloud__dictionary)


p1.getItem("salam")

p1["salam"] = 120

p1.getItem("salam")
print(p1)