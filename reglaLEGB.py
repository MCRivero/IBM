#L: Primero se busca en el ambito local de nuestra funcion
#E: Tras ello se busca en las funiones que encierran a nuestra funcion (enclosing)
#G: Luego se busca en el ambito global del modulo
#B: Finalmente se busca en el modulo builtins
#
g='g: Esta variable es de ambito Global (de modulo)'
def f1():
    e='e: Esta variable es local a f1. Enclosing a f2'
    def f2():
        l='l: Esta variable es local a f2'
        print(l,e,g, sep='\n')
    f2()
f1()
print('---------------')
g='g: Esta variable es de ambito Global (de modulo)'
def f1():
    e='e: Esta variable es local a f1. Enclosing a f2'
    def f2():
        l='l: Esta variable es local a f2'
        e='e: Tambien es local a f2'
        g='g: Tambien es local a f2'
        print(l,e,g, sep='\n')
    f2()
f1()
print('---------------')
g='g: Esta variable es de ambito Global (de modulo)'
def f1():
    e='e: Esta variable es local a f1. Enclosing a f2'
    def f2():
        l='l: Esta variable es local a f2'
        e='e: Tambien es local a f2'
        g='g: Tambien es local a f2'
        print(l,e,g, sep='\n')
    def f3():
    #    print(l)
        print(e,g, sep='\n')
    f2()
    f3()
f1()