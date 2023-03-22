# 173. count é um iterador sem fim (itertools)

from itertools import count

c1 = count()
c2 = count(10, 8) # o primeiro numero é o step (de quanto em quanto vai contar)
                # o segundo é o start (em qual número irá começar)
                    
# a diferença entre o count e o range, é que o count é um iterador e um iterável, porém 
# ele conta até o infinito se vc n colocar um break

print('count 1')
for i in c1:
    if i > 100:
        break
    print(i)
    
print('')

print('count 2')
for i in c2:
    if i > 100:
        break
    print(i)
