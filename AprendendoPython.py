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
# Potênciação **

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

# O operador + tambem funciona com str de uma forna CONCATENADA

texto1 = "Olá " 
texto2 = "Python"
print(texto1 + texto2)

#O operador * tambem multiplica uma str

texto1 = "Python "
print(texto1 *10) #Ao multiplicar por 3 o python printa 3x a str (Caso não tivesse um espaço dentro da str as palavras ficariam grudadas)

#Métodos de strings
texto01 = "Python"
texto01.upper() #Este método retorna a primeira letra em maiúscula 
print(texto01)

texto02 = 'python texto 02'
texto2.capitalize
print(texto02)

#ENTRADA DE USUÁRIO
#Python possui uma função que captura a entrada de valor essa função chama-se INPUT 

nome = input ("Digite seu nome: ")

#Podemos fazer uma formulário para ser preenchido
#E para printar devemos passar todas as variáveis separadas por virgula
nome = input ("Digite seu nome: ")
idade = input ("Digite sua Idade: ")
endereco = input ("Digite seu Endereço: ")
cpf = input("Digite seu CPF: ")
print(nome, idade, endereco, cpf)

#Percebemos que as informação ao final não ficaram claras, pra isso devemos incluir str na função print com espaços 
# e separando as variável das str usando o oprador + para concatenar
nome = input ("Digite seu nome: \n")
idade = input ("Digite sua Idade: \n")
endereco = input ("Digite seu Endereço: \n")
cpf = input("Digite seu CPF: \n")
print(nome + " Tem " + idade + " anos de idade, mora na " + endereco + " e é portador do CPF " + cpf)

#Outra maneira mais elegante de fazer é
#dessa maneira o codigo fica mais limpo e ão é preciso quebrar a str em varias partes

nome = input ("Digite seu nome: \n")
idade = input ("Digite sua Idade: \n")
endereco = input ("Digite seu Endereço: \n")
cpf = input("Digite seu CPF: \n")
print("{} Tem {} anos de idade, mora na {} e é portador do CPF {}" .format(nome, idade, endereco, cpf,))

#Tambem podesmos usar a função format em numeros 
x = 111.2345
print('{:.2f}'.format(x)) #O :.2f arredonda diz que queremos apenas 2 casas decinais para a variável

#CONSTANTES
#True, False, None > essas tbm são palavras chave de python
#True e False são valores Booleanos que representam verdadeiro ou falso 
#python tbm tem a função bool() que retorna true ou false

1 == '1'
print (1 == '1')

2 > 1
print(2 > 1)

2 < 1
print(1 > 2)

print(bool(5 > 3))

print(bool(1 == 1))

#Quando bool() não recebe uma expressão vai retornar true ou false
print(bool(0))
print(bool(''))
print(bool(None))
print(bool(1))
print(bool(-190))
print(bool(13.5))
print(bool('Teste'))
print(bool(False))

#O none é um vaor do tipo nonetype é usado para representar uma abstenção de valor.
type(None)
print(type)

#Operadores de comparação 
# a == b         igual
# a != b         diferente  
# a < b          menor    
# a > b          maior
# a <= b         menor ou igual 
# a => b         maor ou igual 

#Outro operadores que retornam Boleanos não 

# a is b         true se a e b forem identics 
# a is not b     true se a e b não são identicos
# a in b         true se a é membro de b 
# a not in b     true se a não é menbro de b 

#Importante lembra que == e is funcionam de maneira diferente

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)

x = [0, 2, 3]
y = [1, 2, 3]
print(x == y)


x is x
print(x is x)

x is not x
print(x is not x)


#OPERADOR CONDICIONAL
#COMANDO if


numero = 42
chute = input("Digite um numero: ")
chute = int(chute) #neste caso estamos convertendo o valor de 42 para um numero inteiro qpe se não o pyhton vai entender que é uma str
if numero == chute:
  print("Vc Acertou")
else:
  print("Voce Errou.")
  #Temos que tomar cuidade pq nem toda str pode ser convertida para int
  