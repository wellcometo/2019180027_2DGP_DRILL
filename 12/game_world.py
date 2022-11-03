# layer 0: Background Objects
# layer 1: Midground Objects
# layer 2: Foreground Objects
objects = [[], [], []]  # layer 0 리스트, layer 1 리스트, layer 2 리스트


def add_object(o, depth):  # 객체 추가
    objects[depth].append(o)

def add_objects(ol, depth):  # 객체들 추가
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)  # 리스트로부터 삭제
            del o  # 실제로 메모리 삭제
            return
    raise ValueError('Trying destroy non existing object')

def all_objects():
    for layer in objects:
        for o in layer:
            yield o  # yield ~는 객체(~)를 넘겨줌, for 문과 함께 쓸 때 효율적임

def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()
