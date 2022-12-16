#-----------------------------------------------------------------------------#
#                               GOLDEN SEARCH                                 #
#                                                                             #
#-----------------------------------------------------------------------------#
# Author: Eng. Me. Daniel B M Matos
# Date  : 01/11/2022
# Last Modification: 01/11/2022
#-----------------------------------------------------------------------------#
import math

def GSsearch (F,d,acc):

    def answ (al,au,F):
        alpha = 0.5*(al + au)
        return print("Alfa:",alpha,
                     "Valor da função:",F(alpha),sep='\n')
    
    # Estabilishing initial delta    
    i  = 0                              
    gr = (math.sqrt(5)+1)/2   
    al = 0                   
    fl = F(al)
    aa = d
    fa = F(aa)
    while fa > fl:
        d *= 0.1
        i += 1

    j  = 1
    au = aa + (d*(gr**j))
    fu = F(au)

    while fa > fu:
        al = aa
        aa = au
        fl = fa
        fa = fu    
        j += 1
        au = aa + (d*(gr**j))
        fu = F(au)
        i += 1
    print("O intervalo inicial é {} e {}".format(al,au))
    ab = al + ((au - al)/gr)
    fb = F(ab)
    j = 0
    while (au - al) >= acc:
        if fa < fb:
            au = ab
            fu = fb
            ab = aa
            fb = fa
            aa = al + ((au - al)*(1 - (1/gr)))
            fa = F(aa)  
        elif fa > fb:
            al = aa
            fl = fa
            aa = ab
            fa = fb
            ab = al + ((au - al)/gr)
            fb = F(ab)
        else:
            al = aa
            fl = fa
            au = ab
            fu = fb
            aa = al + ((au - al)*(1 - (1/gr)))
            fa = F(aa)
            ab = al + ((au - al)/gr)
            fb = F(ab)
        i += 1
        j+=1
        if j==2:
            break
    return answ(al,au,F)


