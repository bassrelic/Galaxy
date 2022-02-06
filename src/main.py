"""This is the main file"""

from datetime import timedelta, date
import pygame
from galaxy.galaxy import Galaxy
from object.data_window import Dataslate

WHITE = ( 255, 255, 255)
BLACK = ( 0, 0, 0)
SECOND = 1000

def main():
    """This is the main Function of this Game"""
    curr_date = date.fromisoformat('2022-01-01')
    time_delta_per_sec = timedelta(days=1)

    # pygame section
    pygame.init()
    myfont = pygame.freetype.SysFont('Arial', 20)
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Galaxy")
    active = True
    clock = pygame.time.Clock()

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
    pygame.time.set_timer(update_time, SECOND)

    # UiElements
    dataslate = None
    selected_sprites = None

    while active:

        # Check cursor position
        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:

                for sprite in all_sprites_list:
                    if sprite.rect.collidepoint(mouse_position):
                        selected_sprites = sprite
                        break
                    else:
                        selected_sprites = None

                if selected_sprites is not None:
                    print("clicked object: " + selected_sprites.get_name())
                    mouse_x_pos = pygame.mouse.get_pos()[0]
                    mouse_y_pos = pygame.mouse.get_pos()[1]
                    intermed_obj = Dataslate(selected_sprites.get_name(), mouse_x_pos, mouse_y_pos)
                    
                    if dataslate is not None:
                        if intermed_obj.get_name() is not dataslate.get_name():
                            all_sprites_list.remove(dataslate)
                            del dataslate
                            dataslate = Dataslate(selected_sprites.get_name(), mouse_x_pos, mouse_y_pos)
                            all_sprites_list.add(dataslate)
                        else:
                            all_sprites_list.remove(dataslate)
                            del dataslate
                            dataslate = None
                    else:
                        dataslate = Dataslate(selected_sprites.get_name(), mouse_x_pos, mouse_y_pos)
                        all_sprites_list.add(dataslate)

                    del intermed_obj

            if event.type == pygame.QUIT:
                active = False
                print("Player quitted this game")

            elif event.type == pygame.KEYDOWN:
                # Quit game on escape
                if event.key == pygame.K_ESCAPE:
                    active = False

            elif event.type == update_time:
                curr_date = curr_date + time_delta_per_sec

        # Logic here
        all_sprites_list.update()

        # Clear screen
        screen.fill(BLACK)

        # Draw Objects
        myfont.render_to(screen, (450, 0), str(round(clock.get_fps(), 2)), WHITE)
        myfont.render_to(screen, (0, 0), str(curr_date), WHITE)
        all_sprites_list.draw(screen)

        # Update screen
        pygame.display.flip()

        # Refresh time
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
