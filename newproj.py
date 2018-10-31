# from tkinter import *
# import math
# WIDTH = 500
# HEIGHT = 500
# pi = 3.14159265359
#
# #радиус мяча
# BALL_RADIUS = 8
# #радиус кругов
# Radius = 200
# radius = 30
# #устанавливаем начальнй шаг шара
# Speed = 1
#
# # устанавливаем окно
# root = Tk()
# root.geometry("500x680")
# root.title(" Sinai`s Billiard ")
# run = False
# Ball_x, Ball_y = 150,250
# def worker():
#     main()
#     if run:
#         root.after(26 - int(V), worker) # вызываем саму себя каждые 30 миллисекунд
# def start():
#     global V,run
#     V  = Speed_V.get()
#     run = True
#     root.after(0, worker)
# def stop():
#     global run
#     run = False
# def button_ok_fi():
#     global fi, Radian,k,b,X1, Y1, X2, Y2,x1, y1, x2, y2,x0,y0
#     fi = -float(angle.get())
#     print(fi)
#     Radian = pi * fi / 180
#     x0 = Ball_x
#     y0 = Ball_y
#     k = K(Radian)
#     b = B(Radian, x0, y0)
#     X1, Y1, X2, Y2 = XY(Radian, x0, y0)
#     x1, y1, x2, y2 = xy(Radian, x0, y0)
#     print(X1, Y1, X2, Y2)
#
# def button_ok() :
#     global Ball_y ,Ball_x,BALL
#     Ball_x = float(B_X.get())
#     Ball_y = float(B_Y.get())
#     print (Ball_x,Ball_y)
#     BALL = c.create_oval(Ball_x - BALL_RADIUS / 2,
#                          Ball_y - BALL_RADIUS / 2,
#                          Ball_x + BALL_RADIUS / 2,
#                          Ball_y + BALL_RADIUS / 2, fill="black")
#
# Button(text="Старт",          # текст кнопки
#              background="#555",     # фоновый цвет кнопки
#              foreground="white",     # цвет текста
#              padx="20",             # отступ от границ до содержимого по горизонтали
#              pady="8",              # отступ от границ до содержимого по вертикали
#              font="16",              # высота шрифта
#
#              command = lambda :start()
#              ).pack()
#
# Button(text="Пауза",          # текст кнопки
#              background="#555",     # фоновый цвет кнопки
#              foreground="white",     # цвет текста
#              padx="20",             # отступ от границ до содержимого по горизонтали
#              pady="8",              # отступ от границ до содержимого по вертикали
#              font="16",              # высота шрифта
#              command = lambda : stop()
#              ).pack()
#
# Label(root, text = u'Введите скорость от 1 до 25').place(x = 5 , y = 0)
# Speed_V = Entry(root, width = 10,background = "grey",foreground="white",)
# Speed_V.place(x = 55, y = 20)
# Speed_V.insert(0, '20')
#
# Label(root, text = u'Введите угол ').place(x = 5 , y = 40)
# angle = Entry(root, width = 10,background = "grey",foreground="white",)
# angle.place(x = 55, y = 60)
# angle.insert(0,'20')
#
# Label(root, text = u'Введите начальную точку :').place(x = 320 , y = 0)
# Label(root, text = 'x          y').place(x = 380 , y = 15)
# B_X = Entry(root, width = 4,background = "grey",foreground="white",)
# B_X.place(x = 370, y = 35)
# B_X.insert(0,'150')
#
# B_Y = Entry(root, width = 4,background = "grey",foreground="white",)
# B_Y.place(x = 410, y = 35)
# B_Y.insert(0,'250')
# Button(text = 'ok',background = "#555",foreground="white", command = lambda : button_ok()).place(x = 450, y = 30)
# Button(text = 'ok',background = "#555",foreground="white", command = lambda : button_ok_fi()).place(x = 130, y = 55)
#
#
#
# #область анимации
# c = Canvas(root, width=WIDTH, height=HEIGHT, background="gray")
# c.pack()
#
# # левая линия
# c.create_oval(WIDTH/2 - Radius,
#                 HEIGHT / 2 - Radius,
#                 WIDTH / 2 + Radius,
#                 HEIGHT / 2 + Radius,
#                     fill="white",
#                     outline="black",
#                     width=2)
# c.create_oval(WIDTH/2 - radius,
#                 HEIGHT / 2 - radius,
#                 WIDTH / 2 + radius,
#                 HEIGHT / 2 + radius,
#                     fill="white",
#                     outline="black",
#                     width=2)
#
#
# def K(Radian) :
#     return math.tan(Radian)
#
# def B(Radian,x0,y0) :
#     return (y0 - K(Radian) *x0)
#
# def XY(Radian,x0,y0) :
#     b = 2*K(Radian)*(B(Radian,x0,y0) - HEIGHT/2) - 2 * WIDTH/2
#     a = (1 + K(Radian)**2)
#     c = (B(Radian,x0,y0) - HEIGHT/2)**2 + (WIDTH/2)**2 - Radius**2
#     Det = b ** 2 - 4 * a * c
#     X1 = (-b + Det**(1/2))/(2*a)
#     Y1 = K(Radian)*X1 + B(Radian,x0,y0)
#     X2 = (-b - Det**(1/2))/(2*a)
#     Y2 = K(Radian)*X2 + B(Radian,x0,y0)
#     # X1 = (-K(Radian)*B(Radian,x0,y0) + ((Radius**2 + Radius**2 * K(Radian)**2 - B(Radian,x0,y0)**2)**(1/2)))/(2*(1 + K(Radian)**2))
#     # Y1 = K(Radian) * X1  + B(Radian,x0,y0)
#     # X2 = (-K(Radian)*B(Radian,x0,y0) - ((Radius**2 + Radius**2 * K(Radian)**2 - B(Radian,x0,y0)**2)**(1/2)))/(2*(1 + K(Radian)**2))
#     # Y2 = K(Radian) * X2  + B(Radian,x0,y0)
#     return X1,Y1,X2,Y2
#
# def xy(Radian,x0,y0) :
#     b = 2*K(Radian)*(B(Radian,x0,y0) - HEIGHT/2) - 2 * WIDTH/2
#     a = (1 + K(Radian)**2)
#     c = (B(Radian,x0,y0) - HEIGHT/2)**2 + (WIDTH/2)**2 - radius**2
#     Det = b ** 2 - 4 * a * c
#     x1 = (-b + Det**(1/2))/(2*a)
#     y1 = K(Radian)*X1 + B(Radian,x0,y0)
#     x2 = (-b - Det**(1/2))/(2*a)
#     y2 = K(Radian)*X2 + B(Radian,x0,y0)
#     # x1 = (-K(Radian)*B(Radian,x0,y0) + ((radius**2 + radius**2 * K(Radian)**2 - B(Radian,x0,y0)**2)**(1/2)))/(1 + K(Radian)**2)
#     # y1 = K(Radian) * x1  + B(Radian,x0,y0)
#     # x2 = (-K(Radian)*B(Radian,x0,y0) - ((radius**2 + radius**2 * K(Radian)**2 - B(Radian,x0,y0)**2)**(1/2)))/(1 + K(Radian)**2)
#     # y2 = K(Radian) * x2  + B(Radian,x0,y0)
#     return x1,y1,x2,y2
#
# def move_ball(Radian):
#
#     c.move(BALL,Speed*math.cos(Radian),Speed*math.sin(Radian))
#
# def function ():
#     global k,b,X1,Y1,X2,Y2,x1,y1,x2,y2,x0,y0,Radian
#     # определяем координаты сторон мяча и его центра
#     ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
#     ball_centerY = (ball_top + ball_bot) / 2
#     ball_centerX = (ball_left + ball_right) / 2
#     #print(ball_centerX,ball_centerY,"X1:",X1, Y1, 'X2:',X2, Y2,'x1:',x1,y1,'x2:',x2,y2,'k:',k,"b:",b)
#     if (radius**2 + radius**2 * k**2 - b**2) < 0 :
#         if (min(math.fabs(math.tan(Radian) - ((Y1-y0)/(X1-x0)) ),math.fabs(math.tan(Radian) - ((Y2-y0)/(X2-x0)))) == math.fabs(math.tan(Radian) - ((Y1-y0)/(X1-x0)))
#             and ((ball_centerX - WIDTH/2)**2 + (ball_centerY - HEIGHT/2)**2)**(1/2) >= (Radius - BALL_RADIUS )):
#             a = math.atan((Y1 - y0) / (X1 - x0))
#             d = math.atan((Y1 - HEIGHT / 2) / (X1 - WIDTH / 2))
#             Radian = Radian + pi + 2 * (d - a)
#             x0,y0 = X1,Y1
#             X1,Y1,X2,Y2 = XY(Radian,x0,y0)
#             k = K(Radian)
#             b = B(Radian,x0,y0)
#             # if(min(math.fabs(math.tan(Radian) - ((Y1-y0)/(X1-x0)) ),math.fabs(math.tan(Radian) - ((Y2-y0)/(X2-x0)))) == math.fabs(math.tan(Radian) - ((Y1-y0)/(X1-x0)))):
#             #     Radian = math.tan((Y1-y0)/(X1-x0))
#             # else :
#             #     Radian = math.tan((Y2-y0)/(X2-x0))
#             print(x0, y0, 'big X1')
#         elif (min(math.fabs(math.tan(Radian) - ((Y1-y0)/(X1-x0)) ),math.fabs(math.tan(Radian) - ((Y2-y0)/(X2-x0)))) == math.fabs(math.tan(Radian) - ((Y2-y0)/(X2-x0)))
#             and ((ball_centerX - WIDTH/2)**2 + (ball_centerY - HEIGHT/2)**2)**(1/2) >= (Radius - BALL_RADIUS )):
#             a = math.atan((Y2 - y0) / (X2 - x0))
#             d = math.atan((Y2 - HEIGHT / 2) / (X2 - WIDTH / 2))
#             Radian = Radian + pi + 2 * (d - a)
#             x0,y0 = X2,Y2
#             X1,Y1,X2,Y2 = XY(Radian,x0,y0)
#             k = K(Radian)
#             b = B(Radian,x0,y0)
#             # if(min(math.fabs(math.tan(Radian) - ((Y1-y0)/(X1-x0))),math.fabs(math.tan(Radian) - ((Y2-y0)/(X2-x0)))) == math.fabs(math.tan(Radian) - ((Y1-y0)/(X1-x0)) )):
#             #     Radian = math.tan((Y1-0)/(X1-x0))
#             # else :
#             #     Radian = math.tan((Y2-y0)/(X2-x0))
#             print(x0, y0, 'big X2')
#         else:
#             Radian = Radian
#
#     else :
#         if (((((x1-x0)**2 + (y1 - y0)**2)**(1/2)) >= (((x2-x0)**2 + (y2 - y0)**2)**(1/2)))
#                 and ((ball_centerX - WIDTH/2)**2 + (ball_centerY - HEIGHT/2)**2)**(1/2) <= (radius + BALL_RADIUS )):
#             D = math.atan((y2 - HEIGHT / 2) / (x2 - WIDTH / 2))
#             A = math.atan((y2 - y0) / (x2 - x0))
#             Radian = Radian + 2 * (D - A) - pi
#             x0 = x2
#             y0 = y2
#             X1,Y1,X2,Y2 = XY(Radian,x0,y0)
#             k = K(Radian)
#             b = B(Radian, x0, y0)
#             if (min(math.fabs(math.tan(Radian) - ((Y1 - y0) / (X1 - x0))),
#                     math.fabs(math.tan(Radian) - ((Y2 - y0) / (X2 - x0)))) == math.fabs(
#                         math.tan(Radian) - ((Y1 - y0) / (X1 - x0)))):
#                 Radian = math.tan((Y1 - y0) / (X1 - x0))
#             else:
#                 Radian = math.tan((Y2 - y0) / (X2 - x0))
#
#             print(x0, y0, 'small')
#         elif (((((x1-x0)**2 + (y1 - y0)**2)**(1/2)) < (((x2-x0)**2 + (y2 - y0)**2)**(1/2)))
#               and ((ball_centerX - WIDTH/2)**2 + (ball_centerY - HEIGHT/2)**2)**(1/2) <= (radius + BALL_RADIUS )):
#             D = math.atan((y1 - HEIGHT / 2) / (x1 - WIDTH / 2))
#             A = math.atan((y1 - y0) / (x1 - x0))
#             Radian = Radian + 2 * (D - A) - pi
#             x0 = x1
#             y0 = y1
#             X1, Y1, X2, Y2 = XY(Radian, x0, y0)
#             k = K(Radian)
#             b = B(Radian, x0, y0)
#             if (min(math.fabs(math.tan(Radian) - ((Y1 - y0) / (X1 - x0))),
#                     math.fabs(math.tan(Radian) - ((Y2 - y0) / (X2 - x0)))) == math.fabs(
#                     math.tan(Radian) - ((Y1 - y0) / (X1 - x0)))):
#                 Radian = math.tan((Y1 - y0) / (X1 - x0))
#             else:
#                 Radian = math.tan((Y2 - y0) / (X2 - x0))
#
#             print(x0, y0, 'small')
#         else :
#             Radian = Radian
#     return Radian
#
# def main():
#      Radian = function()
#      move_ball(Radian)
#
# # запускаем работу окна
# root.mainloop()
from tkinter import *
import math
WIDTH = 500
HEIGHT = 500
pi = 3.14159265359

#радиус мяча
BALL_RADIUS = 8
#радиус кругов
Radius = 200
radius = 30
#устанавливаем начальнй шаг шара
Speed = 1

# устанавливаем окно
root = Tk()
root.geometry("500x680")
root.title(" Sinai`s Billiard ")
run = False
Ball_x, Ball_y = 150,250

class Ball:
    def __init__(self, x):
        self.x = x

def worker():
    ball1 = Ball(1)
    Ball1.x, = main(ball1)
    if run:
        root.after(26 - int(V), worker) # вызываем саму себя каждые 30 миллисекунд
def start():
    global V,run
    V  = Speed_V.get()
    run = True
    root.after(0, worker)
def stop():
    global run
    run = False
def button_ok_Beta():
    global Beta
    Beta = -float(angle.get())*pi/180
    if (math.fabs(Beta - pi)<=0.005):
        Beta = -pi
    #print("Beta:",Beta)
    return Beta

def button_ok() :
    global BALL,Alpha,Ro,fi,Gamma,Beta,small_previous,Ball_x,Ball_y,R_hit,R
    Ro = float(B_Ro.get())
    R = Ro
    Alpha = -float(B_Alpha.get())*pi / 180
    if (math.fabs(Alpha - pi)<=0.005):
        Alpha = -pi
    fi = Alpha
    #print("alpha:",Alpha)
    small_previous = None
    Gamma = Alpha
    Gamma,R_hit,Beta = next_hit(Gamma,Ro,Beta)
    #RO = ((HEIGHT/2)**2 + (WIDTH/2)**2)**(1/2)
    Ball_x = Ro * math.cos(Alpha) + WIDTH/2
    Ball_y = Ro * math.sin(Alpha) + HEIGHT/2
    BALL = c.create_oval(Ball_x - BALL_RADIUS / 2,
                         Ball_y - BALL_RADIUS / 2,
                         Ball_x + BALL_RADIUS / 2,
                         Ball_y + BALL_RADIUS / 2, fill="black")

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

Label(root, text = u'Введите скорость от 1 до 25').place(x = 5 , y = 0)
Speed_V = Entry(root, width = 10,background = "grey",foreground="white",)
Speed_V.place(x = 55, y = 20)
Speed_V.insert(0, '16')

Label(root, text = u'Введите угол от -180 до 180 ').place(x = 5 , y = 40)
angle = Entry(root, width = 10,background = "grey",foreground="white",)
angle.place(x = 55, y = 60)
angle.insert(0,'110')

Label(root, text = u'Введите начальную точку :').place(x = 320 , y = 0)
Label(root, text = 'ρ      Alpha(-180,180)').place(x = 380 , y = 15)
B_Ro = Entry(root, width = 4,background = "grey",foreground="white",)
B_Ro.place(x = 370, y = 35)
B_Ro.insert(0,'100')

B_Alpha = Entry(root, width = 4,background = "grey",foreground="white",)
B_Alpha.place(x = 410, y = 35)
B_Alpha.insert(0,'-60')
Button(text = 'ok',background = "#555",foreground="white", command = lambda : button_ok()).place(x = 450, y = 30)
Button(text = 'ok',background = "#555",foreground="white", command = lambda : button_ok_Beta()).place(x = 130, y = 55)



#область анимации
c = Canvas(root, width=WIDTH, height=HEIGHT, background="gray")
c.pack()

# левая линия
c.create_oval(WIDTH/2 - Radius,
                HEIGHT / 2 - Radius,
                WIDTH / 2 + Radius,
                HEIGHT / 2 + Radius,
                    fill="white",
                    outline="black",
                    width=2)
c.create_oval(WIDTH/2 - radius,
                HEIGHT / 2 - radius,
                WIDTH / 2 + radius,
                HEIGHT / 2 + radius,
                    fill="white",
                    outline="black",
                    width=2)
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
def move_ball(Beta):

    c.move(BALL,Speed*math.cos(Beta),Speed*math.sin(Beta))

def next_hit(Gamma,R_hit,Beta):
    global small_previous,fi,ball_centerX,ball_centerY,radius,Radius,Gamma_prev,R_hit_prev

    if small_previous == None :
        Alpha = Gamma
        Gamma_prev = Alpha
        R_hit_prev = R_hit
        if ((math.fabs(pi - math.fabs(Alpha) - math.fabs(Beta) ) > math.sin((radius)/R_hit))or
                (signum(Beta) == signum(Alpha) and ((pi - math.fabs(Beta - Alpha)) > math.sin((radius) / Radius)))):
            Gamma = Beta +  math.asin((math.sin(Beta - Alpha - pi)) * (R_hit) / (Radius))
            print(Gamma,"Bef")
            Gamma = to_pi(Gamma)
            print(Gamma, "af")
            small_previous = True
            return Gamma,Radius,Beta
        else:
            print("smal None")
            print(Alpha,Beta)
            Fi = pi - Alpha + Beta
            pci = math.asin((math.sin(Fi)*(R_hit)/(radius)))
            x = pi + Fi + pci
            print(Fi," Fi ",pci," pci ",x," x " )
            Gamma = Beta - pci + pi
            print(Gamma, "Bef",Gamma/pi)
            Gamma = to_pi(Gamma)
            print(Gamma, "af")
            small_previous = True
            return Gamma,radius,Beta
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
            # Beta = pi - math.atan2((Radius * math.sin(-pi - Gamma2) - ((ball_centerY - HEIGHT/2))),
            #                        (Radius * math.cos(-pi - Gamma2) + (ball_centerX - WIDTH/2)))
            # print("B",math.atan2((Radius * math.sin(-pi - Gamma2) - ((ball_centerY - HEIGHT/2))),
            #                        (Radius * math.cos(-pi - Gamma2) - (ball_centerX - WIDTH/2))),
            #                         math.atan2((Radius * math.sin(-pi - Gamma2) - ((ball_centerY - HEIGHT/2))),
            #                        (Radius * math.cos(-pi - Gamma2) + (ball_centerX - WIDTH/2))))
            Gamma_prev = Gamma
            R_hit_prev = R_hit
            return Gamma2,Radius,Beta
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
            return Gamma2,radius,Beta
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
        return Gamma2,Radius,Beta

def main(cls):
    global fi, Gamma, Beta ,Ro,small_previous,Radius,R,R_hit,Alpha,ball_centerX,ball_centerY,Gamma_prev
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_centerY = (ball_top + ball_bot) / 2
    ball_centerX = (ball_left + ball_right) / 2
    fi = math.atan2((ball_centerY - HEIGHT/2),(ball_centerX - WIDTH/2))
    if (math.fabs(fi + pi)<=0.000002):
        fi = pi
    R = ((ball_centerX - WIDTH/2)**2 + (ball_centerY - HEIGHT/2)**2)**(1/2)
    print("fi:",fi,"Gamma:",Gamma,"R:",R,"R_hit",R_hit)
    if ((math.fabs(fi - Gamma)<=0.05) and (math.fabs(R) >= (Radius))):
        print("big")
        print("Before ","Beta:", Beta, "Gamma:",Gamma,Gamma_prev)
        Gamma,R_hit,Beta = next_hit(Gamma,R,Beta)
        print("After ","Beta:", Beta, "Gamma:", Gamma,Gamma_prev)

    elif((math.fabs(fi - Gamma)<=0.05) and (math.fabs(R) <= (radius))):
        print("small")
        print("Before ","Beta:", Beta, "Gamma:",Gamma)
        Gamma,R_hit,Beta = next_hit(Gamma,R,Beta)
        print("After ","Beta:", Beta, "Gamma:", Gamma)
    move_ball(Beta)

# запускаем работу окна
root.mainloop()