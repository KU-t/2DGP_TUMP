import random
from pico2d import *
import game_framework
import game_world

from penguin import Penguin
from human import Human
from tip import Tip
from life import Life
from shoe import Shoe
from wall import Wall
name = "MainState"

penguin = None
students = []
tip = None
life = None
shoes = []
walls = []

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True

def collide_x_character_wall(character, wall):
    left_a, bottom_a, right_a, top_a = character.get_bb_collision_wall()
    left_b, bottom_b, right_b, top_b = wall.get_bb()

    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    if left_b <= left_a and left_a <= right_b:
        return True

    if left_b <= right_a and right_a <= right_b:
        return True

def collide_y_character_wall(character, wall):
    left_a, bottom_a, right_a, top_a = character.get_bb_collision_wall()
    left_b, bottom_b, right_b, top_b = wall.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False

    if bottom_b <= bottom_a and bottom_a <= top_b:
        return True

    elif bottom_b <= top_a and top_a <= top_b:
        return True


def enter():

    global students
    students = [Human(i * 100 - 800, i * 50, random.randint(0, 4)) for i in range(10)]
    for student in students:
        game_world.add_object(student, 1)

    global penguin
    penguin = Penguin()
    game_world.add_object(penguin, 1)

    global tip
    tip = Tip()
    game_world.add_object(tip, 0)

    global life
    life = Life()
    game_world.add_object(life, 1)

    global shoes
    shoes = [Shoe(i * 50 - 800, i * 100) for i in range(10)]
    for shoe in shoes:
        game_world.add_object(shoe, 0)

    global walls
    #세로 벽
    walls = [Wall((i + 1) * 200 - 800 - 40, -300 + 5, (i + 1) * 200 - 800 - 40, -150 - 5) for i in range(7)]
    walls += [Wall((i + 1) * 200 - 800 - 40, 0 + 5, (i + 1) * 200 - 800 - 40, 150 - 5) for i in range(5)]
    walls += [Wall((i + 1) * 200 - 800 - 40, 450 + 5, (i + 1) * 200 - 800 - 40, 600 - 5) for i in range(5)]
    walls += [Wall((i + 1) * 200 - 800 - 40, 750 + 5, (i + 1) * 200 - 800 - 40, 900 - 5) for i in range(7)]
    walls += [Wall(0 - 800- 40, -300, 0 - 800 - 40, 900), Wall(1600 - 800 - 40, -300, 1600 - 800- 40, 900)]

    #가로 벽
    walls += [Wall(0 + 5 - 800 - 40, - 300 + i * 150, 1600 - 5 - 800 - 40, -300 + i * 150) for i in range(9) if i == 0 or i == 8]
    walls += [Wall(0 + 5 - 800 - 40, - 300 + i * 150, 1200 - 800 - 40, -300 + i * 150) for i in range(9) if i == 3 or i == 5]
    walls += [Wall(1400 - 800 - 40, - 300 + i * 150, 1600 + 5 - 800 - 40, -300 + i * 150) for i in range(9) if i == 3 or i == 5]

    #입구 벽
    walls += [Wall(-100 + 400 * i + 5 - 800 - 40, - 300 + 150, 100 + 400 * i - 5 - 800 - 40, -300 + 150) for i in range(5)]
    walls += [Wall(-100 + 400 * i + 5 - 800 - 40, - 300 + 300, 100 + 400 * i - 5 - 800 - 40, -300 + 300) for i in range(5) if not i == 3]
    walls += [Wall(-100 + 400 * 3 + 5 - 800 - 40, - 300 + 300, 100 + 400 * 3 - 100 - 800 - 40, -300 + 300)]
    walls += [Wall(-100 + 400 * i + 5 - 800 - 40, - 300 + 900, 100 + 400 * i - 5 - 800 - 40, -300 + 900) for i in range(5) if not i == 3]
    walls += [Wall(-100 + 400 * 3 + 5 - 800 - 40, -300 + 900, 100 + 400 * 3 - 100 - 800 - 40, -300 + 900)]
    walls += [Wall(-100 + 400 * i + 5 - 800 - 40, -300 + 1050, 100 + 400 * i - 5 - 800 - 40, -300 + 1050) for i in range(5)]

    #입구 & 휴게실 & 중앙문
    walls += [Wall(1200 - 800 - 40, 0, 1200 - 800 - 40, 200), Wall(1200 - 800 - 40, 400, 1200 - 800 - 40, 600)]
    walls += [Wall(1400 - 800 - 40, 0, 1400 - 800 - 40, 200), Wall(1400 - 800 - 40, 300, 1400 - 800 - 40, 600)]
    walls += [Wall(1200 - 800 - 40, 200, 1200 - 800 - 40, 400)]
    #walls += [Wall(0 + 5, - 300 + i * 150, 1200, -300 + i * 150) for i in range(9) if i == 3 or i == 5]
    #walls += [Wall(1400, - 300 + i * 150, 1600 + 5, -300 + i * 150) for i in range(9) if i == 3 or i == 5]

    for wall in walls:
        game_world.add_object(wall, 0)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            penguin.direction[0] = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            penguin.direction[1] = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            penguin.direction[2] = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            penguin.direction[3] = True

        elif event.type == SDL_KEYUP and event.key == SDLK_UP:
            penguin.direction[0] = False
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            penguin.direction[1] = False
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:
            penguin.direction[2] = False
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            penguin.direction[3] = False

def update():
    for wall in walls:
        if collide_x_character_wall(penguin, wall):
            penguin.velocity_x = 0
            for shoe in shoes:
                shoe.velocity_x = 0
            for student in students:
                student.velocity_draw_x = 0
            for wall in walls:
                wall.velocity_x = 0

    for wall in walls:
        if collide_y_character_wall(penguin, wall):
            penguin.velocity_y = 0
            for shoe in shoes:
                shoe.velocity_y = 0
            for student in students:
                student.velocity_draw_y = 0
            for wall in walls:
                wall.velocity_y = 0

    for game_object in game_world.all_objects():
        game_object.update()
    update_obj()

    for student in students:
        if collide(penguin, student):
            if penguin.time_life == 0:
                penguin.time_life = 300
                life.life -= 1
        if (penguin.x - student.x)**2 + (penguin.y - student.y)**2 <= 20000:
            student.state = 'follow'
        else:
            student.state = 'move'

    for shoe in shoes:
        if collide(penguin, shoe):
            penguin.item += 1
            life.life += 1
            shoe.exist = False
            shoes.remove(shoe)
            game_world.remove_object(shoes)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def move_obj():
    if penguin.direction[0] == True:
        if penguin.direction[1] == True:
            count_x_decrease()
            count_y_increase()
            penguin.direct_frame = 4
        elif penguin.direction[2] == True:
            pass
        elif penguin.direction[3] == True:
            count_x_increase()
            count_y_increase()
            penguin.direct_frame = 2
        else:
            count_y_increase()
            penguin.direct_frame = 3


    elif penguin.direction[1] == True:
        if penguin.direction[2] == True:
            count_x_decrease()
            count_y_decrease()
            penguin.direct_frame = 6
        elif penguin.direction[3] == True:
            pass
        else:
            count_x_decrease()
            penguin.direct_frame = 5

    elif penguin.direction[2] == True:
        if penguin.direction[3] == True:
            count_x_increase()
            count_y_decrease()
            penguin.direct_frame = 0
        else:
            count_y_decrease()
            penguin.direct_frame = 7

    elif penguin.direction[3] == True:
        count_x_increase()
        penguin.direct_frame = 1


def update_obj():

    move_obj()

def count_x_increase():

    penguin.velocity_x += penguin.move_speed
    for shoe in shoes:
        shoe.velocity_x -= shoe.move_speed
    for student in students:
        student.velocity_draw_x -= student.move_speed
    for wall in walls:
        wall.velocity_x -= wall.move_speed
    #for resident in residents:
    #    resident.x -= penguin.move_speed



def count_y_increase():

    penguin.velocity_y += penguin.move_speed
    for shoe in shoes:
        shoe.velocity_y -= shoe.move_speed
    for student in students:
        student.velocity_draw_y -= student.move_speed
    for wall in walls:
        wall.velocity_y -= wall.move_speed
    #for resident in residents:
    #   resident.y -= penguin.move_speed


def count_x_decrease():

    penguin.velocity_x -= penguin.move_speed
    for shoe in shoes:
        shoe.velocity_x += shoe.move_speed
    for student in students:
        student.velocity_draw_x += student.move_speed
    for wall in walls:
        wall.velocity_x += wall.move_speed
    #for resident in residents:
    #       resident.x += penguin.move_speed


def count_y_decrease():

   penguin.velocity_y -= penguin.move_speed
   for shoe in shoes:
       shoe.velocity_y += shoe.move_speed
   for student in students:
       student.velocity_draw_y += student.move_speed
   for wall in walls:
       wall.velocity_y += wall.move_speed
   #for resident in residents:
   #    resident.y += penguin.move_speed
