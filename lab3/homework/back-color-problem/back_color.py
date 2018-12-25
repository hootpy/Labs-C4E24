from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]
def is_inside(a,b):
    s1 = b[3]*abs(a[0]-b[0])
    s2 = b[3]*abs(b[0]+b[2]-a[0])
    s3 = b[2]*abs(a[1]-b[1])
    s4 = b[2]*abs(b[1]+b[3]-a[1])
    s = b[3]*b[2]
    if s1 + s2 + s3 + s4 == 2*s:
        return True
    else:
        return False

def get_shapes():
    return shapes


def generate_quiz():
    text = choice(shapes)['text']
    color = choice(shapes)['color']
    quiz_type = randint(0, 1)
    return [
                text,
                color,
                quiz_type
            ]

def mouse_press(x, y, text, color, quiz_type):
    mouse_pos = [x,y]
    if quiz_type == 0:
        for text_pos in shapes:
            if text == text_pos['text']:
                if is_inside(mouse_pos,text_pos['rect']):
                    return True
                else:
                    return False
    else:
        for color_pos in shapes:
            if color == color_pos['color']:
                if is_inside(mouse_pos,color_pos['rect']):
                    return True
                else:
                    return False
    
