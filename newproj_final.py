import random
from tkinter import *
import math #
WIDTH = 680 #задаем ширину окна
HEIGHT = 600 #задаем высоту окна
pi = math.pi
storage_path = 'collision.txt'  # назваине файла для записи

# радиус мяча
BALL_RADIUS = 1

# устанавливаем начальнй шаг шара
Speed = 1

# устанавливаем окно
root = Tk()
root.geometry("680x690")
root.title(" Sinai`s Billiard ")
run = None #переменная для начала движения
def angleMISTAKE(A,B): #функция, дающая случайную величину между А и В деленную на 100
    angleMISTAKE = random.uniform(A, B)/100
    print("~~~~~~~" + str(angleMISTAKE))
    return angleMISTAKE

def worker(): # функция, запускающая движение
    main()
    if run:
        root.after(26 - int(V), worker)  # вызываем саму себя каждые 26 - int(V) миллисекунд

def start():  # действие при кнопке старт
    global V, run, Radius, radius
    V = Speed_V.get()  #считываем значение скорости
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
    c.create_oval(WIDTH / 2 - Radius, # рисуем большой круг
                  HEIGHT / 2 - Radius,
                  WIDTH / 2 + Radius,
                  HEIGHT / 2 + Radius,
                  fill="white",
                  outline="black",
                  width=2)
    c.create_oval(WIDTH / 2 - radius, # рисуем малый круг
                  HEIGHT / 2 - radius,
                  WIDTH / 2 + radius,
                  HEIGHT / 2 + radius,
                  fill="white",
                  outline="black",
                  width=2)

def button_ok():  # действие при кнопке ОК возле углов
    global BALL, Ro, fi, Gamma, Beta, first_hit, Ball_x, Ball_y, R_hit
    Ro = float(B_Ro.get())
    Gamma = -float(B_Gamma.get()) * pi / 180 #считываем значение угла положения
    Beta = -float(angle.get()) * pi / 180 #считываем значение угла направления
    fi = Gamma
    print("Gamma:", Gamma)
    first_hit = None

    Ball_x = Ro * math.cos(Gamma) + WIDTH / 2
    Ball_y = Ro * math.sin(Gamma) + HEIGHT / 2
    BALL = c.create_oval(Ball_x - BALL_RADIUS / 2,
                         Ball_y - BALL_RADIUS / 2,
                         Ball_x + BALL_RADIUS / 2,
                         Ball_y + BALL_RADIUS / 2, fill="black")
    Gamma, R_hit, Beta = next_hit(Gamma, Ro, Beta)

btnSTART = Button(text="Старт",  # текст кнопки
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
angle.insert(0, '90')

Label(root, text=u'Введите начальную точку :').place(x=420, y=0)
Label(root, text='ρ(r,R)       γ(-180,180)').place(x=485, y=19)
B_Ro = Entry(root, width=4, background="grey", foreground="white")
B_Ro.place(x=490, y=38)
B_Ro.insert(0, '100')

B_Gamma = Entry(root, width=4, background="grey", foreground="white")
B_Gamma.place(x=555, y=38)
B_Gamma.insert(0, '-60')

Label(root, text=u'Введите радиусы :').place(x=168, y=0)
Label(root, text='Radius      radius').place(x=168, y=19)
Rad = Entry(root, width=4, background="grey", foreground="white", )
Rad.place(x=170, y=38)
Rad.insert(0, '200')

rad = Entry(root, width=4, background="grey", foreground="white", )
rad.place(x=225, y=38)
rad.insert(0, '30')

Button(text='ok', background="#555", foreground="white", command=lambda: button_ok()).place(x=620, y=34) # приписываем кнопкам действие
Button(text='ok', background="#555", foreground="white", command=lambda: create_Rr()).place(x=261, y=34)


def signum(float): #функция sign()
    if (float < 0):
        return -1
    elif (float > 0):
        return 1
    else:
        return float

def to_pi(Gamma2):                      # конвертирования угла в (-pi,pi)
    Gamma = 0
    if math.fabs(Gamma2) <= pi:
        Gamma = Gamma2
    elif (math.fabs(Gamma2) >= 2 * pi):
        Gamma2 = Gamma2 - signum(Gamma2) * 2 * pi
        Gamma = (Gamma2) % (2 * pi)
        if (math.fabs(Gamma) > pi and (math.fabs(Gamma) < 2 * pi)):
            Gamma = -signum(Gamma) * 2 * pi + Gamma
    elif (math.fabs(Gamma2) > pi and (math.fabs(Gamma2) < 2 * pi)):
        Gamma = (-signum(Gamma2) * 2 * pi + Gamma2)
    return Gamma

def move_ball(Beta): #движение шарика
    c.move(BALL, Speed * math.cos(Beta), Speed * math.sin(Beta))

def next_hit(Gamma, R_hit, Beta):
    global first_hit, fi, ball_centerX, ball_centerY, radius, Radius, Gamma_prev, R_hit_prev, x,Beta_TRUE

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
            Radius *=(1 + angleMISTAKE(-1,1))
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
        Beta_TRUE = to_pi(Gamma + x - pi) #+ angleMISTAKE(-1,1)*pi*100/180
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
        Radius *= (1 + angleMISTAKE(-1,1))
        R_NEXT = Radius
        # летим в малый круг
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
        Radius *= (1 + angleMISTAKE(-1, 1))
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

def main(): # функция , обрабатывающая положения шарика каждую итерацию и находящая столкновения при заданных условиях
    global fi, Gamma, Beta, Ro, Radius, R, R_hit, ball_centerX, ball_centerY, Gamma_prev
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)                              # считываем координаты шарика
    ball_centerY = (ball_top + ball_bot) / 2        #центр шарика по У
    ball_centerX = (ball_left + ball_right) / 2        #центр шарика по Х
    fi = math.atan2((ball_centerY - HEIGHT / 2), (ball_centerX - WIDTH / 2))
    R = ((ball_centerX - WIDTH / 2) ** 2 + (ball_centerY - HEIGHT / 2) ** 2) ** (1 / 2)

    if (((math.fabs(fi - Gamma) <= 0.05) or (   #ударились об большой круг
            (signum(Gamma) != signum(fi)) and ((math.fabs(Gamma) + math.fabs(fi)) >= (2 * pi - 0.05))))
            and ((math.fabs(R) >= (R_hit))and(math.fabs(R_hit-Radius)<=15))):
        print("------------------------------")
        print("fi:", fi, "Gamma:", Gamma, "R:", R, "R_hit", R_hit)
        print("big")
        with open(storage_path, 'a') as file:
            file.write('R_hit = ' + str(R_hit) + ', Gamma = ' + str(Gamma) + ', Beta = ' + str(Beta) + '\n')
        print("Before ", "Beta:", Beta, "Gamma:", Gamma,"Gamma_prev:", Gamma_prev)

        Gamma, R_hit, Beta = next_hit(Gamma, R, Beta)
        print("After ", "Beta:", Beta, "Gamma:", Gamma,"Gamma_prev:", Gamma_prev)

    elif (((math.fabs(fi - Gamma) <= 0.05) or (  #ударились об малый круг
            (signum(Gamma) != signum(fi)) and ((math.fabs(Gamma) + math.fabs(fi)) >= (2 * pi - 0.05))))
            and (math.fabs(R) <= (radius))):
        print("------------------------------")
        print("fi:", fi, "Gamma:", Gamma, "R:", R, "R_hit", R_hit)
        print("small")
        with open(storage_path, 'a') as file:
            file.write('R_hit = ' + str(R_hit) + ', Gamma = ' + str(Gamma) + ', Beta = ' + str(Beta) + '\n')

        print("Before ", "Beta:", Beta, "Gamma:", Gamma)
        Gamma, R_hit, Beta = next_hit(Gamma, R, Beta)
        print("After ", "Beta:", Beta, "Gamma:", Gamma)
    move_ball(Beta)  #вызываем функцию движения шарика

# запускаем работу окна
root.mainloop()
