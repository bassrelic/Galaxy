"""This is the main file"""

from galaxy.galaxy import Galaxy

galaxy = Galaxy("Milkyway")
sols = galaxy.get_sols()
print(sols)

for sol in sols:
    print(sol.get_name())
    planets = sol.get_planets()
    for planet in planets:
        print(planet.get_name())
        for civilization in planet.get_civilizations():
            print(civilization.get_name())
            print(civilization.get_count())
            for belief in civilization.get_beliefs():
                print(belief.get_name())
