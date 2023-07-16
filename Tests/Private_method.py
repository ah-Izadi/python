class dsas:
    @staticmethod
    def public():
        print("salam public")
    @staticmethod
    def __private():
        print("salam private")

dsas.public()
p1 = dsas()
print(p1._dsas__string)