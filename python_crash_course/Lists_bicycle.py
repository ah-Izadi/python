bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

print(bicycles[0])

print(bicycles[0].title())

message = f'my first bicycle was a {bicycles[0].title()}'
print(message)

motorcycles = ['honda','yamaha','suzuki']
motorcycles[0] = 'ducati'
print(','.join(motorcycles))

motorcycles.append('honda')
print(motorcycles)

for x in motorcycles[2:]:
    print(x)