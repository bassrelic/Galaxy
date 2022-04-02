"""This is the main file"""

from datetime import timedelta, date
import pygame
from galaxy.galaxy import Galaxy
from  game_logic.ui_handlers import DataslateHandler
import config

def main():
    """This is the main Function of this Game"""
    curr_date = date.fromisoformat('2022-01-01')
    time_delta_per_sec = timedelta(days=1)

    # pygame section
    pygame.init()
    config.myfont = pygame.freetype.SysFont('Arial', 20)
    config.screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Galaxy")
    active = True
    config.clock = pygame.time.Clock()

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
        astroids = sol.get_astroids()
        for astroid in astroids:
            print(astroid.get_name())
            print(astroid.get_size())

    all_sprites_list = pygame.sprite.Group()

    for sol in sols:
        planets = sol.get_planets()
        astroids = sol.get_astroids()
        for planet in planets:
            all_sprites_list.add(planet)
        for astroid in astroids:
            all_sprites_list.add(astroid)

    # events
    update_time = pygame.USEREVENT + 0
    pygame.time.set_timer(update_time, config.SECOND)

    # logic
    ds_h = DataslateHandler()

    while active:

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                ds_h.handle_dataslate(all_sprites_list)

            if event.type == pygame.QUIT:
                active = False
                print("Player quitted this game")

            elif event.type == pygame.KEYDOWN:
                # Quit game on escape
                if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                    active = False

            elif event.type == update_time:
                curr_date = curr_date + time_delta_per_sec

        # Logic here
        for sprite in all_sprites_list:
            sprite.step()

        all_sprites_list.update()

        # Clear screen
        config.screen.fill(config.BLACK)

        # Draw Objects
        config.myfont.render_to(config.screen, (450, 0), str(round(config.clock.get_fps(), 2)), config.WHITE)
        config.myfont.render_to(config.screen, (0, 0), str(curr_date), config.WHITE)
        all_sprites_list.draw(config.screen)

        # Update screen
        pygame.display.flip()

        # Refresh time
        config.clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
