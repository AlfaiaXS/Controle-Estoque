import pyodbc

dados_conexao = 'Driver={SQLite3 ODBC Driver};Server=localhost;Database=Estoque.db'
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()


def adicionar_insumo(nome_insumo, qtde_insumo, validade_insumo, lote_insumo):
    """

    :param nome_insumo: nome do produto
    :param qtde_insumo: quantidade do produto
    :param validade_insumo: validade do produto
    :param lote_insumo: lote do produto
    :return: adiciona produto na tabela
    """
    cursor.execute(f'''
    INSERT INTO Estoque (Produto, Quantidade, DataValidade, Lote)
    VALUES
    ("{nome_insumo}", {qtde_insumo}, "{validade_insumo}", {lote_insumo})
    ''')
    cursor.commit()


def deletar_insumo(nome_insumo, id_produto):
    """

    :param nome_insumo: nome do produto
    :param id_produto: id do produto
    :return: deleta produto
    """
    cursor.execute(f'''
    DELETE FROM Estoque
    WHERE Produto="{nome_insumo}" AND "{id_produto}"
    ''')
    cursor.commit()


def consumir_insumo(nome_insumo, qtde_insumo, id_insumo):
    """

    :param nome_insumo: nome do produto
    :param qtde_insumo: quantidade do produto
    :param id_insumo: id do produto
    :return: consome a quantidade do produto
    """
    cursor.execute(f'''
    UPDATE Estoque
    SET Quantidade=Quantidade - {qtde_insumo}
    WHERE Produto="{nome_insumo}" AND "{id_insumo}" 
    ''')
    cursor.commit()


def visualizar_insumo(nome_insumo):
    """

    :param nome_insumo: 
    :return:
    """
    cursor.execute(f'''SELECT * FROM Estoque WHERE Produto="{nome_insumo}" ''')
    valores = cursor.fetchall()
    for id_produto, nome, quantidade, validade, lote in valores:
        print('---------------')
        print(f'ID: {id_produto}\nNome: {nome}\nValidade: {validade}\nLote: {lote}')
