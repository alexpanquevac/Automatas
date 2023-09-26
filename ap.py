from sys import argv
d={}
d2={}
F=set()
programa=open(argv[1])
isPila = True
for linea in programa:
    if len(linea.split()) == 3:
        q,s,n=linea.split()
        if '*' in q:
            q=q.strip('*')
            F.add(q)
        d[q,s]=n
        isPila=False
    else:    
        q,s,a1,a2,nq=linea.split()
        if '*' in q:
            q=q.strip('*')
            F.add(q)   
        d[q,s]=a1,a2,nq     
programa.close()

def AFD(d,q0,F,cinta):
    q=q0
    for simbolo in cinta:
        q=d[q,simbolo]
    return q in F

def AP(d,q0,F,cinta):
    pila=['Z']
    q=q0
    for simbolo in cinta:
        a1,a2,q = d[q,simbolo]
        if a1 in pila and a1 != '_':
           pila.pop(-1)
        if a2 != '_' :   
            pila.append(a2) 
    print(list(reversed(pila)))        
    if len(F) == 0:
        if len(pila) == 0:
            return True
        else:
            return False
    else:
        return q in F   

mensaje={True:'Aceptada',False:'Rechazada'}

cintas=open(argv[2])
for cinta in cintas:
    cinta=cinta.strip()
    if isPila:
        print('La entrada',cinta," es ",mensaje[AP(d,'0',F,cinta)])
    else:
        print('La entrada',cinta," es ",mensaje[AFD(d,'0',F,cinta)])    
cintas.close()