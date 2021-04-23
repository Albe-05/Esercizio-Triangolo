import math

a = int(input())
b = int(input())
c = int(input())

#è un triangolo?
if  a < b+c and b < a+c and c < a+b and a > abs(b-c) and b > abs(a-c) and c > abs(a-b):
    print("è un triangolo")
    
    #acutangolo?
    if pow(a, 2) < pow(b, 2) + pow(c, 2) and pow(b, 2) < pow(a, 2) + pow(c, 2) and pow(c, 2) < pow(a, 2) + pow(b, 2):
        #print("è un triangolo acutangolo")
        pass
    
    #ottusangolo
    elif pow(a, 2) > pow(b, 2) + pow(c, 2) or pow(b, 2) > pow(a, 2) + pow(c, 2) or pow(c, 2) > pow(a, 2) + pow(b, 2):
        #print("è un triangolo ottusangolo")
        pass
    
    #per forza di cosa è rettangolo
    else:
        print("è un triangolo rettangolo")
    
    #equilatero  
    if a == b == c:
        print("è un triangolo equilatero")
    
    #scaleno
    elif a != b != c:
        print("è un triangolo scaleno")
    
    #isocele
    else:
        print("è un triangolo isoscele")
    
    # ref: http://www.ubimath.org/triangoli/Triangolo_UbiElearning.pdf
    # https://www.youmath.it/domande-a-risposte/view/2991-formula-di-erone-area.html
    # http://utenti.quipo.it/base5/probabil/probtria.htm
    
    print(f'Perimetro triangolo: {a+b+c}')
    
    semiperimetro = (a+b+c)/2
    print(f'Area: {math.sqrt(semiperimetro*(semiperimetro-a)*(semiperimetro-b)*(semiperimetro-c))}')
    
else:
    print("non è un triangolo")
