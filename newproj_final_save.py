import random
from tkinter import *
import math
WIDTH = 680
HEIGHT = 600
pi = math.pi
storage_path = 'collision.txt'  # назваине файла для записи
Counter = 0
Colour = 'blue'
# радиус мяча
BALL_RADIUS = 1

# устанавливаем начальнй шаг шара
Speed = 1

# устанавливаем окно
root = Tk()
root.geometry("680x690")
root.title(" Sinai`s Billiard ")
run = None
def angleMISTAKE(A,B):
    angleMISTAKE = random.uniform(A, B)/100
    # print("~~~~~~~" + str(angleMISTAKE))
    return angleMISTAKE

def worker():
    main()
    if run:
        root.after(26 - int(V), worker)  # вызываем саму себя каждые 26 - int(V) миллисекунд

def start():  # действие при кнопке старт
    global V, run, Radius, radius,angleMIS
    V = Speed_V.get()
    if run == None:
        with open(storage_path, 'w') as file:  # сздаем файл и записываем в него радиусы
            file.write('Radius = ' + str(Radius) + ', radius = ' + str(radius) + '\n')
    root.after(0, worker)
    run = True


def stop():  # действие при кнопке стоп
    global run

    run = False

def create_Rr():  # действие при кнопке ок возле радиусов
    c.delete("all")
    global Radius, radius, run
    run == None
    Radius = float(Rad.get())
    radius = float(rad.get())
    c.create_oval(WIDTH / 2 - Radius,
                  HEIGHT / 2 - Radius,
                  WIDTH / 2 + Radius,
                  HEIGHT / 2 + Radius,
                  fill="white",
                  outline="black",
                  width=2)
    c.create_oval(WIDTH / 2 - radius,
                  HEIGHT / 2 - radius,
                  WIDTH / 2 + radius,
                  HEIGHT / 2 + radius,
                  fill="white",
                  outline="black",
                  width=2)

def button_ok():  # действие при кнопке ОК возле углов
    global BALL, Ro, fi, Gamma, Beta, first_hit, Ball_x, Ball_y, R_hit, BETA,GAMMA,BALL1,R_HIT,FIRST_HIT,Counter,angleMIS,Radius
    Ro = float(B_Ro.get())
    Gamma = -float(B_Gamma.get()) * pi / 180
    Beta = -float(angle.get()) * pi / 180
    BETA = Beta + 2*(pi / 180)
    fi = Gamma
    Radius = 200
    print("Gamma:", Gamma)
    first_hit = None
    FIRST_HIT = None
    angleMIS = angleMISTAKE(-1,1) * 0
    print("~~~~~~~" + str(angleMIS))
    Ball_x = Ro * math.cos(Gamma) + WIDTH / 2
    Ball_y = Ro * math.sin(Gamma) + HEIGHT / 2
    BALL = c.create_oval(Ball_x - BALL_RADIUS / 2,
                         Ball_y - BALL_RADIUS / 2,
                         Ball_x + BALL_RADIUS / 2,
                         Ball_y + BALL_RADIUS / 2, fill="black")
    BALL1 = c.create_oval(Ball_x - BALL_RADIUS / 2,
                         Ball_y - BALL_RADIUS / 2,
                         Ball_x + BALL_RADIUS / 2,
                         Ball_y + BALL_RADIUS / 2, fill="black")
    GAMMA, R_HIT, BETA = NEXT_HIT(Gamma, Ro, BETA)
    Gamma, R_hit, Beta = next_hit(Gamma, Ro, Beta)

def deviation():
    global Counter,Colour
    if Counter == 0:
        Counter = 1
        Colour = 'red'
    elif Counter == 1:
        Counter =0
        Colour = 'blue'

btnSTART = Button(text="Старт",  # текст кнопки1111
                  background="#555",  # фоновый цвет кнопки
                  foreground="white",  # цвет текста
                  padx="20",  # отступ от границ до содержимого по горизонтали
                  pady="8",  # отступ от границ до содержимого по вертикали
                  font="16",  # высота шрифта
                  command=lambda: start()
                  ).pack()

btnPAUSE = Button(text="Пауза",  # текст кнопки
                  background="#555",  # фоновый цвет кнопки
                  foreground="white",  # цвет текста
                  padx="20",  # отступ от границ до содержимого по горизонтали
                  pady="8",  # отступ от границ до содержимого по вертикали
                  font="16",  # высота шрифта
                  command=lambda: stop()
                  ).pack()

# область анимации
c = Canvas(root, width=WIDTH, height=HEIGHT, background="gray")
c.pack()

Label(root, text=u'Введите скорость от 1 до 25').place(x=5, y=0)
Speed_V = Entry(root, width=10, background="grey", foreground="white", )
Speed_V.place(x=55, y=20)
Speed_V.insert(0, '22')

Label(root, text=u'    β(-180,180)').place(x=395, y=19)
angle = Entry(root, width=4, background="grey", foreground="white", )
angle.place(x=425, y=38)
angle.insert(0, '25')

Label(root, text=u'Введите начальную точку :').place(x=420, y=0)
Label(root, text='ρ(r,R)       γ(-180,180)').place(x=485, y=19)
B_Ro = Entry(root, width=4, background="grey", foreground="white")
B_Ro.place(x=490, y=38)
B_Ro.insert(0, '31')

B_Gamma = Entry(root, width=4, background="grey", foreground="white")
B_Gamma.place(x=555, y=38)
B_Gamma.insert(0, '-15')

Label(root, text=u'Введите радиусы :').place(x=168, y=0)
Label(root, text='Radius      radius').place(x=168, y=19)
Rad = Entry(root, width=4, background="grey", foreground="white", )
Rad.place(x=170, y=38)
Rad.insert(0, '200')

rad = Entry(root, width=4, background="grey", foreground="white", )
rad.place(x=225, y=38)
rad.insert(0, '30')

Button(text='ok', background="#555", foreground="white", command=lambda: button_ok()).place(x=620, y=34)
Button(text='ok', background="#555", foreground="white", command=lambda: create_Rr()).place(x=261, y=34)
Button(text='deviation', background="#555", foreground="white", command=lambda: deviation()).place(x=56, y=50)

def signum(float):
    if (float < 0):
        return -1
    elif (float > 0):
        return 1
    else:
        return float

def to_pi(Gamma2):                      # конвертирования угла в (-pi,pi)
    Gamma = 0
    if math.fabs(Gamma2) <= pi:
        # if (math.fabs(Gamma2 + pi) <= 0.00000005):
        #     Gamma2 = -Gamma2
        Gamma = Gamma2
    elif (math.fabs(Gamma2) >= 2 * pi):
        Gamma2 = Gamma2 - signum(Gamma2) * 2 * pi
        Gamma = (Gamma2) % (2 * pi)
        if (math.fabs(Gamma) > pi and (math.fabs(Gamma) < 2 * pi)):
            Gamma = -signum(Gamma) * 2 * pi + Gamma
    elif (math.fabs(Gamma2) > pi and (math.fabs(Gamma2) < 2 * pi)):
        Gamma = (-signum(Gamma2) * 2 * pi + Gamma2)
        # if (math.fabs(Gamma + pi) <= 0.000000005):
        #     Gamma = -Gamma
    return Gamma

def move_ball(Beta,BETA):
    c.move(BALL, Speed * math.cos(Beta), Speed * math.sin(Beta))
    c.move(BALL1, Speed * math.cos(BETA), Speed * math.sin(BETA))

def NEXT_HIT(Gamma1, R_HIT, Beta1):
    global FIRST_HIT, fi1, radius, Radius, GAMMA_PREV, R_HIT_PREV, X ,BETA_TRUE,angleMIS,Counter
    print("1")
    if FIRST_HIT == None:  # высчитываем 1 столкновение
        GAMMA_PREV = Gamma1
        R_HIT_PREV = R_HIT
        if ((math.fabs(pi - math.fabs(Gamma1) - math.fabs(Beta1)) > math.asin((radius) / R_HIT)) or
                (signum(Beta1) == signum(Gamma1) and (
                        (pi - math.fabs(Beta1 - Gamma1)) > math.sin((radius) / Radius)))):  # удар в большой круг
            X = math.asin((math.sin(Beta1 - Gamma1 - pi)) * (R_HIT) / (Radius))
            Gamma = Beta1 + X
            print(Gamma, "Before")
            Gamma = to_pi(Gamma)
            print(Gamma, "after")
            FIRST_HIT = True
            BETA_TRUE=Beta1
            Radius = 200
            Radius *=(1 + angleMIS)
            return Gamma, Radius, Beta1
        else:  # иначе в малый
            print("into small")
            print(Gamma1, Beta1)
            Fi = pi - Gamma1 + Beta1
            pci = math.asin((math.sin(Fi) * (R_HIT) / (radius)))
            print(Fi, " Fi ", pci, " pci ")
            Gamma = Beta1 - pci + pi
            print(Gamma, "Bef", Gamma / pi)
            Gamma = to_pi(Gamma)
            print(Gamma, "af")
            FIRST_HIT = True
            BETA_TRUE = Beta1
            return Gamma, radius, Beta1
    elif (R_HIT >= Radius):  # если ударились в большой круг 2 и больше столкновение
        print("2")
        R_hit_now = Radius
        Radius = 200
        x1 = math.asin((math.sin(Beta1 - GAMMA_PREV - pi)) * (R_HIT_PREV) / (R_HIT))
        X = math.asin((math.sin(BETA_TRUE - GAMMA_PREV - pi)) * (R_HIT_PREV) / (Radius))
        BETA_TRUE = to_pi(Gamma1 + X - pi)
        Gamma2 = BETA_TRUE + X
        print("3")
        print("Beta_TRUE , Before to_pi", BETA_TRUE  ,(Gamma1 - X - pi ) )
        Beta = math.atan2(Radius * math.sin(Gamma2) - R_HIT * math.sin(fi1),
                          Radius * math.cos(Gamma2) - R_HIT * math.cos(fi1))

        print(Gamma2 * 180/pi, Beta* 180/pi, "Bef", Gamma2 / pi)

        Gamma2 = to_pi(Gamma2)
        Beta = to_pi(Beta)
        print(Gamma2, Beta, "af")
        x2 = math.asin(math.sin(Beta - Gamma2 - pi) * (Radius) / (R_HIT))
        print("x , x1 , x2: " ,X * 180/pi, x1 * 180/pi, x2 * 180/pi)
        c.create_line(R_HIT_PREV * math.cos(GAMMA_PREV) + WIDTH / 2,
                      R_HIT_PREV * math.sin(GAMMA_PREV) + HEIGHT / 2,
                      R_HIT * math.cos(Gamma1) + WIDTH / 2,
                      R_HIT * math.sin(Gamma1) + HEIGHT / 2)
        GAMMA_PREV = Gamma1
        R_HIT_PREV = R_hit_now
        Radius = 200
        Radius *= (1 + angleMIS)
        R_NEXT = Radius

        if (((math.fabs(pi - math.fabs(Gamma1) - math.fabs(Beta)) <= math.asin((radius) / Radius) )and (signum(Beta) != signum(Gamma1))) or
                (signum(Beta) == signum(Gamma1) and (
                        (pi - math.fabs(Beta - Gamma1)) <= math.sin((radius) / Radius)))):
            print("into small")
            print(pi - math.fabs(Gamma1) - math.fabs(Beta),pi - math.fabs(Beta - Gamma1), math.asin((radius) / Radius))
            Fi = pi - Gamma1 + BETA_TRUE
            pci = math.asin((math.sin(Fi) * (Radius) / (radius)))
            print(Fi, " Fi ", pci, " pci ")
            Gamma2 = BETA_TRUE - pci + pi
            print(Gamma2, "Bef")
            Gamma2 = to_pi(Gamma2)
            print(Gamma2, "af")
            Beta = math.atan2(radius * math.sin(Gamma2) - R_HIT * math.sin(fi1),
                              radius * math.cos(Gamma2) - R_HIT * math.cos(fi1))
            Radius = 200
            R_NEXT = radius
        return Gamma2, R_NEXT, Beta
    elif (R_HIT <= radius):  # если ударились в маленький круг 2 и больше столкновение
        print("R_HIT <= radius")
        Radius = 200
        Radius *= (1 + angleMIS)
        c.create_line(R_HIT_PREV * math.cos(GAMMA_PREV) + WIDTH / 2, R_HIT_PREV * math.sin(GAMMA_PREV) + HEIGHT / 2,
                      R_HIT * math.cos(Gamma1) + WIDTH / 2,
                      R_HIT * math.sin(Gamma1) + HEIGHT / 2)
        Gamma2 = 2*Gamma1 - GAMMA_PREV
        Gamma2 = to_pi(Gamma2)
        GAMMA_PREV = Gamma1
        Beta = math.atan2(Radius * math.sin(Gamma2) - R_HIT * math.sin(fi1),
                          Radius * math.cos(Gamma2) - R_HIT * math.cos(fi1))
        R_HIT_PREV = radius
        return Gamma2, Radius, Beta

def next_hit(Gamma, R_hit, Beta):
    global first_hit, fi, radius, Radius, Gamma_prev, R_hit_prev, x,Beta_TRUE

    if first_hit == None:  # высчитываем 1 столкновение
        Gamma_prev = Gamma
        R_hit_prev = R_hit
        if ((math.fabs(pi - math.fabs(Gamma) - math.fabs(Beta)) > math.asin((radius) / R_hit)) or
                (signum(Beta) == signum(Gamma) and (
                        (pi - math.fabs(Beta - Gamma)) > math.sin((radius) / Radius)))):  # удар в большой круг
            x = math.asin((math.sin(Beta - Gamma - pi)) * (R_hit) / (Radius))
            Gamma = Beta + x
            print(Gamma, "Before")
            Gamma = to_pi(Gamma)
            print(Gamma, "after")
            first_hit = True
            Beta_TRUE=Beta
            Radius = 200
            Radius *=(1 + angleMIS)
            return Gamma, Radius, Beta
        else:  # иначе в малый
            print("into small")
            print(Gamma, Beta)
            Fi = pi - Gamma + Beta
            pci = math.asin((math.sin(Fi) * (R_hit) / (radius)))
            print(Fi, " Fi ", pci, " pci ")
            Gamma = Beta - pci + pi
            print(Gamma, "Bef", Gamma / pi)
            Gamma = to_pi(Gamma)
            print(Gamma, "af")
            first_hit = True
            Beta_TRUE = Beta
            return Gamma, radius, Beta
    elif (R_hit >= Radius):  # если ударились в большой круг 2 и больше столкновение
        R_hit_now = Radius
        Radius = 200
        x1 = math.asin((math.sin(Beta - Gamma_prev - pi)) * (R_hit_prev) / (R_hit))
        x = math.asin((math.sin(Beta_TRUE - Gamma_prev - pi)) * (R_hit_prev) / (Radius))
        Beta_TRUE = to_pi(Gamma + x - pi)
        Gamma2 = Beta_TRUE + x
        print("Beta_TRUE , Before to_pi", Beta_TRUE  ,(Gamma - x - pi ) )
        Beta = math.atan2(Radius * math.sin(Gamma2) - R_hit * math.sin(fi),
                          Radius * math.cos(Gamma2) - R_hit * math.cos(fi))

        print(Gamma2 * 180/pi, Beta* 180/pi, "Bef", Gamma2 / pi)

        Gamma2 = to_pi(Gamma2)
        Beta = to_pi(Beta)
        print(Gamma2, Beta, "af")
        x2 = math.asin(math.sin(Beta - Gamma2 - pi) * (Radius) / (R_hit))
        print("x , x1 , x2: " ,x * 180/pi, x1 * 180/pi, x2 * 180/pi)
        c.create_line(R_hit_prev * math.cos(Gamma_prev) + WIDTH / 2,
                      R_hit_prev * math.sin(Gamma_prev) + HEIGHT / 2,
                      R_hit * math.cos(Gamma) + WIDTH / 2,
                      R_hit * math.sin(Gamma) + HEIGHT / 2)
        Gamma_prev = Gamma
        R_hit_prev = R_hit_now
        Radius = 200
        Radius *= (1 + angleMIS)
        R_NEXT = Radius

        if (((math.fabs(pi - math.fabs(Gamma) - math.fabs(Beta)) <= math.asin((radius) / Radius) )and (signum(Beta) != signum(Gamma))) or
                (signum(Beta) == signum(Gamma) and (
                        (pi - math.fabs(Beta - Gamma)) <= math.sin((radius) / Radius)))):
            print("into small")
            print(pi - math.fabs(Gamma) - math.fabs(Beta),pi - math.fabs(Beta - Gamma), math.asin((radius) / Radius))
            Fi = pi - Gamma + Beta_TRUE
            pci = math.asin((math.sin(Fi) * (Radius) / (radius)))
            print(Fi, " Fi ", pci, " pci ")
            Gamma2 = Beta_TRUE - pci + pi
            print(Gamma2, "Bef")
            Gamma2 = to_pi(Gamma2)
            print(Gamma2, "af")
            Beta = math.atan2(radius * math.sin(Gamma2) - R_hit * math.sin(fi),
                              radius * math.cos(Gamma2) - R_hit * math.cos(fi))
            Radius = 200
            R_NEXT = radius
        return Gamma2, R_NEXT, Beta
    elif (R_hit <= radius):  # если ударились в маленький круг 2 и больше столкновение
        print("R_hit <= radius")
        Radius = 200
        Radius *= (1 + angleMIS)
        c.create_line(R_hit_prev * math.cos(Gamma_prev) + WIDTH / 2, R_hit_prev * math.sin(Gamma_prev) + HEIGHT / 2,
                      R_hit * math.cos(Gamma) + WIDTH / 2,
                      R_hit * math.sin(Gamma) + HEIGHT / 2)
        Gamma2 = 2*Gamma - Gamma_prev
        Gamma2 = to_pi(Gamma2)
        Gamma_prev = Gamma
        Beta = math.atan2(Radius * math.sin(Gamma2) - R_hit * math.sin(fi),
                          Radius * math.cos(Gamma2) - R_hit * math.cos(fi))
        R_hit_prev = radius
        return Gamma2, Radius, Beta

def main():
    global fi, Gamma, Beta, Ro, Radius, R, R_hit, Gamma_prev, fi1,R1,R_HIT,GAMMA_PREV,GAMMA,BETA,Colour
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)                              # считываем координаты шарика
    ball_left1, ball_top1, ball_right1, ball_bot1 = c.coords(BALL1)
    ball_centerY = (ball_top + ball_bot) / 2
    ball_centerX = (ball_left + ball_right) / 2
    fi = math.atan2((ball_centerY - HEIGHT / 2), (ball_centerX - WIDTH / 2))
    ball_centerY1 = (ball_top1 + ball_bot1) / 2
    ball_centerX1 = (ball_left1 + ball_right1) / 2
    fi1 = math.atan2((ball_centerY1 - HEIGHT / 2), (ball_centerX1 - WIDTH / 2))
    c.create_line(ball_centerX,ball_centerY,ball_centerX1,ball_centerY1, fill = Colour)

    R = ((ball_centerX - WIDTH / 2) ** 2 + (ball_centerY - HEIGHT / 2) ** 2) ** (1 / 2)
    R1 = ((ball_centerX1 - WIDTH / 2) ** 2 + (ball_centerY1 - HEIGHT / 2) ** 2) ** (1 / 2)

    if (((math.fabs(fi - Gamma) <= 0.05) or (
            (signum(Gamma) != signum(fi)) and ((math.fabs(Gamma) + math.fabs(fi)) >= (2 * pi - 0.05))))
            and ((math.fabs(R) >= (R_hit))and(math.fabs(R_hit-Radius)<=15))):
        print("-----------------1-------------")
        print("fi:", fi, "Gamma:", Gamma, "R:", R, "R_hit", R_hit)
        print("big")
        with open(storage_path, 'a') as file:
            file.write('R_hit = ' + str(R_hit) + ', Gamma = ' + str(Gamma) + ', Beta = ' + str(Beta) + '\n')
        print("Before ", "Beta:", Beta, "Gamma:", Gamma,"Gamma_prev:", Gamma_prev)

        Gamma, R_hit, Beta = next_hit(Gamma, R, Beta)
        print("After ", "Beta:", Beta, "Gamma:", Gamma,"Gamma_prev:", Gamma_prev)

    elif (((math.fabs(fi - Gamma) <= 0.05) or (
            (signum(Gamma) != signum(fi)) and ((math.fabs(Gamma) + math.fabs(fi)) >= (2 * pi - 0.05))))
            and (math.fabs(R) <= (radius))):
        print("----------------1--------------")
        print("fi:", fi, "Gamma:", Gamma, "R:", R, "R_hit", R_hit)
        print("small")
        with open(storage_path, 'a') as file:
            file.write('R_hit = ' + str(R_hit) + ', Gamma = ' + str(Gamma) + ', Beta = ' + str(Beta) + '\n')

        print("Before ", "Beta:", Beta, "Gamma:", Gamma)
        Gamma, R_hit, Beta = next_hit(Gamma, R, Beta)
        print("After ", "Beta:", Beta, "Gamma:", Gamma)
    if (((math.fabs(fi1 - GAMMA) <= 0.05) or (
            (signum(GAMMA) != signum(fi1)) and ((math.fabs(GAMMA) + math.fabs(fi1)) >= (2 * pi - 0.05))))
            and ((math.fabs(R1) >= (R_HIT))and(math.fabs(R_HIT-Radius)<=15))):
        print("---------------2---------------")
        print("fi:", fi1, "Gamma:", GAMMA, "R:", R1, "R_hit", R_HIT)
        print("big")
        with open(storage_path, 'a') as file:
            file.write('R_hit = ' + str(R_HIT) + ', Gamma = ' + str(GAMMA) + ', Beta = ' + str(BETA) + '\n')
        print("Before ", "Beta:", BETA, "Gamma:", GAMMA,"Gamma_prev:", GAMMA_PREV)

        GAMMA, R_HIT, BETA = NEXT_HIT(GAMMA, R1, BETA)
        print("After ", "Beta:", Beta, "Gamma:", Gamma,"Gamma_prev:", Gamma_prev)

    elif (((math.fabs(fi1 - GAMMA) <= 0.05) or (
            (signum(GAMMA) != signum(fi1)) and ((math.fabs(GAMMA) + math.fabs(fi1)) >= (2 * pi - 0.05))))
            and (math.fabs(R1) <= (radius))):
        print("-------------2-----------------")
        print("fi:", fi1, "Gamma:", GAMMA, "R:", R1, "R_hit", R_HIT)
        print("small")
        with open(storage_path, 'a') as file:
            file.write('R_hit = ' + str(R_HIT) + ', Gamma = ' + str(GAMMA) + ', Beta = ' + str(BETA) + '\n')

        print("Before ", "Beta:", BETA, "Gamma:", GAMMA)
        GAMMA, R_HIT, BETA = NEXT_HIT(GAMMA, R1, BETA)
        print("After ", "Beta:", BETA, "Gamma:", GAMMA)
    move_ball(Beta,BETA)

# запускаем работу окна
root.mainloop()
