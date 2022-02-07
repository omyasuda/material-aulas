# Condicões aninhadas e outras estruturas condicionais

# Se, senão se, senão

é comum encontraramos, além da composição das condições usando operadores lógicos, `ìf` dentro de um `ìf` ou de um `else`.
no caso de repetidos `if`, o 'else + if' é abreviado `elif`.

```python
if a == 0:
    faz_isto()
elif a == 1:
    faz_aquilo()
else:
    faz_outra_coisa()
```

# Expressões condicionais e atribuição condicional

muitas linguagens tem uma sintaxe conhecida como * operador condicional ternário * que permite escrever o que em python é conhecido como uma * expressão condicional*. esta forma de `if` é bastante usada para atribuições ou dentro de outras estruturas:

```python
n = x if cond else y
```
isso equivale a:

```python
if cond:
    n = x
else:
    n = y
```
veja um outro exemplo:

```python
a = 50 if key_pressed else 100
# A variável a passa a valer 50 se houver uma tecla pressionada
# senão, passa a valer 100
```

# Usando `or` para atribuição condicional

O operador lógico `or` retorna o valor do lado esquerdo caso este seja considerado algo 'verdadeiro', de outra forma, ele retorna o valor do lado direito(que pode ou não ser algo considerado 'falso').

em python `None`, `0` (o número zero), `""` (um * string * vazio) ou uma coleção vazia(lista, tupla, etc.) são considerados `False`. outros valores são considerados `True`.

```python
print(0 or 10)  # exibe: 10
print(10 or 0)  # exibe: 10
print(None or 10)  # exibe: 10
print(10 or None)  # exibe: 10
print(None or 0)  # exibe: 0
print(0 or None)  # exibe: None
```

por conta disso, você pode se deparar com a seguinte expressão:

```
a = a or b  # é o mesmo que: a = a if a else b
```

essa forma é bastante usada em funções com parâmetros default:

```python


def quadrado(x, y, tamanho=None):
    tamanho = tamanho or 10
    # Isso significa que se tamanho for 0 ou `None` então tamanho deve passar a valer 10:
    # Equivalente a:
    # tamanho = tamanho if tamanho else 10
    rect(x, y, tamanho, tamanho)


```

se `0` for um valor válido para o tamanho, melhor usar assim:

```python


def quadrado(x, y, tamanho=None):
    tamanho = tamanho if tamanho is not None else 10
    rect(x, y, tamanho, tamanho)


```
