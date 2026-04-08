#Programa que lê um número n inteiro qualquer e mostra na tela os n primeiros elementos da sequencia de Fibonacci.
n=int(input('Digite quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
if n == 1:
    print(t1)
elif n == 2:
    print('{} {}'.format(t1,t2), end='')
else:
    print('{} {}'.format(t1, t2), end='')
    cont = 3
    while cont <= n:
        t3 = t1 + t2
        print(' {}'.format(t3), end='')
        t1 = t2
        t2 = t3
        cont += 1
