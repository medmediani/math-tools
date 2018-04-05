# La ligne suivante nous pernmettra d'utliser les caractere accentes dans l'affichage
# -*- coding: utf-8 -*-

import math
import time


################Ex1
x=int(raw_input("Donnez un entier pour tester ca parité: "))
if x % 2==0:
	print x,"est un nombre pair"
else:
	print x,"est un nombre impair"

##Autre solution
print x,"est un nombre "+ ("pair" if x%2==0 else "impair")

##Autre
print x,"est un nombre %s"%("pair" if x%2==0 else "impair")

################EX2

x=int(raw_input("Donnez entier pour calculer ca valeur absolue: "))
if x<0:
	print "Valeu absolue de",x,"est:",-x
else:
	print "Valeu absolue de",x,"est:",x
##Autre
print "Valeu absolue de",x,"est:", x if x>0 else -x

#############Ex3

x=float(raw_input("Donnez un réel x: "))
y=float(raw_input("Donnez un réel y: "))
print "Surface du cercle avec rayon",x,"est:",math.pi*x**2
print "Surface du rectangle dont les côté sont:",x,"et",y,"est:",x*y
print "Surface du cylindre dont le rayon est", x,"et la hauteur est", y,"est:",2*math.pi*x*(x+y)



#############Ex4
mois=["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]

moi_p=raw_input("Donnez le moi en cours (Un parmi (%s)): "%(" ".join(mois) ))
i=mois.index(moi_p)
if i==11:
	print "Le moi suivant est:",mois[0]
else:
	print "Le moi suivant est:",mois[i+1]
print "Solution sans if:", mois[(i+1)%12]


###############Ex5

x=float(raw_input("Donnez la coordonnée x: "))
y=float(raw_input("Donnez la coordonnée y: "))

r=math.sqrt(x*x+y*y)
theta=math.arctan(y/x)
print "Les coordonnées polaires: r=",r,"Theta=",theta


###############Ex6

t=time.time()
nsecs=int(t)
milli=t-nsecs

#print nsecs,milli
mins=nsecs/60
nsecs=nsecs%60
#print nsecs,nsecs+milli,mins
hrs=mins/60
mins=mins%60
#print hrs,mins
days=hrs/24
hrs%=24
#print days,hrs
years=days/365
days%=365
print years,days

# Utilisation de time.time()+sleep. Le temps compté sera toujours superier a la constante passée a la fonction sleep.
# Car le système passera du temps dans les appels des fonction et l'intepretation des commandes'


#############Ex7

x=int(raw_input("Donnez la base: "))
y=int(raw_input("Donnez la puissance: "))
p=x**y
p=str(p)
s=0
for c in p:
	s+=int(c)
print "Résultat:",s

##Autre sol En utilisant map et sum 
print "Résultat dans une seule ligne:",sum(map(int,str(x**y)))

###############Ex8
if delta >=0:
a=float(raw_input("Donnez a: "))
b=float(raw_input("Donnez b: "))
c=float(raw_input("Donnez c: "))
delta=b**2-4*a*c

if delta >=0:
	sol0=b+math.sqrt(delta)/2/a
	sol1=b-math.sqrt(delta)/2/a
	print "%.2f*x^2+%.2f*x+%.2f=0 a deux solutions réelles:"%(a,b,c),sol0,"et",sol1
else:
	import cmath
	
	sol0=b+cmath.sqrt(delta)/2/a
	sol1=b-cmath.sqrt(delta)/2/a
	
	print "%.2f*x^2+%.2f*x+%.2f=0 a deux solutions complexes:"%(a,b,c),sol0,"et",sol1

