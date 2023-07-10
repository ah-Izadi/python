class TagCloud:
    def __init__(self):
        self.dictionary = {}
    def add(self,inputKey):
        self.dictionary[inputKey.lower()] = self.dictionary.get(inputKey.lower(),0)+1

    def getItem(self,inputKey):
        print(self.dictionary.get(inputKey,0))
    def __iter__(self):
        return iter(self.dictionary)
    def __setitem__(self,key,value):
        self.dictionary[key] = value

p1 = TagCloud()
p1.add("SaLaM")
p1.add("SAlAM")
p1.add("SALAM")


p1.getItem("salam")
p1["salam"] = 120
p1.getItem("salam")
print(p1)