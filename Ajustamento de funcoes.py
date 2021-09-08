#Thiago dos Santos

import matplotlib.pyplot as plt
import matplotlib
from numpy import exp,linspace,multiply,sum,array,linalg,log as ln
from sympy import lambdify,var

def x_coord(ListaDePontos):
    return ListaDePontos[0]

def y_coord(ListaDePontos):
    return ListaDePontos[1]


def Lagrange(x):
    res = float(1)

    for i in range(len(ListaDePontos)):
        if i != cont:
            res = res * ((x - x_coord(ListaDePontos[i])) / (x_coord(ListaDePontos[cont]) - x_coord(ListaDePontos[i])))

    return res

def polinomio(L):
    aux=[]
    res=[]

    for i in range(n):
        aux.append(multiply(y_coord(ListaDePontos[i]),L[i]))

    soma=aux[0]

    for i in range(n):
        if i!=n-1:
            soma =[x + y for x, y in zip(soma, aux[i+1])]
        else:
            break

    return soma

def linear(ListadePontos):
    n_pontos=len(ListadePontos)
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    soma_x=0
    soma_y=0
    soma_xy=0
    soma_x2=0

    for i in range(len(ListadePontos)):

        soma_x=x_coord(ListadePontos[i])
        soma_y=y_coord(ListadePontos[i])

        l1.append(soma_x)
        l2.append(soma_y)

    soma_x=sum(l1)
    soma_y=sum(l2)

    for i in range(len(l1)):
        l3.append(l1[i]*l2[i])
        l4.append(l1[i]**2)

    soma_xy=sum(l3)
    soma_x2=sum(l4)

    mat=array([[soma_x2,soma_x],[soma_x,n_pontos]])
    vet=array([soma_xy,soma_y])

    solve = linalg.solve(mat, vet)
    a = solve[0]
    b = solve[1]
    return a,b

def exponencial(ListadePontos):
    n_pontos=len(ListadePontos)
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    soma_x=0
    soma_y=0
    soma_xy=0
    soma_x2=0

    for i in range(len(ListadePontos)):

        soma_x=x_coord(ListadePontos[i])
        soma_y=ln(y_coord(ListadePontos[i]))

        l1.append(soma_x)
        l2.append(soma_y)

    soma_x=sum(l1)
    soma_y=sum(l2)

    for i in range(len(l1)):
        l3.append(l1[i]*l2[i])
        l4.append(l1[i]**2)

    soma_xy=sum(l3)
    soma_x2=sum(l4)

    mat=array([[soma_x2,soma_x],[soma_x,n_pontos]])
    vet=array([soma_xy,soma_y])

    solve = linalg.solve(mat, vet)
    a = solve[0]
    b = solve[1]
    return a,b

menuPrincipal=0
eixo_x=linspace(-1000,1000,100000)

while menuPrincipal!=3:
    print("Selecione um método:")
    print("1-Interpolação polinomial")
    print("2-Quadrados mínimos")
    print("3-Sair")
    menuPrincipal= int(input("Digite uma opção:"))

    if menuPrincipal==1:
        menuInterpolacao=0
        cont=0
        L = []
        p = []
        ListaDePontos=[]
        n = int(input("Digite o numero de pontos desejados:"))
        if (n==1):
            print("Digite no mínimo 2 pontos")
            menuPrincipal=0


        else:
            for i in range(n):
                print("Ponto", i + 1, ":")
                print("x", "y")
                ponto = input()
                ponto = ponto.split(' ')
                ponto[0] = float(ponto[0])
                ponto[1] = float(ponto[1])
                ListaDePontos.append(ponto)

            for i in range(n):
                L.append([])
                for x1 in eixo_x:
                    L[i].append(Lagrange(x1))
                cont = cont + 1

            p = polinomio(L)

            while menuInterpolacao!=3:
                print("1-Exibir método")
                print("2-Verificar sua função")
                print("3-Voltar")
                menuInterpolacao=int(input("Digite uma opção:"))

                if menuInterpolacao==1:
                    '''
                    for i in range(n):
                        plt.plot(eixo_x,L[i],"black") #Lagrange
                    '''
                    for i in range(n):
                        plt.plot(x_coord(ListaDePontos[i]), y_coord(ListaDePontos[i]), "go")
                    plt.plot(eixo_x, p[:100000], "red")
                    plt.axis([-50, 50, -50, 50])
                    plt.suptitle("Interpolação polinomial")
                    plt.show()

                    menuInterpolacao=0

                elif menuInterpolacao==2:
                    entrada=input("Digite sua função:")
                    x=var("x")
                    f=lambdify(x,entrada,"numpy")

                    '''
                    for i in range(n):
                        plt.plot(eixo_x,L[i],"black") #Lagrange
                    '''

                    for i in range(n):
                        plt.plot(x_coord(ListaDePontos[i]), y_coord(ListaDePontos[i]), "go")
                    plt.plot(eixo_x, p[:100000], "red")
                    plt.plot(eixo_x,f(eixo_x),"blue")
                    plt.axis([-50, 50, -50, 50])
                    plt.suptitle("Interpolação polinomial vs função")
                    plt.show()

                    menuInterpolacao=0

                elif menuInterpolacao==3:
                    L.clear()
                    p.clear()
                    ListaDePontos.clear()
                    cont=0

            menuPrincipal=0

    elif menuPrincipal==2:
        menuQuadrados = 0
        ListaDePontos = []
        n = int(input("Digite o numero de pontos desejados:"))

        if(n==1):
            print("Digite no mínimo 2 pontos")
            menuPrincipal=0

        else:
            for i in range(n):
                print("Ponto", i + 1, ":")
                print("x", "y")
                ponto = input()
                ponto = ponto.split(' ')
                ponto[0] = float(ponto[0])
                ponto[1] = float(ponto[1])
                ListaDePontos.append(ponto)

            while menuQuadrados!=4:

                print("1-Linear")
                print("2-Exponencial")
                print("3-Linear vs Exponencial")
                print("4-Voltar")
                menuQuadrados=int(input("Digite uma opção:"))

                if menuQuadrados==1:
                    menuLin=0
                    a, b = linear(ListaDePontos)
                    print("a linear:",a)
                    print("b linear:",b)
                    reta=a*eixo_x+b

                    while menuLin!=3:
                        print("1-Exibir método")
                        print("2-Verificar sua função")
                        print("3-Voltar")
                        menuLin = int(input("Digite uma opção:"))

                        if menuLin==1:
                            for i in range(n):
                                plt.plot(x_coord(ListaDePontos[i]), y_coord(ListaDePontos[i]), "go")

                            plt.plot(eixo_x,reta, "red")
                            plt.axis([-50, 50, -50, 50])
                            plt.suptitle("Ajustamento Linear")
                            plt.show()
                            menuLin=0

                        elif menuLin==2:
                            entrada = input("Digite sua função:")
                            x = var("x")
                            f = lambdify(x, entrada, "numpy")

                            for i in range(n):
                                plt.plot(x_coord(ListaDePontos[i]), y_coord(ListaDePontos[i]), "go")

                            plt.plot(eixo_x, reta, "red")
                            plt.plot(eixo_x,f(eixo_x),"blue")
                            plt.axis([-50, 50, -50, 50])
                            plt.suptitle("Ajustamento Linear vs Função")
                            plt.show()
                            menuLin=0

                    menuQuadrados=0

                elif menuQuadrados==2:
                    menuExp=0
                    a,b=exponencial(ListaDePontos)
                    print("a exponencial:",a)
                    print("b exponencial:",b)
                    funcao = exp(b)*exp(a*eixo_x)

                    while menuExp!=3:
                        print("1-Exibir método")
                        print("2-Verificar sua função")
                        print("3-Voltar")
                        menuExp = int(input("Digite uma opção:"))

                        if menuExp==1:
                            for i in range(n):
                                plt.plot(x_coord(ListaDePontos[i]), y_coord(ListaDePontos[i]), "go")

                            plt.plot(eixo_x, funcao, "red")
                            plt.axis([-50, 50, -50, 50])
                            plt.suptitle("Ajustamento Exponencial")
                            plt.show()
                            menuExp=0

                        elif menuExp==2:
                            entrada = input("Digite sua função:")
                            x = var("x")
                            f = lambdify(x, entrada, "numpy")

                            for i in range(n):
                                plt.plot(x_coord(ListaDePontos[i]), y_coord(ListaDePontos[i]), "go")

                            plt.plot(eixo_x, funcao, "red")
                            plt.axis([-50, 50, -50, 50])
                            plt.plot(eixo_x,f(eixo_x),"blue")
                            plt.suptitle("Ajustamento Exponencial vs Função")
                            plt.show()
                            menuExp=0

                    menuQuadrados=0

                elif menuQuadrados==3:
                    a1,b1=linear(ListaDePontos)
                    a2,b2=exponencial(ListaDePontos)
                    print("a linear:",a1)
                    print("b linear:",b1)
                    print("a exponencial:",a2)
                    print("b exponencial:",b2)
                    f1=a1*eixo_x+b1
                    f2=exp(b2)*exp(a2*eixo_x)

                    for i in range(n):
                        plt.plot(x_coord(ListaDePontos[i]), y_coord(ListaDePontos[i]), "go")

                    plt.plot(eixo_x, f1, "red")
                    plt.plot(eixo_x, f2, "blue")
                    plt.axis([-50, 50, -50, 50])
                    plt.suptitle("Ajustamento Linear vs Ajustamento Exponencial")
                    plt.show()

                    menuQuadrados=0

            menuPrincipal=0
