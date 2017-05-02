
# Inserção em árvore AVL
Baseado no algorítimo apresentado no livro "Estruturas de Dados e seus algorítimos" de Szwarcfiter, J.L. e Markenzon, L.

### Implementação em Python por Alifer Sales em 01/05/2017
alifer10@gmail.com


```python
def inserir_AVL(x,arv):
    
    def inserir_auxiliar(x,arv): # Necessário para o retorno final não conter o h.
        # Inserção do nó
        if arv == None: 
            arv = {'chave': x, 'bal': 0, 'esq': None, 'dir': None}
            h = True
            return arv,h

        # Nó já existe
        elif x == arv['chave']: 
            print("Já existe um nó com a chave {} na árvore.".format(x))
            h = False
            return arv,h

        # Busca de x por recurssão

        # Quando x é menor que o nó, segue-se para a subárvore esquerda T_e
        elif x < arv['chave']:
            arv['esq'],h = inserir_auxiliar(x,arv['esq']) # Recurssão para percorrer T_e

            # Verificação do nó (regulado ou não)
            if h:
                if arv['bal'] == 1:
                    arv['bal'] = 0
                    h = False

                elif arv['bal'] == 0:
                    arv['bal'] = -1

                else: # arv['bal'] == -1 -> Nó desregulado
                    arv,h = caso1(arv) # h(T_e) > h(T_d)

            return arv,h

        # Quando x é maior que o nó, segue-se para a subárvore direita T_d
        else: # x > arv['chave']
            arv['dir'],h = inserir_auxiliar(x,arv['dir']) # Recurssão para percorrer T_d

            # Verificação do nó (regulado ou não)
            if h:
                if arv['bal'] == -1:
                    arv['bal'] = 0
                    h = False

                elif arv['bal'] == 0:
                    arv['bal'] = 1

                else: # arv['bal'] == 1 -> Nó desregulado
                    arv,h = caso2(arv) # h(T_e) < h(T_d)
                
        return arv,h
    
    return inserir_auxiliar(x,arv)[0]
```


```python
def caso1(arv):
    
    u = arv['esq']
    
    if u['bal'] == -1: # caso 1.1 - Rotação direita
        arv['esq'] = u['dir']
        arv['bal'] = 0
        u['dir'] = arv
        nova_arv = u
        
    else: #u['bal'] == 1, Caso 1.2 - Rotação dupla direita
        v = u['dir']
        
        #Ajuste dos balanços
        if v['bal'] == -1: 
            u['bal'] = 0
            arv['bal'] = 1
        else: # v['bal'] == 1
            u['bal'] = -1
            arv['bal'] = 0
        
        u['dir'] = v['esq']
        v['esq'] = u
        arv['esq'] = v['dir']
        v['dir'] = arv
        nova_arv = v
        
    nova_arv['bal'] = 0
    h = False
    
    return nova_arv,h
```


```python
def caso2(arv):
    
    u = arv['dir']
    
    if u['bal'] == 1: # caso 2.1 - Rotação esquerda
        arv['dir'] = u['esq']
        arv['bal'] = 0
        u['esq'] = arv
        nova_arv = u
        
    else: #u['bal'] == 1, Caso 2.2 - Rotação dupla esquerda
        v = u['esq']
        
        #Ajuste dos balanços
        if v['bal'] == 1: 
            u['bal'] = 0
            arv['bal'] = -1
        else: # v['bal'] == -1
            u['bal'] = 1
            arv['bal'] = 0
        
        u['esq'] = v['dir']
        v['dir'] = u
        arv['dir'] = v['esq']
        v['esq'] = arv
        nova_arv = v
        
    nova_arv['bal'] = 0
    h = False
    
    return nova_arv,h
```

## Alguns Testes

#### 1. Inserção sem rebalanceamento


```python
arv_base = None
for chave in [18,12,21,6,15,24,3,9]:
    arv_base = inserir_AVL(chave,arv_base)
arv_base
```




    {'bal': -1,
     'chave': 18,
     'dir': {'bal': 1,
      'chave': 21,
      'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},
      'esq': None},
     'esq': {'bal': -1,
      'chave': 12,
      'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},
      'esq': {'bal': 0,
       'chave': 6,
       'dir': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None},
       'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}}



#### 2. Inserção com caso 1.1 - Rotação direita

Acontece ao inserir um nó com chave 1 ou 4 na árvore base, por exemplo.


```python
caso11_1 = None
for chave in [18,12,21,6,15,24,3,9]:
    caso11_1 = inserir_AVL(chave,caso11_1)
    
caso11_4 = None
for chave in [18,12,21,6,15,24,3,9]:
    caso11_4 = inserir_AVL(chave,caso11_4)
```


```python
inserir_AVL(1,caso11_1)
caso11_1
```




    {'bal': -1,
     'chave': 18,
     'dir': {'bal': 1,
      'chave': 21,
      'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},
      'esq': None},
     'esq': {'bal': 0,
      'chave': 6,
      'dir': {'bal': 0,
       'chave': 12,
       'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},
       'esq': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None}},
      'esq': {'bal': -1,
       'chave': 3,
       'dir': None,
       'esq': {'bal': 0, 'chave': 1, 'dir': None, 'esq': None}}}}




```python
inserir_AVL(4,caso11_4)
caso11_4
```




    {'bal': -1,
     'chave': 18,
     'dir': {'bal': 1,
      'chave': 21,
      'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},
      'esq': None},
     'esq': {'bal': 0,
      'chave': 6,
      'dir': {'bal': 0,
       'chave': 12,
       'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},
       'esq': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None}},
      'esq': {'bal': 1,
       'chave': 3,
       'dir': {'bal': 0, 'chave': 4, 'dir': None, 'esq': None},
       'esq': None}}}



#### 3. Inserção com caso 1.2 - Rotação dupla direita

Acontece ao inserir um nó com chave 7 ou 11 na árvore base, por exemplo.


```python
caso12_7 = None
for chave in [18,12,21,6,15,24,3,9]:
    caso12_7 = inserir_AVL(chave,caso12_7)
    
caso12_11 = None
for chave in [18,12,21,6,15,24,3,9]:
    caso12_11 = inserir_AVL(chave,caso12_11)
```


```python
inserir_AVL(7,caso12_7)
caso12_7
```




    {'bal': -1,
     'chave': 18,
     'dir': {'bal': 1,
      'chave': 21,
      'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},
      'esq': None},
     'esq': {'bal': 0,
      'chave': 9,
      'dir': {'bal': 1,
       'chave': 12,
       'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},
       'esq': None},
      'esq': {'bal': 0,
       'chave': 6,
       'dir': {'bal': 0, 'chave': 7, 'dir': None, 'esq': None},
       'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}}




```python
inserir_AVL(11,caso12_11)
caso12_11
```




    {'bal': -1,
     'chave': 18,
     'dir': {'bal': 1,
      'chave': 21,
      'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},
      'esq': None},
     'esq': {'bal': 0,
      'chave': 9,
      'dir': {'bal': 0,
       'chave': 12,
       'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},
       'esq': {'bal': 0, 'chave': 11, 'dir': None, 'esq': None}},
      'esq': {'bal': -1,
       'chave': 6,
       'dir': None,
       'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}}



## Caso 2

Para o caso 2, considere uma outra árvore como base.


```python
arv_base2 = None
for chave in [18,6,21,3,12,24,9,15]:
    arv_base2 = inserir_AVL(chave,arv_base2)
arv_base2
```




    {'bal': -1,
     'chave': 18,
     'dir': {'bal': 1,
      'chave': 21,
      'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},
      'esq': None},
     'esq': {'bal': 1,
      'chave': 6,
      'dir': {'bal': 0,
       'chave': 12,
       'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},
       'esq': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None}},
      'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}



#### 4. Inserção com caso 2.1 - Rotação esquerda

Acontece ao inserir um nó com chave 13 ou 16 na árvore base, por exemplo.


```python
caso21_13 = None
for chave in [18,6,21,3,12,24,9,15]:
    caso21_13 = inserir_AVL(chave,caso21_13)
    
caso21_16 = None
for chave in [18,6,21,3,12,24,9,15]:
    caso21_16 = inserir_AVL(chave,caso21_16)
```


```python
inserir_AVL(13,caso21_13)
caso21_13
```




    {'bal': -1,
     'chave': 18,
     'dir': {'bal': 1,
      'chave': 21,
      'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},
      'esq': None},
     'esq': {'bal': 0,
      'chave': 12,
      'dir': {'bal': -1,
       'chave': 15,
       'dir': None,
       'esq': {'bal': 0, 'chave': 13, 'dir': None, 'esq': None}},
      'esq': {'bal': 0,
       'chave': 6,
       'dir': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None},
       'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}}




```python
inserir_AVL(16,caso21_16)
caso21_16
```




    {'bal': -1,
     'chave': 18,
     'dir': {'bal': 1,
      'chave': 21,
      'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},
      'esq': None},
     'esq': {'bal': 0,
      'chave': 12,
      'dir': {'bal': 1,
       'chave': 15,
       'dir': {'bal': 0, 'chave': 16, 'dir': None, 'esq': None},
       'esq': None},
      'esq': {'bal': 0,
       'chave': 6,
       'dir': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None},
       'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}}



#### 5. Inserção com caso 2.2 - Rotação dupla esquerda

Acontece ao inserir um nó com chave 7 ou 10 na árvore base, por exemplo.


```python
caso22_7 = None
for chave in [18,6,21,3,12,24,9,15]:
    caso22_7 = inserir_AVL(chave,caso22_7)
    
caso22_10 = None
for chave in [18,6,21,3,12,24,9,15]:
    caso22_10 = inserir_AVL(chave,caso22_10)
```


```python
inserir_AVL(7,caso22_7)
caso22_7
```




    {'bal': -1,
     'chave': 18,
     'dir': {'bal': 1,
      'chave': 21,
      'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},
      'esq': None},
     'esq': {'bal': 0,
      'chave': 9,
      'dir': {'bal': 1,
       'chave': 12,
       'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},
       'esq': None},
      'esq': {'bal': 0,
       'chave': 6,
       'dir': {'bal': 0, 'chave': 7, 'dir': None, 'esq': None},
       'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}}




```python
inserir_AVL(10,caso22_10)
caso22_10
```




    {'bal': -1,
     'chave': 18,
     'dir': {'bal': 1,
      'chave': 21,
      'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},
      'esq': None},
     'esq': {'bal': 0,
      'chave': 9,
      'dir': {'bal': 0,
       'chave': 12,
       'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},
       'esq': {'bal': 0, 'chave': 10, 'dir': None, 'esq': None}},
      'esq': {'bal': -1,
       'chave': 6,
       'dir': None,
       'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}}



## Mais Exemplos


```python
a = [5, 7, 2, 3, 4, 9]
b = [7, 5, 4, 3, 2, 9]
c = [1, 2, 3, 4, 5, 7]
```


```python
arv_a = None
for chave in a:
    arv_a = inserir_AVL(chave,arv_a)
arv_a
```




    {'bal': 0,
     'chave': 5,
     'dir': {'bal': 1,
      'chave': 7,
      'dir': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None},
      'esq': None},
     'esq': {'bal': 0,
      'chave': 3,
      'dir': {'bal': 0, 'chave': 4, 'dir': None, 'esq': None},
      'esq': {'bal': 0, 'chave': 2, 'dir': None, 'esq': None}}}




```python
arv_b = None
for chave in b:
    arv_b = inserir_AVL(chave,arv_b)
arv_b
```




    {'bal': 0,
     'chave': 5,
     'dir': {'bal': 1,
      'chave': 7,
      'dir': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None},
      'esq': None},
     'esq': {'bal': 0,
      'chave': 3,
      'dir': {'bal': 0, 'chave': 4, 'dir': None, 'esq': None},
      'esq': {'bal': 0, 'chave': 2, 'dir': None, 'esq': None}}}




```python
arv_c = None
for chave in c:
    arv_c = inserir_AVL(chave,arv_c)
arv_c
```




    {'bal': 0,
     'chave': 4,
     'dir': {'bal': 1,
      'chave': 5,
      'dir': {'bal': 0, 'chave': 7, 'dir': None, 'esq': None},
      'esq': None},
     'esq': {'bal': 0,
      'chave': 2,
      'dir': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None},
      'esq': {'bal': 0, 'chave': 1, 'dir': None, 'esq': None}}}




```python
arv_a == arv_b
```




    True


