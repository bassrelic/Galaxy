"""This is the main file"""

import pygame
from galaxy.galaxy import Galaxy
from datetime import timedelta, date

WHITE = ( 255, 255, 255)
BLACK = ( 0, 0, 0)
SECOND = 1000

def main():
    """This is the main Function of this Game"""
    # testing stuff
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

    date = date.fromisoformat('2022-01-01')
    timeDeltaPerSec = timedelta(days=1)

    # pygame section
    pygame.init()
    myfont = pygame.freetype.SysFont('Arial', 20)
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Galaxy")
    active = True
    clock = pygame.time.Clock()

    # events
    update_time = pygame.USEREVENT + 0
    pygame.time.set_timer(update_time, SECOND)

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                print("Player quitted this game")

            elif event.type == pygame.KEYDOWN:
                # Quit game on escape
                if event.key == pygame.K_ESCAPE:
                    active = False

            elif event.type == update_time:
                date = date + timeDeltaPerSec

        # Logic here

        # Clear screen
        screen.fill(BLACK)

        # Draw Objects
        myfont.render_to(screen, (450, 0), str(round(clock.get_fps(), 2)), WHITE)
        myfont.render_to(screen, (0, 0), str(year), WHITE)

        # Update screen
        pygame.display.flip()

        # Refresh time
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
