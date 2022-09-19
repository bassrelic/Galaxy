"""This module is intended to make utilities available which are expected to be used by multiple modules"""
import pygame

# pylint: disable-next=too-many-statements, too-many-branches
def getkeystroke():
    """Thi function checks pygame events and returns known keystrokes"""
    retval = None
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            
            if event.key is pygame.K_a:
                retval = 'a'
            elif event.key is pygame.K_b:
                retval = 'b'
            elif event.key is pygame.K_c:
                retval = 'c'
            elif event.key is pygame.K_d:
                retval = 'd'
            elif event.key is pygame.K_e:
                retval = 'e'
            elif event.key is pygame.K_f:
                retval = 'f'
            elif event.key is pygame.K_g:
                retval = 'g'
            elif event.key is pygame.K_h:
                retval = 'h'
            elif event.key is pygame.K_i:
                retval = 'i'
            elif event.key is pygame.K_j:
                retval = 'j'
            elif event.key is pygame.K_k:
                retval = 'k'
            elif event.key is pygame.K_l:
                retval = 'l'
            elif event.key is pygame.K_m:
                retval = 'm'
            elif event.key is pygame.K_n:
                retval = 'n'
            elif event.key is pygame.K_o:
                retval = 'o'
            elif event.key is pygame.K_p:
                retval = 'p'
            elif event.key is pygame.K_q:
                retval = 'q'
            elif event.key is pygame.K_r:
                retval = 'r'
            elif event.key is pygame.K_s:
                retval = 's'
            elif event.key is pygame.K_t:
                retval = 't'
            elif event.key is pygame.K_u:
                retval = 'u'
            elif event.key is pygame.K_v:
                retval = 'v'
            elif event.key is pygame.K_w:
                retval = 'w'
            elif event.key is pygame.K_x:
                retval = 'x'
            elif event.key is pygame.K_y:
                retval = 'y'
            elif event.key is pygame.K_z:
                retval = 'z'
            elif event.key is pygame.K_0:
                retval = '0'
            elif event.key is pygame.K_1:
                retval = '1'
            elif event.key is pygame.K_2:
                retval = '2'
            elif event.key is pygame.K_3:
                retval = '3'
            elif event.key is pygame.K_4:
                retval = '4'
            elif event.key is pygame.K_5:
                retval = '5'
            elif event.key is pygame.K_6:
                retval = '6'
            elif event.key is pygame.K_7:
                retval = '7'
            elif event.key is pygame.K_8:
                retval = '8'
            elif event.key is pygame.K_9:
                retval = '9'
            elif event.key is pygame.K_KP_EQUALS:
                retval = '='
            elif event.key is pygame.K_PERIOD:
                retval = '.'
            elif event.key is pygame.K_COMMA:
                retval = ','
            elif event.key is pygame.K_MINUS:
                retval = '-'
            elif event.key is pygame.K_RETURN:
                retval = '\n'
            else:
                retval = None

    return retval
