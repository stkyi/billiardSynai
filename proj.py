from tkinter import *
import math
WIDTH = 680
HEIGHT = 600
pi = 3.14159265359

#радиус мяча
BALL_RADIUS = 8
#радиус кругов
# Radius = 200
# radius = 30
#устанавливаем начальнй шаг шара
Speed = 1

# устанавливаем окно
root = Tk()
root.geometry("680x690")
root.title(" Sinai`s Billiard ")
run = None
a = []
class Ball:
    def __init__(self,Gamma,R_hit,Beta,Gamma_prev,R_hit_prev ):
        self.Gamma = Gamma
        self.R_hit = R_hit
        self.Beta = Beta
        self.Gamma_prev = Gamma_prev
        self.R_hit_prev = R_hit_prev
        if small_previous == None:
            self.Ball_x = R_hit * math.cos(Gamma) + WIDTH / 2
            self.Ball_y = R_hit * math.sin(Gamma) + HEIGHT / 2
    def img(self):
        BALL = c.create_oval(self.Ball_x - BALL_RADIUS / 2,
                             self.Ball_y - BALL_RADIUS / 2,
                             self.Ball_x + BALL_RADIUS / 2,
                             self.Ball_y + BALL_RADIUS / 2, fill="black")
        ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
        return BALL



def worker():
    for i in range (len(a)):
        Gamma, R_hit, Beta, Gamma_prev, R_hit_prev = main(a[i-1])
        a[i-1] = a[i-1](Gamma,R_hit,Beta,Gamma_prev,R_hit_prev )
    if run:
        root.after(26 - int(V), worker) # вызываем саму себя каждые 30 миллисекунд
def start():
    global V,run,Radius,radius
    if run == None:
        V  = Speed_V.get()
        with open(storage_path, 'w') as file:
            file.write('Radius = ' + str(Radius)  + ', radius = ' + str(radius) + '\n')
    run = True
    root.after(0, worker)
def stop():
    global run
    print(a)
    run = False
def create_Rr():
    global Radius, radius
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
def button_ok() :
    global small_previous
    #global Ro,fi,Gamma,Beta,small_previous,R_hit,R,R_hit_prev,Gamma_prev
    Ro = float(B_Ro.get())
    R = Ro
    Gamma = -float(B_Gamma.get())*pi / 180
    Beta = -float(angle.get()) * pi / 180
    if (math.fabs(Beta - pi) <= 0.005):
        Beta = -pi
    if (math.fabs(Gamma - pi)<=0.005):
        Gamma = -pi
    fi = Gamma
    small_previous = None
    Gamma_prev = 0
    R_hit_prev = 0
    ball = Ball(Gamma,Ro,Beta,Gamma_prev,R_hit_prev)
    a.append(ball)
    i = len(a)
    a[i - 1].img()
    Gamma,R_hit,Beta,Gamma_prev,R_hit_prev = next_hit(Gamma,Ro,Beta,fi,Gamma_prev,R_hit_prev)
    a[i - 1] = Ball(Gamma, R_hit, Beta, Gamma_prev, R_hit_prev)

Button(text="Старт",          # текст кнопки1111
             background="#555",     # фоновый цвет кнопки
             foreground="white",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16",              # высота шрифта

             command = lambda :start()
             ).pack()

Button(text="Пауза",          # текст кнопки
             background="#555",     # фоновый цвет кнопки
             foreground="white",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16",              # высота шрифта
             command = lambda : stop()
             ).pack()
# область анимации
c = Canvas(root, width=WIDTH, height=HEIGHT, background="gray")
c.pack()

Label(root, text = u'Введите скорость от 1 до 25').place(x = 5 , y = 0)
Speed_V = Entry(root, width = 10,background = "grey",foreground="white",)
Speed_V.place(x = 55, y = 20)
Speed_V.insert(0, '16')

Label(root, text = u'Beta(-180,180)').place(x = 395 , y = 19)
angle = Entry(root, width = 4,background = "grey",foreground="white",)
angle.place(x = 425, y = 38)
angle.insert(0,'110')

Label(root, text = u'Введите начальную точку :').place(x = 420 , y = 0)
Label(root, text = 'ρ(r,R)   Gamma(-180,180)').place(x = 485 , y = 19)
B_Ro = Entry(root, width = 4,background = "grey",foreground="white")
B_Ro.place(x = 490, y = 38)
B_Ro.insert(0,'100')

B_Gamma = Entry(root, width = 4,background = "grey",foreground="white")
B_Gamma.place(x = 555, y = 38)
B_Gamma.insert(0,'-60')

Label(root, text = u'Введите радиусы :').place(x = 168 , y = 0)
Label(root, text = 'Radius      radius').place(x = 168 , y = 19)
Rad = Entry(root, width = 4,background = "grey",foreground="white",)
Rad.place(x = 170, y = 38)
Rad.insert(0,'200')

rad = Entry(root, width = 4,background = "grey",foreground="white",)
rad.place(x = 225, y = 38)
rad.insert(0,'30')


Button(text = 'ok',background = "#555",foreground="white", command = lambda : button_ok()).place(x = 620, y = 34)
Button(text = 'ok',background = "#555",foreground="white", command = lambda : create_Rr()).place(x = 261, y = 34)



def signum(float):
 if(float < 0): return -1;
 elif(float > 0): return 1;
 else: return float;

def to_pi(Gamma2):
    Gamma = 0
    if math.fabs(Gamma2) <= pi:
        if (math.fabs(Gamma2 + pi) <= 0.000005):
            Gamma2 = -Gamma2
        Gamma = Gamma2
    elif (math.fabs(Gamma2) >= 2 * pi):
        Gamma2 = Gamma2 - signum(Gamma2) * 2 * pi
        Gamma = (Gamma2) % (2 * pi)
        if (math.fabs(Gamma) > pi and (math.fabs(Gamma) < 2 * pi)):
            Gamma = -signum(Gamma) * 2 * pi + Gamma
    elif (math.fabs(Gamma2) > pi and (math.fabs(Gamma2) < 2 * pi)):
        Gamma = (-signum(Gamma2) * 2 * pi + Gamma2)
        if (math.fabs(Gamma + pi) <= 0.000005):
            Gamma = -Gamma
    return Gamma

def move_ball(BALL,Beta):
    c.move(BALL,Speed*math.cos(Beta),Speed*math.sin(Beta))

def next_hit(Gamma,R_hit,Beta,fi,Gamma_prev,R_hit_prev):
    global small_previous,x

    if small_previous == None :
        Gamma_prev = Gamma
        R_hit_prev = R_hit
        if ((math.fabs(pi - math.fabs(Gamma) - math.fabs(Beta) ) > math.sin((radius)/R_hit))or
                (signum(Beta) == signum(Gamma) and ((pi - math.fabs(Beta - Gamma)) > math.sin((radius) / Radius)))):
            x = math.asin((math.sin(Beta - Gamma - pi)) * (R_hit) / (Radius))
            Gamma = Beta + x
            print(Gamma,"Bef")
            Gamma = to_pi(Gamma)
            print(Gamma, "af")
            small_previous = True
            return Gamma,Radius,Beta,Gamma_prev,R_hit_prev
        else:
            print("smal None")
            print(Gamma,Beta)
            Fi = pi - Gamma + Beta
            pci = math.asin((math.sin(Fi)*(R_hit)/(radius)))
            x = pi + Fi + pci
            print(Fi," Fi ",pci," pci ",x," x " )
            Gamma = Beta - pci + pi
            print(Gamma, "Bef",Gamma/pi)
            Gamma = to_pi(Gamma)
            print(Gamma, "af")
            small_previous = True
            return Gamma,radius,Beta,Gamma_prev,R_hit_prev
    elif(R_hit >= Radius):

        Gamma2 = Gamma - pi - 2 * (Beta - Gamma)
        Beta = math.atan2(Radius * math.sin(Gamma2) - R_hit * math.sin(fi),
                          Radius * math.cos(Gamma2) - R_hit * math.cos(fi))
        print(Gamma2, Beta, "Bef", Gamma2 / pi)
        Gamma2 = to_pi(Gamma2)
        Beta = to_pi(Beta)
        print(Gamma2, Beta, "af")
        c.create_line(R_hit_prev * math.cos(Gamma_prev) + WIDTH/2, R_hit_prev * math.sin(Gamma_prev) + HEIGHT/2, R_hit * math.cos(Gamma) + WIDTH/2,
                      R_hit * math.sin(Gamma) + HEIGHT/2)
        if((math.fabs(pi - math.fabs(Gamma) - math.fabs(Beta)) > math.sin((radius) / R_hit)) or
            (signum(Beta) == signum(Gamma) and ((pi - math.fabs(Beta - Gamma)) > math.sin((radius) / Radius)))):
            print("not into small",math.sin((radius) / R_hit),math.fabs(-math.fabs(Gamma) - math.fabs(Beta)))

            Gamma_prev = Gamma
            R_hit_prev = R_hit
            return Gamma2,Radius,Beta,Gamma_prev,R_hit_prev
        else:
            print("into small")
            print(Gamma,Gamma*180/pi,Gamma_prev,Gamma_prev*180/pi)
            Gamma2=(Gamma - Gamma_prev) + Gamma
            Beta = math.atan2(radius * math.sin(Gamma2) - R_hit * math.sin(fi),
                              radius * math.cos(Gamma2) - R_hit * math.cos(fi))
            # Fi = pi - Gamma + Beta
            # # Fi = to_pi(Fi)
            # pci = math.asin((math.sin(Fi)*(Radius)/(radius)))
            # print(Fi," Fi ",pci," pci " )
            # Gamma2 = Beta - pci + pi
            print(Gamma2, "Bef",Gamma2/pi)
            Gamma2 = to_pi(Gamma2)
            print(Gamma2, "af")
            Gamma_prev = Gamma
            # Fi = math.asin(math.sin(pci)*R_hit/(BALL_RADIUS+radius))
            # pci = pi + Fi + Gamma
            # Gamma2 = -pi + pci
            # Gamma3 = Gamma2
            R_hit_prev = R_hit
            return Gamma2,radius,Beta,Gamma_prev,R_hit_prev
    elif(R_hit <= radius ):
        print("R_hit <= radius")
        c.create_line(R_hit_prev * math.cos(Gamma_prev) + WIDTH/2, R_hit_prev * math.sin(Gamma_prev) + HEIGHT/2, R_hit * math.cos(Gamma) + WIDTH/2,
                      R_hit * math.sin(Gamma) + HEIGHT/2)
        Fi = -pi - Beta + Gamma_prev
        kci = -Gamma_prev + Gamma
        pci = -pi - kci - Fi
        Gamma2 = Gamma - pi - pci - Fi
        Gamma2 = to_pi(Gamma2)
        Gamma_prev = Gamma
        Beta = math.atan2(Radius*math.sin(Gamma2) - R_hit*math.sin(fi),Radius*math.cos(Gamma2) -  R_hit*math.cos(fi))
        R_hit_prev = R_hit
        return Gamma2,Radius,Beta,Gamma_prev,R_hit_prev

storage_path = 'collision.txt'

def main(cls):
    # global Gamma, Beta, R_hit, Gamma_prev, R_hit_prev
    ball_left, ball_top, ball_right, ball_bot = c.coords(cls.img)
    ball_centerY = (ball_top + ball_bot) / 2
    ball_centerX = (ball_left + ball_right) / 2
    fi = math.atan2((ball_centerY - HEIGHT/2),(ball_centerX - WIDTH/2))
    if (math.fabs(fi + pi)<=0.000002):
        fi = pi
    R = ((ball_centerX - WIDTH/2)**2 + (ball_centerY - HEIGHT/2)**2)**(1/2)
    print("fi:",fi,"Gamma:",cls.Gamma,"R:",R,"R_hit",cls.R_hit)
    if ((math.fabs(fi - cls.Gamma)<=0.05) and (math.fabs(R) >= (Radius))):
        print("big")
        with open(storage_path, 'a') as file:
            file.write('R_hit = '+ str(cls.R_hit) + ', Gamma = ' + str(cls.Gamma)+ '\n' )
        print("Before ","Beta:", cls.Beta, "Gamma:",cls.Gamma,cls.Gamma_prev)
        Gamma,R_hit,Beta,Gamma_prev,R_hit_prev = next_hit(cls.Gamma,R,cls.Beta,fi,cls.Gamma_prev,cls.R_hit_prev)
        print("After ","Beta:", Beta, "Gamma:", Gamma,Gamma_prev)

    elif((math.fabs(fi - cls.Gamma)<=0.05) and (math.fabs(R) <= (radius))):
        print("small")
        with open(storage_path, 'a') as file:
            file.write('R_hit = ' + str(cls.R_hit) + ', Gamma = ' + str(cls.Gamma) + '\n')
        print("Before ","Beta:", cls.Beta, "Gamma:",cls.Gamma)
        Gamma,R_hit,Beta,Gamma_prev,R_hit_prev = next_hit(cls.Gamma,R,cls.Beta,fi,cls.Gamma_prev,cls.R_hit_prev)
        print("After ","Beta:", Beta, "Gamma:", Gamma)
    else:
        Gamma, R_hit, Beta, Gamma_prev, R_hit_prev = cls.Gamma, cls.R_hit, cls.Beta, cls.Gamma_prev, cls.R_hit_prev
    move_ball(cls.img,cls.Beta)
    return Gamma, R_hit, Beta, Gamma_prev, R_hit_prev

# запускаем работу окна
root.mainloop()