from pico2d import *
open_canvas()
character = load_image('sprite_sheet.png')

frame = 0

#공통된 행동 정의(sprite sheet의 바텀좌표, x, y, 행동 프레임수)
def action(bottom, x, y, number_of_frames):
    global frame
    clear_canvas()
    character.clip_draw(frame * 64, bottom, 64, 64, x, y)
    update_canvas()
    frame = (frame + 1) % number_of_frames
    delay(0.05)
    get_events()

#오른쪽으로 이동(x : 50 ~ 750)
for x in range(50, 750+1, 5):
    action(64 * 4, x, 90, 9)

#위로 이동(y : 90 ~ 550)
for y in range(90, 550+1, 5):
    action(64 * 7, 750, y, 9)

#왼쪽으로 이동(x : 750 ~ 400)
for x in range(750, 400-1, -5):
    action(64 * 6, x, 550, 9)

#아래로 이동
for y in range(550, 300-1, -5):
    action(64 * 5, 400, y, 9)

#앞으로 창 찌르기
for frames_no in range(0, 8):
    action(64 * 9, 400, 300, 8)

#왼쪽으로 창 찌르기
for frames_no in range(0, 8):
    action(64 * 10, 400, 300, 8)

#뒤로 창 찌르기
for frames_no in range(0, 8):
    action(64 * 11, 400, 300, 8)

#오르쪽으로 창 찌르기
for frames_no in range(0, 8):
    action(64 * 8, 400, 300, 8)

#앞으로 가며 칼 휘두르기
for y in range(300, 270-1, -5):
    action(64 * 1, 400, y, 6)

#왼쪽으로 가며 칼 휘두르기
for x in range(400, 370-1, -5):
    action(64 * 2, x, 270, 6)

#뒤로 가며 칼 휘두르기
for y in range(270, 300+1, 5):
    action(64 * 3, 370, y, 6)

#오른쪽으로 가며 칼 휘두르기
for x in range(370, 400+1, 5):
    action(64 * 0, x, 300, 6)

#오른쪽으로 점프
for x in range(400, 500+1, 5):
    if (x <= 445):
        y = x - 100         #y : 300 ~ 345
    elif ((x > 445)&(x < 455)):
        y = 345
    else:
        y = 345 + 455 - x   #y : 345 ~ 300
    action(64 * 12, x, y, 7)

#왼쪽으로 점프
for x in range(500, 400-1, -5):
    if (x >= 455):
        y = 300 + 500 - x   #y : 300 ~ 345
    elif ((x < 455)&(x > 445)):
        y = 345
    else:
        y = 345 - 445 + x   #y : 345 ~ 300
    action(64 * 14, x, y, 7)

close_canvas()