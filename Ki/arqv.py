def principal ():
    dic = dict()
    lista = list()
    with open ("grafos.txt" , "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            lista.append(linha)
            
        print(lista)
        n = int(lista[0].split()[0])
        print(n)
        
        m = int(lista[1].split()[1])
        print(m)
       
        print(m,n)
        for k in range(1,n+1):
            dic[k] = []
        print(dic)
        i = 1
        while i <= m:
            a = int(lista[i].split()[0])
            b = int(lista[i].split()[1])
            dic[a].append(b)
            dic[b].append(a)
            i += 1
        print(f"\n{dic}")
        for k in dic:
            print(f"{k}:{dic[k]}")


    

if __name__ == "__main__":
    principal()
                 
