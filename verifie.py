def verifie(tab):
    m2 = 0
    c=0
    for j in tab:
        for p in ['1', '2']:
            m1 = 0
            for i in j:
                if i==p:
                    m1 = m1 + 1
                if i!=p:
                    m1 = 0
                if m1 == 4:
                    #print('ligne')
                    return True
    for i in range(7):
          for v in ['1', '2']:
              m2 = 0
              for j in range(6):
                if tab[j][i] == v:
                    m2 = m2 + 1
                if tab[j][i] != v:
                    m2 = 0
                if m2 == 4:
                    #print('colonne')
                    return True
    
    for p in ['1', '2']:
        base=[0, 0]
        temp=[0, 0]
        for i in range(6):
            temp=[i for i in base]
            for n in range(i+1):
                if tab[temp[0]][temp[1]]==p:
                    c+=1
                if tab[temp[0]][temp[1]]!=p:
                    c=0
                if c==4:
                    #print('diag')
                    return True
                temp[0]-=1
                temp[1]+=1
            base[0]+=1
            c=0
        
        base=[5, 1]
        temp=[5, 1]
        for i in range(5, -1, -1):
            temp=[i for i in base]
            for n in range(i+1):
                if tab[temp[0]][temp[1]]==p:
                    c+=1
                if tab[temp[0]][temp[1]]!=p:
                    c=0
                if c==4:
                    #print('diag')
                    return True
                temp[0]-=1
                temp[1]+=1
            c=0
            base[1]+=1
            
        base=[5, 0]
        temp=[5, 0]
        for i in range(6):
            temp=[i for i in base]
            for n in range(i+1):
                if tab[temp[0]][temp[1]]==p:
                    c+=1
                if tab[temp[0]][temp[1]]!=p:
                    c=0
                if c==4:
                    #print('diag')
                    return True
                temp[0]-=1
                temp[1]-=1
            c=0
            base[1]+=1
        
        base=[5, 6]
        temp=[5, 6]
        for i in range(6, -1, -1):
            temp=[i for i in base]
            for n in range(i):
                if tab[temp[0]][temp[1]]==p:
                    c+=1
                if tab[temp[0]][temp[1]]!=p:
                    c=0
                if c==4:
                    #print('diag')
                    return True
                temp[0]-=1
                temp[1]-=1
            c=0
            base[0]-=1          
    return False