import pandas as pd
from sklearn import linear_model

df = pd.DataFrame()
base = pd.read_csv("database2.csv")
r_df = base.drop(labels = list(range(17360)))
base = r_df
base = base.drop("user_id", axis=1)
print("Base de dados utilizada para o TDE 2:")

print()
print("Passo 1: ")
print()
variaveisIndependentes = []
for i in base:
  if i not in variaveisIndependentes: # nao repetir a linguagem na lista
    variaveisIndependentes.append(i)
  else:
    break
print("As variáveis que estão presentes na base de dados são: \n", variaveisIndependentes)
print()
print("Cada uma dessas variáveis indica as skills de cada programador, ou seja, indica quanto o programador conhece da linguagem.")

print()
print("="*99)

print()
print("Passo 2: ")
print()
print("A minha variável dependente é: \n Python")

print()
print("="*99)

print()
print("Passo 3: ")
print()

for linguagem in base:
  if linguagem == 'assembly':
    py = base["python"]
    ass = base["assembly"]
    print("-> Coeficiente de correlação entre as linguagens Assembly e Python:")
    print(ass.corr(py))
    print()
  
  if linguagem == 'c':
    py = base["python"]
    c = base["c"]
    print("-> Coeficiente de correlação entre as linguagens C e Python:")
    print(c.corr(py))
    print()
  
  if linguagem == 'c#':
    py = base["python"]
    csharp = base["c#"]
    print("-> Coeficiente de correlação entre as linguagens C# e Python:")
    print(csharp.corr(py))
    print()
  
  if linguagem == 'c++':
    py = base["python"]
    cplus = base["c++"]
    print("-> Coeficiente de correlação entre as linguagens C++ e Python:")
    print(cplus.corr(py))
    print()

  if linguagem == 'css':
    py = base["python"]
    css = base["css"]
    print("-> Coeficiente de correlação entre as linguagens CSS e Python:")
    print(css.corr(py))
    print()

  if linguagem == 'go':
    py = base["python"]
    go = base["go"]
    print("-> Coeficiente de correlação entre as linguagens GO e Python:")
    print(go.corr(py))
    print()

  if linguagem == 'haskell':
    py = base["python"]
    has = base["haskell"]
    print("-> Coeficiente de correlação entre as linguagens Haskell e Python:")
    print(has.corr(py))
    print()

  if linguagem == 'html':
    py = base["python"]
    html = base["html"]
    print("-> Coeficiente de correlação entre as linguagens HTML e Python:")
    print(html.corr(py))
    print()

  if linguagem == 'java':
    py = base["python"]
    java = base["java"]
    print("-> Coeficiente de correlação entre as linguagens Java e Python:")
    print(java.corr(py))
    print()

  if linguagem == 'javascript':
    py = base["python"]
    javaS = base["javascript"]
    print("-> Coeficiente de correlação entre as linguagens Javascript e Python:")
    print(javaS.corr(py))
    print()

  if linguagem == 'objective-c':
    py = base["python"]
    obj = base["objective-c"]
    print("-> Coeficiente de correlação entre as linguagens Objective-c e Python:")
    print(obj.corr(py))
    print()

  if linguagem == 'php':
    py = base["python"]
    php = base["php"]
    print("-> Coeficiente de correlação entre as linguagens PHP e Python:")
    print(php.corr(py))
    print()

  if linguagem == 'powershell':
    py = base["python"]
    power = base["powershell"]
    print("-> Coeficiente de correlação entre as linguagens Powershell e Python:")
    print(power.corr(py))
    print()  
  
  if linguagem == 'ruby':
    py = base["python"]
    ruby = base["ruby"]
    print("-> Coeficiente de correlação entre as linguagens Ruby e Python:")
    print(ruby.corr(py))
    print()

  if linguagem == 'swift':
    py = base["python"]
    swift = base["swift"]
    print("-> Coeficiente de correlação entre as linguagens Swift e Python:")
    print(swift.corr(py))
    print()

  if linguagem == 'sql':
    py = base["python"]
    sql = base["sql"]
    print("-> Coeficiente de correlação entre as linguagens Sql e Python:")
    print(sql.corr(py))
    print()

print("="*99)

print()
print("Passo 4: ")
print()

print("Para obter a Regressão Linear Múltipla, devemos definir as nossas variáveis dependentes e independentes. No meu caso o X é a minha variável independente e o Y é a minha variável dependente.")
print()
print("Entao fica assim: ")
print()
print("x = base[['c', 'c#']] \ny = base['python']")
print()
print("Logo depois definimos a variavel regrecao e chamamos a função da regreção linear")
print("regrecao = linear_model.LinearRegression()")
print()
print("Então pegamos a variável regrecao e fazemos a junção das variáveis X e Y para obter a regreção")
print()
print("regrecao.fit(x, y)")
print()
print("Logo após essas etapas, podemos fazer o print do coeficiente da nossa variável regrecao.")
print()
print("Entao o resultado fica: ")
x = base[['c', 'c#']]
y = base['python']

regrecao = linear_model.LinearRegression()
regrecao.fit(x, y)

print(regrecao.coef_)

print("="*99)

print()
print("Passo 5: ")
print()
print("Coeficiente de qualidade do R")
print()
print("Com a função score, recebemos um numero que vai de 0.0 ate 1.0, quanto mais perto de 1.0 melhor")
print(regrecao.score(x, y))
