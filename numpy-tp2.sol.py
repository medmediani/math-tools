# La ligne suivante nous pernmettra d'utliser les caractere accentes dans l'affichage
# -*- coding: utf-8 -*-


import numpy as np
import time
#La ligne suivante (seed) est utilis�e pour que tous le monde aura les m�me don�es 
np. random .seed (1234)
d=np. random .rand (10)
e=np. random . randint (1 ,20,10)


###################################
## Exo 1                                                                        ##
###################################
#2 passages sur les donn�es
# Noter l'utilisation de 0.0, pour que la variable soit reelle meme si le vecteur est entier
def avg_std(v):
    a=0.0
    for x in v:
        a+=x
    a/=len(v)
    std=0.0
    for x in v:
        std+=(x-a)**2
    std/=len(v)
    return a,  np.sqrt(std)
# Un seul passage
def avg_std1(v):
    s, ss=0., 0.
    for x in v:
        s+=x
        ss+=x**2
    s, ss=s/len(v), ss/len(v)
    return s, np.sqrt(ss-s**2)

# En utilisant les fonctions de Numpy
def avg_std2(v):
    return v.mean(), v.std()
# Autre solution en utilisant lesoperations sur les arrays
# Noter l'utilisation de float, pour forcer la division r�elle. si levecteur est entier, la division sera entiere
def avg_std3(v):    
    s, ss=v.sum()/float(len(v)),(v**2).sum()/float(len(v))
    return s, np.sqrt(ss-s**2)

###################################
## Exo 2                                                                        ##
###################################
########
def median(v):
    if len(v)<2:
        return v[0]
    sv=np.sort(v)
    mid=len(v)/2
    if len(v)%2==0:
        return (sv[mid-1]+sv[mid])/2.
    else:
        return sv[mid]
    
### Version plus rapide de median
## Argpartition/partition: fait un tri partiel. On ne doit pas trier completement le vecteur, on doit seulement correctement positionner l'element au milieu
## 
def median1(v):
    if len(v)<2:
        return v[0]
    
    mid=len(v)/2
    sv=np.partition(v, mid)
    if len(v)%2==0:
        return (sv[:mid].max()+sv[mid])/2.
    else:
        return sv[mid]
    
###################################
## Exo 3                                                                        ##
###################################
def median_from_freq(vals, counts):
    
    if len(vals)<2:
        return vals[0]
    #Calculer lecumul des comptes, pour trouver la valeur au milieu
    csum=counts.cumsum()
    #La derniere valeur dans csum est le nombre total deselements
    # la moitie est lemilieu
    if csum[-1] %2==0:
        return (vals[np.searchsorted(csum, csum[-1]/2)]+vals[np.searchsorted(csum, csum[-1]/2+1)])/2.0
    else:
        return vals[np.searchsorted(csum, csum[-1]/2+1)]
        

###################################
## Exo 4                                                                        ##
###################################
########
def closest(v, x):
    #La valeur laplus proche est celle qui a la moindre difference par raport a x
    return v[np.absolute(v-x).argmin()]
###################################
## Exo 5                                                                        ##
###################################
########
def moving_avgs(v, n) :
    #lamoyennemobile implique la somme de chaque n elements consecutifs
    # On va utiliser un truc:
    # On calcule lasomme cumulative 
    # pour avoir la somme des n elements consecutifs on fait la soustraction entre chaque 2 elements eloignes den positions, dans le vecteur cumulatif
    #on divise le toout par n pour avoir la moyenne
    ret = np.cumsum(v, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    
    return ret[n-1:]/n
    
#Autresolution en utilisant une boucle
#Ajouter leselements successifs jusqua n, ensuite eliminer lesderniers qui ne sont pas utilises
def moving_avgs1(v, n):
    ret=v.copy().astype(float)
    for i in range(1, n):
        ret[:-i]+=ret[i:]        
    return ret[:-n+1]/n
    
if __name__=="__main__":
    #d=e
    print d
    ##### 
    ############# EXO 1 ###################
    #Affichages des resultats de Exo 1
    # Noter les differences dans le temps de csalcul
    # Lesfonctions donneront approximativement lememe resultat a 10^-13 pres
    # Car lamethode de calcul influe sur le cumul d'erreur.
    # en tout cas, les operations numpy sont toutes a 10^-15 pres.
    #####
    t0=time.time()
    r1= avg_std(d)
    t1=time.time()
    print r1, "Calcul� en:", t1-t0, "secondes"
    t0=time.time()
    r2= avg_std1(d)
    t1=time.time()
    
    print r2, "Calcul� en:", t1-t0, "secondes"
    
    t0=time.time()
    r3= avg_std2(d)
    t1=time.time()
    
    print r3, "Calcul� en:", t1-t0, "secondes"
    
    
    t0=time.time()
    r4= avg_std3(d)
    t1=time.time()
    
    print r4, "Calcul� en:", t1-t0, "secondes"
    
    ###### Les operations de transformation:
    ###### ----------------------------------------------
    ## On va utiliser des fonctions LAMBDA: fonctions qui sont definies lors du besoin
    ## Standardisation:
    ## Le resultat de std est toujours float, on a pas besoin de le convertir
    standardize= lambda v: (v-v.mean())/v.std()
    ## Normalisation:  Noter l'utilisation de lavaleur par defaut du parametre norm. Si norm n'est pas utilise il va prendre "l1"
    ## Le resultat de sqrt est toujours float, on a pas besoin de le convertir
    normalize=lambda v,  norm="l1":v/float(np.absolute(v).sum()) if norm=="l1" else v/np.sqrt((v**2).sum())
    ## Mis al'echelle
    scale=lambda v: (v-v.min())/float(v.max()-v.min())
    s=standardize(d) 
    print "Standardisation:",  s
    #True est equivalent a 1, False a 0, Alors lasomme dece predicat donnera le nombre des nombres negatifs
    print "Nomredenombres negatifs:",  sum(s<0)
    
    print "Normalisation L1:", normalize(d)
    print "Normalisation L2:", normalize(d, norm="l2")
    
    print "Mise al'echelle:", scale(d)
    # Examiner lasyntaxe de reduce, a chaque iteration elle recoit un element de la liste (2eme argument), applique la fonction (1er argument) au resultat precedent et l'element recu de la liste et retourne le resultat
    #La valeur initiale peut etre passee en utilisant le 3eme argument 
    # 
    print reduce(lambda v, f:f(v), [standardize, normalize, scale], d)
    ##### 
    ############# Fin EXO 1 ###################
    
    ##### 
    ############# EXO 2 ###################
    ## Peut tre le tempsd'execution sera plus long pour la version rapide
    ## C'est a cause dela taille reduite des donnees
    ## Si on prend des vecteurs de taille 1000 par exemple, la difference sera beacoup plus clair
    t0=time.time()
    m=median(d)
    t1=time.time()
    print "Mediane:", m, "Temps:", t1-t0
    ### Version partielle 
    
    t0=time.time()
    m=median1(d)
    t1=time.time()
    print "Mediane avec tri partiel:", m, "Temps:", t1-t0
    #Numpy aune fonction qui calcul la mediane. 
    t0=time.time()
    m=np.median(d)
    t1=time.time()
    print     "Median de numpy:", m, "Temps:", t1-t0
    
    ##### 
    ############# Fin EXO 2 ###################

    ##### 
    ############# EXO 3 ###################
    #Noter l'utilisation duparametre return_counts
    uvals, counts=np.unique(e,return_counts=True )
    #counts est de type entier. On doit le convertir en float, sinon,les divisions s'effectuent comme division entiere et le resultat sera 0 partout
    probs=counts.astype(float)
    #1. Transform des comptes en probabilites ==> diviser par la somme
    probs/=probs.sum()
    print uvals, counts, probs
    
    # 2. La valeur la plus frequente= l'element dont le compte est le max:
    # argmax donne l'index du maximum
    print uvals[counts.argmax()]
    #3.
   #somme 
    print e.sum(), "=",  (uvals*counts).sum()
    #moyenne
    print e.mean(), "=",  (uvals*counts).sum()/float(counts.sum())
    ##ou bien
    print e.mean(), "=",  (uvals*probs).sum()
    #ecart type
    print e.std(), "=", np.sqrt( ((uvals-(uvals*probs).sum())**2*probs).sum())
    
    #Recherche dichotomique
    # La recherche dichotomique est beaucoupsplus rapide qu'une recherche lineaire
    # Mais elle exige que le vecteur soit tri�
    #On va generer un nombre aleatoir et essayer dele trouver dans le vecteur.
    #On va repeter cette operation plusieurs fois
    msg=["n'existe pas", "existe"] #msg n'est pas vraiment util, on va l'utiliser pour l'affichage seulement
    #Noter l'utilisation de variable anonyme _, On utilise cette variable quand on n'a pas besoin d'utiliser son contenu. comme dans cet exemple
    for _ in range(10):
        i=np. random . randint (1 ,20)
        try: 
            #searchsorted, donne la position ou i peut etre insere, on doit verifier si le contenu de cette position egale a i ou non
            exists=uvals[np.searchsorted(uvals, i)]==i
            #si la valeur de i est hors les bornes, Python va generer une exception, IndexError
        except IndexError:
            exists=False
        
        print i, msg[exists], "dans le vecteur"

    #On va utiliser searchsorted aussi pour calculer la mediane a partir des frequences
    print np.median(e), "=", median_from_freq(uvals, counts)
    
    # Regenerer le vecteur
    # 
    print np.repeat(uvals, counts)
    
    # Echantillon sans ponderation
    print np.random.choice(uvals, 5, replace=False)
    
    # Echantillon avec ponderation, on tient compte des repetitions
    print np.random.choice(e, 5, replace=False)
    
    #Pour avoir leselement pairs, onpeut indexer avec un predicat
    print "Le vecteur e a", sum(e%2==0),  "elements pairs. Ilssont:", e[e%2==0]
    # De la meme maniere, les predicats peuvent ettres composes. Leselement entre 10 et 20
    print "Leselements entre 10 et 20:", e[(e<=20) & (e>=10)]
    
    ##### 
    ############# Fin EXO 3 ###################

    ##### 
    ############# EXO 4 ###################
    for _ in range(10):
        i=np. random . rand()
        print "Lavaleur de d la plus proche par rapport a", i, "est:", closest(d, i)
        
    
    ##### 
    ############# Fin EXO 4 ###################
    
    ##### 
    ############# EXO 5 ###################
    print e
    t0=time.time()
    ma=moving_avgs(e, 2)
    t1=time.time()
    print "Premiere fonction Moving Averages:", ma, "Temps:", t1-t0
    #Peut etre aussi effectue comme suit:
    
    t0=time.time()
    ma=moving_avgs1(e, 2)
    t1=time.time()
    print "Deuxieme fonction Moving Averages:", ma, "Temps:", t1-t0
