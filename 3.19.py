# Игра "Порази цель"
import turtle as t

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

t.hideturtle()
t.speed(0)
t.penup()
t.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
t.pendown()
t.setheading(EAST)
t.forward(TARGET_WIDTH)
t.setheading(NORTH)
t.forward(TARGET_WIDTH)
t.setheading(WEST)
t.forward(TARGET_WIDTH)
t.setheading(SOUTH)
t.forward(TARGET_WIDTH)
t.penup()

t.goto(0, 0)
t.setheading(EAST)
t.showturtle()
t.speed(PROJECTILE_SPEED)

angle = float(input('Введите угол снаряда: '))
force = float(input('Введите пусковую силу (1-10): '))

distance = force * FORCE_FACTOR

t.setheading(angle)

t.pendown()
t.forward(distance)

if (TARGET_LLEFT_X <= t.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    TARGET_LLEFT_Y <= t.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('Цель поражена!')
else:
    print('Вы промахнулись.')
    TARGET_TLEFT_Y = TARGET_LLEFT_Y + TARGET_WIDTH
    TARGET_LRIGHT_X = TARGET_LLEFT_X + TARGET_WIDTH
    # тангенс = противолежащий катет (высота) / прилежащий катет (ширина)
    # тангенсы высчитываются относительно начала координат (0, 0)
    TAN_TARGET_TLEFT = TARGET_TLEFT_Y / TARGET_LLEFT_X
    TAN_TARGET_LRIGHT = TARGET_LLEFT_Y / TARGET_LRIGHT_X
    TAN_TURTLE = t.ycor() / t.xcor()
    if TAN_TURTLE > TAN_TARGET_TLEFT:
        print('Попробуйте угол меньше')
    elif TAN_TURTLE < TAN_TARGET_LRIGHT:
        print('Попробуйте угол побольше')

    # т.к. по учебнику нам ещё не известна функция квадратного корня,
    # будем сравнивать квадраты расстояний
    MIN_DISTANCE_TO_TARGET =  TARGET_LLEFT_X ** 2 + TARGET_LLEFT_Y ** 2
    MAX_DISTANCE_TO_TARGET = TARGET_LRIGHT_X ** 2 + TARGET_TLEFT_Y ** 2
    SQR_DISTANCE = distance ** 2
    if SQR_DISTANCE < MIN_DISTANCE_TO_TARGET:
        print('Примените силу побольше')
    elif SQR_DISTANCE > MAX_DISTANCE_TO_TARGET:
        print('Примените силу поменьше')

t.done()

