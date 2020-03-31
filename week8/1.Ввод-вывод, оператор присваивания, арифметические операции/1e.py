speed = int(input())
time = int(input())
mkad = 109
if speed > 0:
    coordinate = (speed * time - mkad) % mkad
else:
    speed = -speed
    coordinate = (mkad - speed * time) % mkad
print(coordinate)
