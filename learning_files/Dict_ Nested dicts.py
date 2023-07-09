Sport_cars = {
    "Ford" : {
        "model" : "Mustang",
        "year" : "2023"
    },
    
    "lamborghini" : {
        "model" : "aventador",
        "year" : "2018"
    },
    
    "mclaren" : {
        "model" : "p1 GTR-18",
        "year" : "2018"
    }
}

print(Sport_cars)
print("\n")
print(Sport_cars["Ford"]["model"])

#or
print("\n")

Ford = {
    "model" : "Mustang",
    "year" : "2023"
}

lamborghini = {
    "model" : "aventador",
    "year" : "2018"
}

mclaren = {
    "model" : "p1 GTR-18",
    "year" : "2018"
}

Sport_Cars = {
    "Ford" : Ford,
    "lamborghini" : lamborghini,
    "mclaren" : mclaren
}

print(Sport_Cars)
print("\n")
print(Sport_Cars["mclaren"]["year"])