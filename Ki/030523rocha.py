#representação Implícita de grafos

file = open ("grafos.txt" , "r")

grafos = {}
estado1 = {'uf' : 'Rio De Janeiro', 'Sigla' : 'RJ'}
estado2 = {'uf' : 'Píaui' , 'Sigla' : 'PI'}
file.append(estado1)
file.append(estado2)

print(file[0] ['Sigla'])
print(file[1] ['Sigla'])
print(file)