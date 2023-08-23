print('100 DIAS DE PYTHON para ganhar Xp.')
#Pesquisar sobre: pypy, pep, 

# O hasteg é utilizado para fazer comentários sem que sejam executados 
'''
Outra forma de comentar é utilizando as aspas, dessa forma podemos comentas linhas 
'''

#VARIÁVEIS E TIPOS EMBUTIDOS
#Tipos de bibliotescas padrão python - números, sequenciais, mapas classes pbjetos e execução
#Os Objetos nativos de python são recursos que já vêm prntos e são chamados de (Built-ins)

#TIPOS EMBUTIDOS - vamos focar em strings e numeros inteiros
#STRING = TEXTO  (Texto, Palavras)
#INT = 1, 10, 100, 1000 (número Inteiros)
#Python identifica um string porque elas sempre estão dentro de aspas simples ou duplas ''  ""
print ("Hello World!")
print ('Hello World!')

#A função print é para imprimir na tela o que quer que seja mostrado

#Print tambem funciona para números
print(1) # diferente da str ou string números não precisão de aspas 

#Quando não temos certeza do valor podemos usar a função TYPE, isso irá nos retornar qual é o tipo daquela argumento
print(type('Hello Wrold!')) #<class 'str'>
print(type(1)) #<class 'int'>
#Repare que nos retornou <class 'str'> String, <class 'int'> Inteiro

#Outro tipo que existe em python são os números de casas decimais, chamados de FLOAT ou Pontos Flutuante
print(type(1.22)) #<class 'float'>

#Se mandarmos imprimir a função abaixo vai retornar str, porque python entende que tudo dentro de aspas é string
print(type("2")) #<class 'str'>
#ou 
print(type("2.2")) #<class 'str'>

#Tambem temos os números Complexos, números complexos são definidos por 2 valores - 
# a Parte real e a parte imaginária em python é escrito na forma real + imag j.
print(type(2 + 3j)) #<class 'complex'>   (?) 

#VARIÁVEIS
#Podemos pedir ao Python para guardar algum valor que iremos utilizar em um outro momento, ele guarda em uma variável
#Um comando de atribuição (um sinal de = e o argumento) cria uma variável e atriui uma valor a ela

mensagem = 'Hello Python' #neste exemplo o nome *mensagem é a variável e *Hello Python é a atribuiçãp
print(mensagem)

numeros = 123 
print(numeros)

#neste exemplo abaixo fizemos 3 variáveis e mandamos imprimir tudo de uma vez, perceba que ficou tudo em uma linha 
texto = "Hello World"
numeros_inteiros = 123456
ponto_flutuante = 123.456
print(texto, numeros_inteiros, ponto_flutuante) 

#Neste Exemplo pedimos para imprimir trazendo os tipos que compoem as variáveis
texto = "Hello World" 
numeros_inteiros = 123456
ponto_flutuante = 123.456
print(type(texto), type(numeros_inteiros),type(ponto_flutuante))

#Perceba que ouve uma quebra de linha, isso acontece porque utilizamos o "\n" que indique que queremos quebrar a linha
texto = "Hello World"
numeros_inteiros = 123456
ponto_flutuante = 123.456
print(texto,"\n", numeros_inteiros,"\n", ponto_flutuante)

#Obs, procurar sempre usar palavras SEMANTICAS para as variaáveis
#O nome de um variável pode ser composto, pode ser longo e pode conter letras e números, 
#mas sempre iniciar por letra minusculae nunca com numeros e não podem conter caracteres especiais 
#Isso faz parte da conveção de Python, mas não podemos escrever por exemplo palavras reservadas ou palavras com espaços 
#Para Separar as palavras devemos usar _ Underscore esse padrão é chamado se Snake Case 
#Caso nomeamos uma variável incorretamente o interpretador irá acusar um erro 
'''
seunome = "Python"
print("Seu nome")

ERRO
#PS# 
C:\Ws.will\Python> & C:/Users/willa/AppData/Local/Programs/Python/Python311/python.exe c:/Ws.will/Python/AprendendoPython.py

  File "c:\Ws.will\Python\AprendendoPython.py", line 76
    seu nome = "Python"
        ^^^^
SyntaxError: invalid syntax
PS C:\Ws.will\Python>
'''
#Palavras chaves reservadas 
#and, del, from, none, true, as, elif, global, nonlocal, try, assert, else, if, not, while, break, except
# import, or, with, class, false, in, pass, yield, continue, finaly, is, raisw, def, for lambda, retorn
#Portanto não pode usar essas palavras para nomear variáveis  

#OPERADORES ARITMÉTICOS

# Adição + 
# Subtração -
# Multiplicação *
# Divisão /
# POtênciação **

#Quando digitamos uma expressão o interpretador irá resolver e nos devolver o resultado 
# Segue abeixo alguns exemplos 

print (1 + 1)
print (2 - 1)
print (3 * 2)
print (4 / 2)
print (10 ** 2)

x = 1 
y = 3
print(x + y)
print(x - y)
print(x * y)
print(y / x)
print(y ** x)

#Além desses operados temos o operador do resto da divisão representado por //

print(3 // 2) # Nesse exemplo restou 1 esse 1 é o resto da divisão

#Tambem temos o operador módulo % que resulta no resto da divisão entre dois numeros inteiros

print(7 % 3)  # 7 dividido ppor 3 é igual a 2 o resto é o 1, esse operador é bem util quando queremos saber se um numero é divisivel por outro


