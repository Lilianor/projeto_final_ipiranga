{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "42b3beeb",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Conexão com o MYSQL\n",
    "\n",
    "import mysql.connector as sql\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "import pandas as pd\n",
    "\n",
    "def conexao(host,user,db):\n",
    "    file = open('arquivo.txt','r')\n",
    "    lines = file.readlines()\n",
    "    file.close()\n",
    "    for line in lines:\n",
    "        senha = line\n",
    "    conn =  sql.connect(host = host,user = user,password = senha,database = db)\n",
    "    return conn\n",
    "\n",
    "conn = conexao('localhost','root','t_final')\n",
    "\n",
    "# Conexão com o CSV que o Pierre me mandou\n",
    "\n",
    "import pandas as pd\n",
    "df = pd.read_csv('dados.csv',header = None, sep = ',', encoding = 'ISO-8859-1')\n",
    "headers = df.iloc[0].values\n",
    "df.columns = headers\n",
    "df.drop(index=0, axis=0, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "64d62b5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def inserindo_tipo_cliente():\n",
    "    \n",
    "    lista_all = []\n",
    "    for i in range(1,16477):\n",
    "        lista_one = []\n",
    "        cod_tipo_cliente = df.iloc[i,0]  \n",
    "        nome_tipo_cliente= df.iloc[i,1]\n",
    "\n",
    "        \n",
    "        lista_one.append(cod_tipo_cliente)\n",
    "        lista_one.append(nome_tipo_cliente)\n",
    "        \n",
    "         \n",
    "        if lista_one not in lista_all:\n",
    "            lista_all.append(lista_one)     \n",
    "               \n",
    "        \n",
    "    #print(lista_all)\n",
    "    for item in lista_all:\n",
    "        comando = f'''\n",
    "        insert into t_final.tipo_cliente(cod_tipo_cliente,nome_tipo_cliente)\n",
    "        values \n",
    "        ({item[0]},\"{item[1]}\");\n",
    "        '''\n",
    "        \n",
    "        \n",
    "        cursor = conn.cursor()\n",
    "        cursor.execute(comando)\n",
    "        conn.commit()   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "baa7a273",
   "metadata": {},
   "outputs": [],
   "source": [
    "def inserindo_empresa():\n",
    "        \n",
    "    lista_all = []\n",
    "    for i in range(1,16477):\n",
    "        lista_one = []\n",
    "        cod_empresa = df.iloc[i,2]  \n",
    "        nome_empresa= df.iloc[i,3]\n",
    "\n",
    "        \n",
    "        lista_one.append(cod_empresa)\n",
    "        lista_one.append(nome_empresa)\n",
    "        \n",
    "         \n",
    "        if lista_one not in lista_all:\n",
    "            lista_all.append(lista_one)     \n",
    "               \n",
    "        \n",
    "    #print(lista_all)\n",
    "    for item in lista_all:\n",
    "        comando = f'''\n",
    "        insert into t_final.empresa(cod_empresa,nome_empresa)\n",
    "        values \n",
    "        ({item[0]},\"{item[1]}\");\n",
    "        '''\n",
    "        \n",
    "        \n",
    "        cursor = conn.cursor()\n",
    "        cursor.execute(comando)\n",
    "        conn.commit()   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6e6e2b59",
   "metadata": {},
   "outputs": [],
   "source": [
    "def inserindo_cliente():        \n",
    "    lista_all = []\n",
    "    for i in range(1,16477):\n",
    "        lista_one = []\n",
    "        cod_cliente = df.iloc[i,4]\n",
    "        cod_tipo_cliente = df.iloc[i,0]  \n",
    "        cod_empresa= df.iloc[i,2]\n",
    "\n",
    "        lista_one.append(cod_cliente)\n",
    "        lista_one.append(cod_tipo_cliente)\n",
    "        lista_one.append(cod_empresa)\n",
    "        \n",
    "         \n",
    "        if lista_one not in lista_all:\n",
    "            lista_all.append(lista_one)\n",
    "        \n",
    "        \n",
    "    #print(lista_all)\n",
    "    for item in lista_all:\n",
    "        comando = f'''\n",
    "        insert into t_final.cliente(cod_cliente,cod_tipo_cliente,cod_empresa)\n",
    "        values \n",
    "        ({item[0]},{item[1]},{item[2]});\n",
    "        '''\n",
    "        \n",
    "        \n",
    "        cursor = conn.cursor()\n",
    "        cursor.execute(comando)\n",
    "        conn.commit()   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "15c01b6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def inserindo_produto(): \n",
    "\n",
    "    lista_all = []\n",
    "    for i in range(1,16477):\n",
    "        lista_one = []\n",
    "        cod_produto = df.iloc[i,10]          \n",
    "        nome_produto = df.iloc[i,8]\n",
    "        marca_produto = df.iloc[i,9]\n",
    "        \n",
    "        lista_one.append(cod_produto)\n",
    "        lista_one.append(nome_produto)\n",
    "        lista_one.append(marca_produto) \n",
    "         \n",
    "        if lista_one not in lista_all:\n",
    "            lista_all.append(lista_one)     \n",
    "               \n",
    "        \n",
    "    #print(lista_all)\n",
    "    for item in lista_all:\n",
    "        comando = f'''\n",
    "        insert into t_final.produto(cod_produto,nome_produto,marca_produto)\n",
    "        values \n",
    "        ({item[0]},\"{item[1]}\",\"{item[2]}\");\n",
    "        '''\n",
    "        \n",
    "        \n",
    "        cursor = conn.cursor()\n",
    "        cursor.execute(comando)\n",
    "        conn.commit()   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a0d63b2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def inserindo_cliente_produto(): \n",
    "\n",
    "    lista_all = []\n",
    "    for i in range(1,16477):\n",
    "        lista_one = []\n",
    "        cod_produto = df.iloc[i,10]  \n",
    "        cod_cliente = df.iloc[i,4]\n",
    "\n",
    "        \n",
    "        lista_one.append(cod_produto)\n",
    "        lista_one.append(cod_cliente)\n",
    "        \n",
    "         \n",
    "        if lista_one not in lista_all:\n",
    "            lista_all.append(lista_one)     \n",
    "               \n",
    "        \n",
    "    #print(lista_all)\n",
    "    for item in lista_all:\n",
    "        comando = f'''\n",
    "        insert into t_final.cliente_produto(cod_produto,cod_cliente)\n",
    "        values \n",
    "        ({item[0]},{item[1]});\n",
    "        '''\n",
    "        \n",
    "        \n",
    "        cursor = conn.cursor()\n",
    "        cursor.execute(comando)\n",
    "        conn.commit()   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3d0bcd48",
   "metadata": {},
   "outputs": [],
   "source": [
    "def inserindo_regiao(): \n",
    "\n",
    "    lista_all = []\n",
    "    lista_cod = []\n",
    "    for i in range(1,16477):\n",
    "        lista_one = []\n",
    "        cod_municipio = df.iloc[i,7]  \n",
    "        nome_municipio = df.iloc[i,6]\n",
    "        uf = df.iloc[i,5]\n",
    "\n",
    "        \n",
    "        lista_one.append(cod_municipio)\n",
    "        lista_one.append(nome_municipio)\n",
    "        lista_one.append(uf)\n",
    "        \n",
    "         \n",
    "        if lista_one not in lista_all and cod_municipio not in lista_cod:\n",
    "            lista_all.append(lista_one)   \n",
    "            lista_cod.append(cod_municipio)\n",
    "               \n",
    "        \n",
    "    #print(lista_all)\n",
    "    for item in lista_all:\n",
    "        comando = f'''\n",
    "        insert into t_final.regiao(cod_municipio,nome_municipio,uf)\n",
    "        values \n",
    "        ({item[0]},\"{item[1]}\",\"{item[2]}\");\n",
    "        '''\n",
    "        \n",
    "        \n",
    "        cursor = conn.cursor()\n",
    "        cursor.execute(comando)\n",
    "        conn.commit()  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0e123564",
   "metadata": {},
   "outputs": [],
   "source": [
    "def inserindo_regiao_produto(): \n",
    "\n",
    "    lista_all = []\n",
    "    for i in range(1,16477):\n",
    "        lista_one = []\n",
    "        cod_municipio = df.iloc[i,7]\n",
    "        cod_produto = df.iloc[i,10]  \n",
    "        \n",
    "        \n",
    "        lista_one.append(cod_municipio)\n",
    "        lista_one.append(cod_produto)\n",
    "        \n",
    "         \n",
    "        if lista_one not in lista_all:\n",
    "            lista_all.append(lista_one)     \n",
    "               \n",
    "        \n",
    "    #print(lista_all)\n",
    "    for item in lista_all:\n",
    "        comando = f'''\n",
    "        insert into t_final.regiao_produto(cod_municipio,cod_produto)\n",
    "        values \n",
    "        ({item[0]},{item[1]});\n",
    "        '''\n",
    "        \n",
    "        \n",
    "        cursor = conn.cursor()\n",
    "        cursor.execute(comando)\n",
    "        conn.commit()   \n",
    "    \n",
    "\n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ca2947b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def inserindo_regiao_cliente(): \n",
    "\n",
    "    lista_all = []\n",
    "    for i in range(1,16477):\n",
    "        lista_one = []\n",
    "        cod_municipio = df.iloc[i,7]\n",
    "        cod_cliente = df.iloc[i,4]  \n",
    "        \n",
    "        \n",
    "        lista_one.append(cod_municipio)\n",
    "        lista_one.append(cod_cliente)\n",
    "        \n",
    "         \n",
    "        if lista_one not in lista_all:\n",
    "            lista_all.append(lista_one)     \n",
    "               \n",
    "        \n",
    "    #print(lista_all)\n",
    "    for item in lista_all:\n",
    "        comando = f'''\n",
    "        insert into t_final.regiao_cliente(cod_municipio,cod_cliente)\n",
    "        values \n",
    "        ({item[0]},{item[1]});\n",
    "        '''\n",
    "        \n",
    "        \n",
    "        cursor = conn.cursor()\n",
    "        cursor.execute(comando)\n",
    "        conn.commit()   \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "06d72b94",
   "metadata": {},
   "outputs": [],
   "source": [
    "def inserindo_venda(): \n",
    "\n",
    "    lista_all = []\n",
    "    for i in range(1,16477):\n",
    "        lista_one = []\n",
    "        id_venda = df.iloc[i,14]\n",
    "        ano_mes = df.iloc[i,11]  \n",
    "        vol_litros = df.iloc[i,12]\n",
    "        total_bruto = df.iloc[i,13]\n",
    "\n",
    "        lista_one.append(id_venda)\n",
    "        lista_one.append(ano_mes)\n",
    "        lista_one.append(vol_litros)\n",
    "        lista_one.append(total_bruto)\n",
    "        \n",
    "         \n",
    "        if lista_one not in lista_all:\n",
    "            lista_all.append(lista_one)                  \n",
    "        \n",
    "    #print(lista_all)\n",
    "    for item in lista_all:\n",
    "        comando = f'''\n",
    "        insert into t_final.venda(id_venda,ano_mes,vol_litros,total_bruto)\n",
    "        values \n",
    "        ({item[0]},{item[1]},{item[2]},{item[3]});\n",
    "        '''\n",
    "        \n",
    "        \n",
    "        cursor = conn.cursor()\n",
    "        cursor.execute(comando)\n",
    "        conn.commit()   \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d0b9345f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def inserindo_venda_regiao(): \n",
    "\n",
    "    lista_all = []\n",
    "    for i in range(1,16477):\n",
    "        lista_one = []\n",
    "        id_venda = df.iloc[i,14]\n",
    "        cod_municipio = df.iloc[i,7]        \n",
    "        \n",
    "        lista_one.append(id_venda)\n",
    "        lista_one.append(cod_municipio)     \n",
    "        \n",
    "         \n",
    "        if lista_one not in lista_all:\n",
    "            lista_all.append(lista_one)     \n",
    "               \n",
    "        \n",
    "    #print(lista_all)\n",
    "    for item in lista_all:\n",
    "        comando = f'''\n",
    "        insert into t_final.venda_regiao(id_venda,cod_municipio)\n",
    "        values \n",
    "        ({item[0]},{item[1]});\n",
    "        '''\n",
    "        \n",
    "        \n",
    "        cursor = conn.cursor()\n",
    "        cursor.execute(comando)\n",
    "        conn.commit()   \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f7e5cf44",
   "metadata": {},
   "outputs": [],
   "source": [
    "def inserindo_venda_produto(): \n",
    "\n",
    "    lista_all = []\n",
    "    for i in range(1,16477):\n",
    "        lista_one = []\n",
    "        id_venda = df.iloc[i,14]\n",
    "        cod_produto = df.iloc[i,10]        \n",
    "        \n",
    "        lista_one.append(id_venda)\n",
    "        lista_one.append(cod_produto)     \n",
    "        \n",
    "         \n",
    "        if lista_one not in lista_all:\n",
    "            lista_all.append(lista_one)     \n",
    "               \n",
    "        \n",
    "    #print(lista_all)\n",
    "    for item in lista_all:\n",
    "        comando = f'''\n",
    "        insert into t_final.venda_produto(id_venda,cod_produto)\n",
    "        values \n",
    "        ({item[0]},{item[1]});\n",
    "        '''\n",
    "        \n",
    "        \n",
    "        cursor = conn.cursor()\n",
    "        cursor.execute(comando)\n",
    "        conn.commit()   \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "27d531d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def inserindo_venda_cliente(): \n",
    "\n",
    "    lista_all = []\n",
    "    for i in range(1,16477):\n",
    "        lista_one = []\n",
    "        id_venda = df.iloc[i,14]\n",
    "        cod_cliente = df.iloc[i,4]        \n",
    "        \n",
    "        lista_one.append(id_venda)\n",
    "        lista_one.append(cod_cliente)     \n",
    "        \n",
    "         \n",
    "        if lista_one not in lista_all:\n",
    "            lista_all.append(lista_one)     \n",
    "               \n",
    "        \n",
    "    #print(lista_all)\n",
    "    for item in lista_all:\n",
    "        comando = f'''\n",
    "        insert into t_final.venda_cliente(id_venda,cod_cliente)\n",
    "        values \n",
    "        ({item[0]},{item[1]});\n",
    "        '''\n",
    "        \n",
    "        \n",
    "        cursor = conn.cursor()\n",
    "        cursor.execute(comando)\n",
    "        conn.commit()   \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04e55c97",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
