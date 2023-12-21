def summa3(arv1: float,arv2: float,arv3: float)->float:
 """Tagastab kolme arvu summa
 
 :param float arv1: Esimene arv
 :param float arv2: Teine arv
 :param float arv3: Kolmas arv
 :rtype: float

  """
 summa=arv1+arv2+arv3
 return summa


#1 Простейшие арифметические операции
#Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними. 
#Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
#В остальных случаях вернуть строку "Неизвестная операция".

 def arithmetic(a:float,b:float,t:str)->any:
    """Lihtne kalkulaator.
    + - liitne
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: arv
    :param float b: arv
    :param str t: aritmeetiline tehing
    :rtype: var Määramata tüüp(float or str)
    """
 if t in ["+","-","*","/"]:
      if b==0 and t=="/":
          vastus="DIV/0"
      else: 
          vastus=eval(str(a)+t+str(b))
 else:
      vastus="Tundmatu tehe"

 return vastus

#2 Високосный год
#Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
    Tagastab True, kui liigaasta ja False kui on tavaline aasta.
    :param int aasta: aasta number
    :rtype: bool tagastab loogilises formaadis tulemus
    
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v

#3 Квадрат (to chto v trojnõh skobkah nužno budet dopisat potom)
#Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения: периметр квадрата, площадь квадрата и диагональ квадрата.

def square(a:float):
    """
    """
    s=a**2
    p=4*a
    d=(2)**(1/2)*a
    return s,p,d

def square_text(a:float):
    """
    """
    s=a**2
    p=4*a
    d=(2)**(1/2)*a
    return "Pindala"+str(s)+",Ümbermõõt"+str(p)+",Läbimõõt"+str(d)
    
#4 Времена года
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (talv, kevad, suvi или sügis).
def season(param:int)->str:
    """
    """
    if 1<=param<=12:
        if param in [1,2,12]:
            v="talv"
        elif param>2 and param<6:
            v="kevad"
        elif 6<=param<=8:
            v="suvi"
        else:
            v="sügis"
    else:
        v="!!!!"
    return v

#5 Банковский вклад
#Пользователь делает вклад в размере a евро сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%.
#Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
#Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

def bank(a:float,years:int)->float:
   """
   """
   for i in range(years):
      a*=1.1
   return a

#6 Простые числа
#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.

from random import*
def is_prime(a=randint(0,1000))->bool:
 """
 """
 print(a)
 v=False
 for i in range(2,a):
   if a%i==0:
    v=True

 return v 

#7 Правильная дата
#Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем календаре, и False иначе.

def date(päev:int,kuu:int,aasta:int)->bool:
 """
 """
 if päev in range(1,31) and kuu in [1,3,5,7,8,10,12]:
    v=True 
 elif päev in range(1,29) and kuu==2 and is_year_leap(aasta):
    v=True 
 elif päev in range(1,30) and kuu in [2,4,6,9,11]:
    v=True 
 else:
    v=False
 return v

#8 XOR-шифрование
# Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая возвращает строку,
# зашифрованную путем применения функции XOR (^) над символами строки с ключом. Написать также функцию XOR_uncipher,
# которая по зашифрованной строке и ключу восстанавливает исходную строку.