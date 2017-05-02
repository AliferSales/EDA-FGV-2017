{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Inserção em árvore AVL\n",
    "Baseado no algorítimo apresentado no livro \"Estruturas de Dados e seus algorítimos\" de Szwarcfiter, J.L. e Markenzon, L.\n",
    "\n",
    "### Implementação em Python por Alifer Sales em 01/05/2017\n",
    "alifer10@gmail.com"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def inserir_AVL(x,arv):\n",
    "    \n",
    "    def inserir_auxiliar(x,arv): # Necessário para o retorno final não conter o h.\n",
    "        # Inserção do nó\n",
    "        if arv == None: \n",
    "            arv = {'chave': x, 'bal': 0, 'esq': None, 'dir': None}\n",
    "            h = True\n",
    "            return arv,h\n",
    "\n",
    "        # Nó já existe\n",
    "        elif x == arv['chave']: \n",
    "            print(\"Já existe um nó com a chave {} na árvore.\".format(x))\n",
    "            h = False\n",
    "            return arv,h\n",
    "\n",
    "        # Busca de x por recurssão\n",
    "\n",
    "        # Quando x é menor que o nó, segue-se para a subárvore esquerda T_e\n",
    "        elif x < arv['chave']:\n",
    "            arv['esq'],h = inserir_auxiliar(x,arv['esq']) # Recurssão para percorrer T_e\n",
    "\n",
    "            # Verificação do nó (regulado ou não)\n",
    "            if h:\n",
    "                if arv['bal'] == 1:\n",
    "                    arv['bal'] = 0\n",
    "                    h = False\n",
    "\n",
    "                elif arv['bal'] == 0:\n",
    "                    arv['bal'] = -1\n",
    "\n",
    "                else: # arv['bal'] == -1 -> Nó desregulado\n",
    "                    arv,h = caso1(arv) # h(T_e) > h(T_d)\n",
    "\n",
    "            return arv,h\n",
    "\n",
    "        # Quando x é maior que o nó, segue-se para a subárvore direita T_d\n",
    "        else: # x > arv['chave']\n",
    "            arv['dir'],h = inserir_auxiliar(x,arv['dir']) # Recurssão para percorrer T_d\n",
    "\n",
    "            # Verificação do nó (regulado ou não)\n",
    "            if h:\n",
    "                if arv['bal'] == -1:\n",
    "                    arv['bal'] = 0\n",
    "                    h = False\n",
    "\n",
    "                elif arv['bal'] == 0:\n",
    "                    arv['bal'] = 1\n",
    "\n",
    "                else: # arv['bal'] == 1 -> Nó desregulado\n",
    "                    arv,h = caso2(arv) # h(T_e) < h(T_d)\n",
    "                \n",
    "        return arv,h\n",
    "    \n",
    "    return inserir_auxiliar(x,arv)[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def caso1(arv):\n",
    "    \n",
    "    u = arv['esq']\n",
    "    \n",
    "    if u['bal'] == -1: # caso 1.1 - Rotação direita\n",
    "        arv['esq'] = u['dir']\n",
    "        arv['bal'] = 0\n",
    "        u['dir'] = arv\n",
    "        nova_arv = u\n",
    "        \n",
    "    else: #u['bal'] == 1, Caso 1.2 - Rotação dupla direita\n",
    "        v = u['dir']\n",
    "        \n",
    "        #Ajuste dos balanços\n",
    "        if v['bal'] == -1: \n",
    "            u['bal'] = 0\n",
    "            arv['bal'] = 1\n",
    "        else: # v['bal'] == 1\n",
    "            u['bal'] = -1\n",
    "            arv['bal'] = 0\n",
    "        \n",
    "        u['dir'] = v['esq']\n",
    "        v['esq'] = u\n",
    "        arv['esq'] = v['dir']\n",
    "        v['dir'] = arv\n",
    "        nova_arv = v\n",
    "        \n",
    "    nova_arv['bal'] = 0\n",
    "    h = False\n",
    "    \n",
    "    return nova_arv,h"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def caso2(arv):\n",
    "    \n",
    "    u = arv['dir']\n",
    "    \n",
    "    if u['bal'] == 1: # caso 2.1 - Rotação esquerda\n",
    "        arv['dir'] = u['esq']\n",
    "        arv['bal'] = 0\n",
    "        u['esq'] = arv\n",
    "        nova_arv = u\n",
    "        \n",
    "    else: #u['bal'] == 1, Caso 2.2 - Rotação dupla esquerda\n",
    "        v = u['esq']\n",
    "        \n",
    "        #Ajuste dos balanços\n",
    "        if v['bal'] == 1: \n",
    "            u['bal'] = 0\n",
    "            arv['bal'] = -1\n",
    "        else: # v['bal'] == -1\n",
    "            u['bal'] = 1\n",
    "            arv['bal'] = 0\n",
    "        \n",
    "        u['esq'] = v['dir']\n",
    "        v['dir'] = u\n",
    "        arv['dir'] = v['esq']\n",
    "        v['esq'] = arv\n",
    "        nova_arv = v\n",
    "        \n",
    "    nova_arv['bal'] = 0\n",
    "    h = False\n",
    "    \n",
    "    return nova_arv,h"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Alguns Testes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 1. Inserção sem rebalanceamento"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bal': -1,\n",
       " 'chave': 18,\n",
       " 'dir': {'bal': 1,\n",
       "  'chave': 21,\n",
       "  'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},\n",
       "  'esq': None},\n",
       " 'esq': {'bal': -1,\n",
       "  'chave': 12,\n",
       "  'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},\n",
       "  'esq': {'bal': 0,\n",
       "   'chave': 6,\n",
       "   'dir': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None},\n",
       "   'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}}"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arv_base = None\n",
    "for chave in [18,12,21,6,15,24,3,9]:\n",
    "    arv_base = inserir_AVL(chave,arv_base)\n",
    "arv_base"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 2. Inserção com caso 1.1 - Rotação direita\n",
    "\n",
    "Acontece ao inserir um nó com chave 1 ou 4 na árvore base, por exemplo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "caso11_1 = None\n",
    "for chave in [18,12,21,6,15,24,3,9]:\n",
    "    caso11_1 = inserir_AVL(chave,caso11_1)\n",
    "    \n",
    "caso11_4 = None\n",
    "for chave in [18,12,21,6,15,24,3,9]:\n",
    "    caso11_4 = inserir_AVL(chave,caso11_4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bal': -1,\n",
       " 'chave': 18,\n",
       " 'dir': {'bal': 1,\n",
       "  'chave': 21,\n",
       "  'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},\n",
       "  'esq': None},\n",
       " 'esq': {'bal': 0,\n",
       "  'chave': 6,\n",
       "  'dir': {'bal': 0,\n",
       "   'chave': 12,\n",
       "   'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},\n",
       "   'esq': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None}},\n",
       "  'esq': {'bal': -1,\n",
       "   'chave': 3,\n",
       "   'dir': None,\n",
       "   'esq': {'bal': 0, 'chave': 1, 'dir': None, 'esq': None}}}}"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inserir_AVL(1,caso11_1)\n",
    "caso11_1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bal': -1,\n",
       " 'chave': 18,\n",
       " 'dir': {'bal': 1,\n",
       "  'chave': 21,\n",
       "  'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},\n",
       "  'esq': None},\n",
       " 'esq': {'bal': 0,\n",
       "  'chave': 6,\n",
       "  'dir': {'bal': 0,\n",
       "   'chave': 12,\n",
       "   'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},\n",
       "   'esq': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None}},\n",
       "  'esq': {'bal': 1,\n",
       "   'chave': 3,\n",
       "   'dir': {'bal': 0, 'chave': 4, 'dir': None, 'esq': None},\n",
       "   'esq': None}}}"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inserir_AVL(4,caso11_4)\n",
    "caso11_4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 3. Inserção com caso 1.2 - Rotação dupla direita\n",
    "\n",
    "Acontece ao inserir um nó com chave 7 ou 11 na árvore base, por exemplo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "caso12_7 = None\n",
    "for chave in [18,12,21,6,15,24,3,9]:\n",
    "    caso12_7 = inserir_AVL(chave,caso12_7)\n",
    "    \n",
    "caso12_11 = None\n",
    "for chave in [18,12,21,6,15,24,3,9]:\n",
    "    caso12_11 = inserir_AVL(chave,caso12_11)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bal': -1,\n",
       " 'chave': 18,\n",
       " 'dir': {'bal': 1,\n",
       "  'chave': 21,\n",
       "  'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},\n",
       "  'esq': None},\n",
       " 'esq': {'bal': 0,\n",
       "  'chave': 9,\n",
       "  'dir': {'bal': 1,\n",
       "   'chave': 12,\n",
       "   'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},\n",
       "   'esq': None},\n",
       "  'esq': {'bal': 0,\n",
       "   'chave': 6,\n",
       "   'dir': {'bal': 0, 'chave': 7, 'dir': None, 'esq': None},\n",
       "   'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}}"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inserir_AVL(7,caso12_7)\n",
    "caso12_7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bal': -1,\n",
       " 'chave': 18,\n",
       " 'dir': {'bal': 1,\n",
       "  'chave': 21,\n",
       "  'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},\n",
       "  'esq': None},\n",
       " 'esq': {'bal': 0,\n",
       "  'chave': 9,\n",
       "  'dir': {'bal': 0,\n",
       "   'chave': 12,\n",
       "   'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},\n",
       "   'esq': {'bal': 0, 'chave': 11, 'dir': None, 'esq': None}},\n",
       "  'esq': {'bal': -1,\n",
       "   'chave': 6,\n",
       "   'dir': None,\n",
       "   'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}}"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inserir_AVL(11,caso12_11)\n",
    "caso12_11"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Caso 2\n",
    "\n",
    "Para o caso 2, considere uma outra árvore como base."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bal': -1,\n",
       " 'chave': 18,\n",
       " 'dir': {'bal': 1,\n",
       "  'chave': 21,\n",
       "  'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},\n",
       "  'esq': None},\n",
       " 'esq': {'bal': 1,\n",
       "  'chave': 6,\n",
       "  'dir': {'bal': 0,\n",
       "   'chave': 12,\n",
       "   'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},\n",
       "   'esq': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None}},\n",
       "  'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arv_base2 = None\n",
    "for chave in [18,6,21,3,12,24,9,15]:\n",
    "    arv_base2 = inserir_AVL(chave,arv_base2)\n",
    "arv_base2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 4. Inserção com caso 2.1 - Rotação esquerda\n",
    "\n",
    "Acontece ao inserir um nó com chave 13 ou 16 na árvore base, por exemplo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "caso21_13 = None\n",
    "for chave in [18,6,21,3,12,24,9,15]:\n",
    "    caso21_13 = inserir_AVL(chave,caso21_13)\n",
    "    \n",
    "caso21_16 = None\n",
    "for chave in [18,6,21,3,12,24,9,15]:\n",
    "    caso21_16 = inserir_AVL(chave,caso21_16)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bal': -1,\n",
       " 'chave': 18,\n",
       " 'dir': {'bal': 1,\n",
       "  'chave': 21,\n",
       "  'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},\n",
       "  'esq': None},\n",
       " 'esq': {'bal': 0,\n",
       "  'chave': 12,\n",
       "  'dir': {'bal': -1,\n",
       "   'chave': 15,\n",
       "   'dir': None,\n",
       "   'esq': {'bal': 0, 'chave': 13, 'dir': None, 'esq': None}},\n",
       "  'esq': {'bal': 0,\n",
       "   'chave': 6,\n",
       "   'dir': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None},\n",
       "   'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}}"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inserir_AVL(13,caso21_13)\n",
    "caso21_13"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bal': -1,\n",
       " 'chave': 18,\n",
       " 'dir': {'bal': 1,\n",
       "  'chave': 21,\n",
       "  'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},\n",
       "  'esq': None},\n",
       " 'esq': {'bal': 0,\n",
       "  'chave': 12,\n",
       "  'dir': {'bal': 1,\n",
       "   'chave': 15,\n",
       "   'dir': {'bal': 0, 'chave': 16, 'dir': None, 'esq': None},\n",
       "   'esq': None},\n",
       "  'esq': {'bal': 0,\n",
       "   'chave': 6,\n",
       "   'dir': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None},\n",
       "   'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}}"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inserir_AVL(16,caso21_16)\n",
    "caso21_16"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 5. Inserção com caso 2.2 - Rotação dupla esquerda\n",
    "\n",
    "Acontece ao inserir um nó com chave 7 ou 10 na árvore base, por exemplo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "caso22_7 = None\n",
    "for chave in [18,6,21,3,12,24,9,15]:\n",
    "    caso22_7 = inserir_AVL(chave,caso22_7)\n",
    "    \n",
    "caso22_10 = None\n",
    "for chave in [18,6,21,3,12,24,9,15]:\n",
    "    caso22_10 = inserir_AVL(chave,caso22_10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bal': -1,\n",
       " 'chave': 18,\n",
       " 'dir': {'bal': 1,\n",
       "  'chave': 21,\n",
       "  'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},\n",
       "  'esq': None},\n",
       " 'esq': {'bal': 0,\n",
       "  'chave': 9,\n",
       "  'dir': {'bal': 1,\n",
       "   'chave': 12,\n",
       "   'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},\n",
       "   'esq': None},\n",
       "  'esq': {'bal': 0,\n",
       "   'chave': 6,\n",
       "   'dir': {'bal': 0, 'chave': 7, 'dir': None, 'esq': None},\n",
       "   'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}}"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inserir_AVL(7,caso22_7)\n",
    "caso22_7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bal': -1,\n",
       " 'chave': 18,\n",
       " 'dir': {'bal': 1,\n",
       "  'chave': 21,\n",
       "  'dir': {'bal': 0, 'chave': 24, 'dir': None, 'esq': None},\n",
       "  'esq': None},\n",
       " 'esq': {'bal': 0,\n",
       "  'chave': 9,\n",
       "  'dir': {'bal': 0,\n",
       "   'chave': 12,\n",
       "   'dir': {'bal': 0, 'chave': 15, 'dir': None, 'esq': None},\n",
       "   'esq': {'bal': 0, 'chave': 10, 'dir': None, 'esq': None}},\n",
       "  'esq': {'bal': -1,\n",
       "   'chave': 6,\n",
       "   'dir': None,\n",
       "   'esq': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None}}}}"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inserir_AVL(10,caso22_10)\n",
    "caso22_10"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Mais Exemplos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "a = [5, 7, 2, 3, 4, 9]\n",
    "b = [7, 5, 4, 3, 2, 9]\n",
    "c = [1, 2, 3, 4, 5, 7]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bal': 0,\n",
       " 'chave': 5,\n",
       " 'dir': {'bal': 1,\n",
       "  'chave': 7,\n",
       "  'dir': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None},\n",
       "  'esq': None},\n",
       " 'esq': {'bal': 0,\n",
       "  'chave': 3,\n",
       "  'dir': {'bal': 0, 'chave': 4, 'dir': None, 'esq': None},\n",
       "  'esq': {'bal': 0, 'chave': 2, 'dir': None, 'esq': None}}}"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arv_a = None\n",
    "for chave in a:\n",
    "    arv_a = inserir_AVL(chave,arv_a)\n",
    "arv_a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bal': 0,\n",
       " 'chave': 5,\n",
       " 'dir': {'bal': 1,\n",
       "  'chave': 7,\n",
       "  'dir': {'bal': 0, 'chave': 9, 'dir': None, 'esq': None},\n",
       "  'esq': None},\n",
       " 'esq': {'bal': 0,\n",
       "  'chave': 3,\n",
       "  'dir': {'bal': 0, 'chave': 4, 'dir': None, 'esq': None},\n",
       "  'esq': {'bal': 0, 'chave': 2, 'dir': None, 'esq': None}}}"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arv_b = None\n",
    "for chave in b:\n",
    "    arv_b = inserir_AVL(chave,arv_b)\n",
    "arv_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bal': 0,\n",
       " 'chave': 4,\n",
       " 'dir': {'bal': 1,\n",
       "  'chave': 5,\n",
       "  'dir': {'bal': 0, 'chave': 7, 'dir': None, 'esq': None},\n",
       "  'esq': None},\n",
       " 'esq': {'bal': 0,\n",
       "  'chave': 2,\n",
       "  'dir': {'bal': 0, 'chave': 3, 'dir': None, 'esq': None},\n",
       "  'esq': {'bal': 0, 'chave': 1, 'dir': None, 'esq': None}}}"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arv_c = None\n",
    "for chave in c:\n",
    "    arv_c = inserir_AVL(chave,arv_c)\n",
    "arv_c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arv_a == arv_b"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2+"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
