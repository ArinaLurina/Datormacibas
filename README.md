# Datormacibas kursa elektroniskā klāde

CTRL + ALT + T - atvēras loga "Terminal"

CTRL + SHIFT + T - atvēras papildloga logā "Terminal"

U + TAB x2 - komandu saraksts

CTRL + L - nodzēst visu logā

________________________________________

12.09.2018

uname - command

man uname - print certain system information

uname -a - print all information, in the following order

echo $0 - bash / shell language or a 'friendly'one sh - 'unfriendly'shell language

whoami - prints the effective user ID

who - reports which users are logged in to the system

pwd - prints the name of the working directory

ls - is a Linux shell command that lists directory contents of files and directories

ls -l - list with long format - show permissions

ls -a - list all files including hidden file starting with '.'

ls -ls - list with long format with file size

ls -la - list long format including hidden files

history - a history command



________________

Datormācība (pamatkurss)
Laboratorijas darbs L1BH
3
# 1B3.py Programma grafiskai kompleksā skaitļa attēlošanai polārās koordinātās

from matplotlib.pyplot import figure, show
from math import pi
fig = figure()

# izveido sagatavi grafikam
ax = fig.add_subplot(111, polar=True) # zīmējums būs polārās koordinātās
theta = [30,60]
# leņķis grados (komplekso skaitļu argumenti)
theta = [i*pi/180 for i in theta]     # leņķi pārveido: grad/rad
r = [1.,2.]

# radiuss (komplekso skaitļu moduļi)
ax.bar(theta,r, width=0.01)

# radiuss tiek zīmēts ar sektora platumu 0.01
show()

# Zīmējumu parāda
RTU ETF EPK, 2013. gada rudens
sastādīja: V.Zagorskis
Datormācība (pamatkurss)
Laboratorijas darbs L1BH
4
""""
Python instrukciju fragmenti darbam ar kompleksajiem skaitļiem.
Autors: Viktors Zagorksis, ETF, RTU. 2010
Ja interesē kvadrātskane no '-1', tiek iekļauta bibliotēka 'cmath'
No tās pašas bibliotēkas iekļauj funkciju atan2() - k.s. argumenta aprēķinam
un funkciju exp() - k.s. izteikšanai pēc Euler izteiksmes:
r*e^{j*\phi} = r*(cos(\phi)+j*sin(\phi))
Funkcija abs() , kas noderīga k.s. moduļa aprēķinam, ir standarta funkciju izvēlnē
"""
>>> from cmath import sqrt
>>> sqrt(-1)
1j
>>> sqrt(-1)*sqrt(-1)
(-1+0j)
>>> sqrt(-1)*sqrt(-1)*sqrt(-1)
-1j
>>> sqrt(-1)*sqrt(-1)*sqrt(-1)*sqrt(-1)
(1-0j)
>>> sqrt(-1)*sqrt(-1)*sqrt(-1)*sqrt(-1)*sqrt(-1)
1j
# Definējam kompleksu skaitli:
>>> z = 3+4j
# Kompleksa skaitļa reālā daļa:
>>> z.real
3.0
# Kompleksa skaitļa nereālā daļa:
>>> z.imag
4.0
# Kompleksa skaitļa z=a+bj,
# kas attēlots Arganda diagrammā,
# (hipotenūza I.jā kvadrantā) - vektora 'r' garums # polārās koordinātās:
>>> abs(z)
5.0
# Kompleksa skaitļa z=a+bj,
# kas attēlots Arganda diagrammā,
# (hipotenūzas I.jā kvadrantā) - vektora 'r'
# leņķis ar 0 rad leņķi polārās koordinātās:
>>> from math import atan2
>>> atan2(z.imag, z.real)
0.92729521800161219
# Klasiskais atan strādā tikai tad,
# ja reālā daļa !=0
>>> from cmath import atan
>>> atan(z.imag/z.real)
(0.92729521800161219+0j)
RTU ETF EPK, 2013. gada rudens
sastādīja: V.Zagorskis
Datormācība (pamatkurss)
Laboratorijas darbs L1BH
5
>>> atan(7/0)
Traceback (most recent call last):
File "<pyshell#19>", line 1, in <module>
atan(7/0)
ZeroDivisionError: integer division or modulo by zero
# Tā paša kompleksā skaitļa fāze
# ar atan2() ir aprēķināma pareizi(šoreiz 90 gradi) :
>>> atan2(7, 0)
1.5707963267948966
# Vēl viena kompleksā skaitļa fāzes aprēķina metode:
>>> import cmath
>>> cmath.phase(z)
0.92729521800161219
# Kompleksi saistītais skaitlis iegūstams ar metodi:
>>> z.conjugate()
(3-4j)
# Kompleksā skaitļa un tā kompleksi saistītā skaitļa reizinājums ir reāls skaitlis:
>>> z*z.conjugate()
(25+0j)
# Kompleksā skaitļa un tā kompleksi saistītā skaitļa summa ir reāls skaitlis
>>> z+z.conjugate()
(6+0j)
# Kompleksā skaitļa un tā kompleksi saistītā skaitļa starpība ir nereāls skaitlis
>>> z-z.conjugate()
8j
# Kompleksā skaitļa un tā kompleksi saistītā skaitļa dalījums ir komplekss skaitlis
>>> z/z.conjugate()
(-0.28000000000000003+0.95999999999999996j)
# Kompleksais skaitlis exponenciālā formā 45 grad leņķim:
>>> cmath.exp(1j*3.14159/4)
(0.70710725027922627+0.70710631209355757j)
# Cita moduļa (r=3, \phi=pi/4 ) gadījumam:
>>> 3*cmath.exp(1j*3.14159/4)
(2.1213217508376787+2.1213189362806726j)
# Komplekso skaitli var izveidot, ja dotas tā reālās un nereālās daļas:
>>> a = 3
>>> b = 4
>>> z = complex(a,b)
>>> z
(3+4j)
RTU E
________________________________________

17.09.2018

cd - pārvietošanas komanda

example: cd /Music

LAI PĀRIETU UZ HOME:

home/user/

example 1: cd /home/user/

example 2: cd + enter

example 3: cd + ~

~ - relatīva adrese

/ - absolūta adrese

mkdir - mapes izveidošanas komanda

rmdir - mapes dzēšanas komanda

rm - remove files or directory

echo - komanda,kura attēlo tekstu

example 1: echo "Teksts"

example 2: echo "Teksts + enter

Teksts

Teksts

"

=> Teksts

Teksts

Teksts

vai

example 3: echo -e "Teksts\nTeksts\nTeksts"

Izmantojot >> , mēs varam papildināt jau ēsošo tekstu.

example: echo "Teksts" >> fails1.txt

cat - teksta attēlošanas komanda

more vai less - citas komandas, kuras uzrada tekstu dažādos veidos

nano - komanda lai modificētu tekstu

example: nano fails1.txt

chmod - lai edītu tiesības

example: chmod 540 fails1.txt

Un vairs mēs to nevaram modificēt.

cp - komanda, kura nokopē mapi

example: cp fails1.txt fails101.txt

mv - komanda, kura pārnes failus un mapes / var nomainīt nosaukumu

example: mv 1.txt Music/ (pārnesa)

example: mv fails101.txt fails103.txt (nomainīja nosaukumu)

rm - komanda lai nodzēstu failu

example: rm Music/fails101.txt

example: rm fails*.txt (nodzēsa visus failus ar nosaukumu "fails")

________________________________________

26.09.2018

nano mans_skripts.sh - komanda, lai izveidotu savu skriptu ar Shell valodu

#!/bin/bash/ - kāds interpriators, kas nosaka mūsu darbības

$PATH - tells the shell which directories to search for executable files

PATH=$PATH:~ - Linux determines the executable search path with the $PATH environment variable

________________________________________
10.10.2018.

Python comandas

" vars() "

pieejamo objektu sarakts

" doc "

kompaktakts saraksts

" idle & "

komandu saraksts

" break" 

ends the current loop and jumps to the next statement

"continue"

ends the current iteration and jums to the top of the loop
