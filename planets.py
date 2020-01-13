planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")

rocky_planets = planet_list[:4]

del planet_list[-1]

# Example spacecraft list
spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
]

for planet in planet_list:
    visited = False
    
    for ship in spacecraft:
        if ship[1] == planet:
            visited = True
            craft = ship[0]
        
    if visited:
        print(f'{planet} has been visited by {craft}')
    else:
        print(f'{planet} has not been visited by any spacecraft.')