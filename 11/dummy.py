class Star: # 클래스의 역할 : 함수 또는 그룹을 엮는다
    name = 'Star'
    x = 100

    def change():
        x = 200
        print('x is ', x)

print('x IS ', Star.x)  # 클래스 변수 액세스
Star.change()  # 클래스 함수 호출
print('x Is ', Star.x)

star = Star()  # 생성자가 없는데 생성??
# Star.change(star)
print(type(star))
print(star.x)  # 비록 객체 변수로 액세스했으나, 같은 이름의 클래스 변수가 우선.

# star.change()  # Star.change(star)와 동일
