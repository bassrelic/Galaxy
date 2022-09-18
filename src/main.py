"""This is the main file"""
from datetime import timedelta, date
import pygame
from civilization.civilization_spawner import force_spawn_civilization
from galaxy.galaxy import Galaxy
from object.console import Console
from  game_logic.ui_handlers import DataslateHandler
import config

if __name__ == '__main__':
    curr_date = date.fromisoformat('2022-01-01')
    time_delta_per_sec = timedelta(days=1)
    # pylint:disable-next=invalid-name
    clock = None

    # pygame section
    pygame.init()
    config.FONT = pygame.freetype.SysFont('Arial', 20)
    config.screen = pygame.display.set_mode()
    pygame.display.set_caption("Galaxy")

    icon = pygame.image.load(config.ICONPATH).convert_alpha()
    pygame.display.set_icon(icon)

    window_size = pygame.display.get_window_size()

    # pylint:disable-next=invalid-name
    active = True

    # pylint:disable-next=invalid-name
    pause = False
    config.clock = pygame.time.Clock()

    consoleActive = False
    console = Console("Console", 0, int(window_size[1]-300))

    # location of ui elements
    FPS_COUNTER_LOC_X = window_size[0] - 50
    FPS_COUNTER_LOC_Y = 0

    # testing stuff
    galaxy = Galaxy("Milkyway")
    sols = galaxy.get_sols()
    print(sols)

    for sol in sols:
        print(sol.get_name())
        planets = sol.get_planets()
        for planet in planets:
            print(planet.get_name())
            if planet.get_atmosphere() is not None:
                planet.add_civilization(force_spawn_civilization(planet))
                planet.add_civilization(force_spawn_civilization(planet))
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
    UPDATE_TIME = pygame.USEREVENT + 0
    pygame.time.set_timer(UPDATE_TIME, config.SECOND)

    # logic
    ds_h = DataslateHandler()

    while active:

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN and pause is False:
                ds_h.handle_dataslate(all_sprites_list)

            if event.type == pygame.QUIT:
                # pylint:disable-next=invalid-name
                active = False
                print("Player quitted this game")

            elif event.type == pygame.KEYDOWN:
                # Quit game on escape
                if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                    # pylint:disable-next=invalid-name
                    active = False
                if event.key in [pygame.K_p, pygame.K_SPACE]:
                    if pause is True:
                        # pylint:disable-next=invalid-name
                        pause = False
                    else:
                        # pylint:disable-next=invalid-name
                        pause = True
                # Open / close console
                if event.key == pygame.K_c:
                    if consoleActive == False:
                        consoleActive = True
                        # Console is handled as a sprite
                        all_sprites_list.add(console)
                    else:
                        consoleActive = False
                        # Console is handled as a sprite
                        all_sprites_list.remove(console)

            elif event.type == UPDATE_TIME and pause is False:
                curr_date = curr_date + time_delta_per_sec

        # Logic here
        if pause is False:
            for sprite in all_sprites_list:
                sprite.step()
        # Console must not be paused
        if consoleActive == True:
            console.step()

        all_sprites_list.update()

        # Clear screen
        config.screen.fill(config.BLACK)

        # Draw Objects
        # pylint:disable-next=invalid-name
        fps_counter = str(round(config.clock.get_fps(), 2))
        config.FONT.render_to(config.screen, (FPS_COUNTER_LOC_X, FPS_COUNTER_LOC_Y), fps_counter, config.WHITE)
        config.FONT.render_to(config.screen, (0, 0), str(curr_date), config.WHITE)
        all_sprites_list.draw(config.screen)

        # Update screen
        pygame.display.flip()

        # Refresh time
        config.clock.tick(60)

    pygame.quit()
