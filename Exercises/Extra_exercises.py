# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 22:11:25 2022

@author: JAG
"""

"""
1. Vad beraknar kommandot sqrt fran modulen math om kommandot anropas med ett nega-
tivt argument? Vilken enhet anvands pa argumentet till kommandot cos? Testa komman-
dona, men titta ocksa i dokumentationen pa sidan
https://docs.python.org/3.10/library/math.html
"""
# math.sqrt fungerar inte for negativa argument. cos raknar i radianer.

#****************************************************************************#
"""
2. Skriv f ̈oljande uttryck i Python
(a) 3.6 · 10−5
"""
# Man kan skriva 3.6*10**(-5), men det ar vanligare att skriva 3.6e-5.
#(e-5 betyder 10−5). 

"""
(b) e−2 sin(π/2)
"""
#Man brukar anv ̈anda exponentialfunktionen exp f ̈or att ber ̈akna e−2. Mitt f ̈orslag  ̈ar
from math import exp, sin, pi
exp(-2)*sin(pi/2)

"""
(c) cos^2(π/3)
"""
from math import cos, pi
cos(pi/3)**2

"""
(d) e^(−x2−y2) , om x = 1/2 och y = π/3
"""
from math import pi, exp
x=1/2
y=pi/3
exp(-x**2-y**2)

#***********************************************************#
"""
3. Testa operatorerna // och % i Python. Vad skiljer // fran vanlig division / ? (Operator-
erna finns beskrivna i Pythons dokumentation. Pa sidan
https://docs.python.org/3.10/library/stdtypes.html#numeric-types-int-float-complex
finns en tabell.
"""
# Operatorn // beraknar heltaldivision och % beraknar modulo (dvs resten vid heltalsdivision).

#**********************************************************************#

"""
4. Om man bortser fran luftmotstand kan kastlangd (avstand fran utkastplats till nedslagsplats)
for ett kastat foremal beraknas med formeln
d = v20 sin(2θ0)/g
och banhojd (kastets hogsta hojd) med formeln
h = v20 sin2(θ0)/2g
dar θ0  ̈ar kastvinkeln, v0  ̈ar utkastfarten och g = 9.81 tyngdkraftsaccelerationen1. Skriv
ett program i Python som beraknar banhojden h och kastlangden d. Lat θ0 = 60◦ och
v0 = 10m/s2
"""
from math import sin, pi
g=9.81
th=60*pi/180
v0=10
d=v0**2*sin(2*th)/g
h=v0**2*sin(th)**2/(2*g)

"""
5. Anvand plot fran Matplotlib.pyplot och rita en figur som sammanbinder punkterna
(1, 0), (0, 1), (−1, 0), (0, −1), (1, 0)
i precis den ordningen. Rita sedan en ny figur som istallet sammanbinder punkterna
(1, 0),(−1, 0),(0, 1), (0, −1), (1, 0).
"""
from matplotlib.pyplot import plot
# forsta figuren
x=[1,0,-1,0,1]
y=[0,1,0,-1,0]
plot(x,y)

# andra figuren
x=[1,-1,0,0,1]
y=[0,0,1,-1,0]
plot(x,y)

"""
(Beroende pa i vilken miljo du arbetar. I vissa miljoer behover du anvanda kommandot
show() for att fa Python att visa figuren.)
"""


