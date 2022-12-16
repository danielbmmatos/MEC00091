#-----------------------------------------------------------------------------#
#                               EQUAL INTERVAL SEARCH                         #
#                                                                             #
#-----------------------------------------------------------------------------#
# Author: Eng. Me. Daniel B M Matos
# Date  : 28/11/2022
# Last Modification: 01/11/2022
#-----------------------------------------------------------------------------#

import numpy as np


def equalInterval(funct,a, aui, ali,  d,  e, f, n):

    q = 2; 
    al = 0; 
    fa = 0; 
    aa = d; 
    fu = 0;
    au = q*d; 
    fa,n = funct(aa, n);
    fu,n = funct(au, n);

    while(fa >= fu):
            i = 0
            q = q+1;
            aa = au;
            fa = fu;
            au = q*d;
            fu,n = funct(au, n);

    al = (q-2)*d;
    aui = au;
    ali = al;
            
    while(au-al > e):

        d = d*0.1; 
        q = 2;
        aa = al+d;
        au = al+(q*d);
        fa,n = funct(aa, n);
        fu,n = funct(au, n);

        while(fa >= fu):

            q = q+1;
            aa = au;
            fa = fu

            au = al+(q*d);
            fu,n = funct(au, n);


        al = al+((q-2)*d);

    a = (au+al)/2; 
    f,n = funct(a, n); 
    i = i+5
    print(" O intervalo está entre {ali} e {aui}")
    return 
