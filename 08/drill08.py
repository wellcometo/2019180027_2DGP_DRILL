from pico2d import *

move = True
dir_x, dir_y = 0, 0
status = 3

def move_events():
    global move
    global dir_x, dir_y
    global status
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                status = 1
                dir_x += 1
            elif event.key == SDLK_LEFT:
                status = 0
                dir_x -= 1
            elif event.key == SDLK_UP:
                if status == 2:
                    status = 0
                elif status == 3:
                    status = 1
                dir_y += 1
            elif event.key == SDLK_DOWN:
                if status == 2:
                    status = 0
                elif status == 3:
                    status = 1
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                move = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                status = 3
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                status = 2
                dir_x += 1
            elif event.key == SDLK_UP:
                if status == 0:
                    status = 2
                elif status == 1:
                    status = 3
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                if status == 0:
                    status = 2
                elif status == 1:
                    status = 3
                dir_y += 1

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
frame = 0
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2

while move:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, status * 100, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    move_events()
    x += dir_x * 5
    if x > TUK_WIDTH:
        x = TUK_WIDTH
    if x < 0:
        x = 0
    y += dir_y * 5
    if y > TUK_HEIGHT:
        y = TUK_HEIGHT
    if y < 0:
        y = 0
    delay(0.01)