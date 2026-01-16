# Código feito por Asaf Ferreira; Data de publicação: 16/02/2026

from biblioteca.controller.Classes import Livro, Leitor, Reserva
from biblioteca.model.database import engine
from sqlalchemy import join, select, update, delete
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate

def PagInicial():
    print("\n\n\n\nSeja bem-vindo ao Biblios, seu gerenciador de biblioteca! \n O que você deseja fazer hoje?")
    print("1 - Cadastrar;")
    print("2 - Consultar;")
    print("3 - Atualizar;")
    print("4 - Excluir;")
    print("5 - Sair;")

    while True:

        try:
            global nav
            nav = int(input())
            # Tratamento de erros de entrada (se o usuario digitar algo diferente de 1, 2, 3 ou 4)
            if(nav<1 or nav>5):
                print("Digite um número válido")
            elif (nav == str):
                print("Digite apenas números")

            # Navegação do menu Cadastro
            if(nav == 1):
                nav1 = 0
                while(nav1 != 1 or nav1 != 2 or nav1 != 3 or nav1 != 4):
                    print("    1 - Cadastrar novos livros \n    2 - Cadastrar novos leitores \n    3 - Cadastrar Reservas \n    4 - Voltar a pagina inicial")
                    nav1 = int(input())

                    if(nav1 < 1 or nav1 > 4):
                        print("Digite um número válido")

                    # Chamando as respectivas funções (Cadastro de livros e leitores)
                    if (nav1 == 1):
                        CadNovosLivros()
                        nav1 = 0
                        break
                    elif (nav1 == 2):
                        CadNovosClientes()
                        nav1 = 0
                        break
                    elif (nav1 == 3):
                        CadReservas()
                        nav1 = 0
                        break
                    elif (nav1 == 4):
                        PagInicial()
                        break

                nav = 0 # Esta funcionalidade define que ao acabar nosso bloco de codigo, a navegacao torne a pag. inicial.

            # Navegação do menu "Consultar":

            elif(nav == 2):
                nav2 = 0
                while(nav2 != 1 or nav2 != 2 or nav2 != 3 or nav2 != 4):
                    print("    1 - Consultar livros \n    2 - Consultar leitores \n    3 - Consultar reservas \n    4 - Voltar a pagina inicial")
                    nav2 = int(input())

                    if(nav2 < 1 or nav2 > 4):
                        print("Digite um numero valido")

                    if(nav2 == 1):
                        cstLivros()
                        nav2 = 0
                        break
                    elif(nav2 == 2):
                        cstLeitores()
                        nav2 = 0
                        break
                    elif(nav2 == 3):
                        cstReservas()
                        nav2 = 0
                        break
                    elif(nav2 == 4):
                        PagInicial()
                        break
                nav = 0

            # Navegação do menu "Atualizar":

            elif(nav == 3):
                nav3 = 0
                while(nav3 != 1 or nav3 != 2 or nav3 != 3 or nav3 != 4):
                    print("    1 - Atualizar livros \n    2 - Atualizar leitores \n    3 - Atualizar reservas \n    4 - Voltar a pagina inicial")
                    nav3 = int(input())

                    if(nav3 < 1 or nav3 > 4):
                        print("Digite um numero valido")

                    if (nav3 == 1):
                        UpdLivros()
                        nav3 = 0
                        break
                    elif (nav3 == 2):
                        UpdClientes()
                        nav3 = 0
                        break
                    elif (nav3 == 3):
                        UpdReservas()
                        nav3 = 0
                        break
                    elif (nav3 == 4):
                        PagInicial()
                        break
                nav = 0

            # Navegação do menu "Excluir"

            elif(nav == 4):
                nav4 = 0
                
                while(nav4 != 1 or nav4 != 2 or nav4 != 3 or nav4 != 4):
                    print("    1 - Excluir livros \n    2 - Excluir leitores \n    3 - Excluir reservas \n    4 - Voltar a pagina inicial")
                    nav4 = int(input())

                    if(nav4 < 1 or nav4 > 4):
                        print("Digite um numero valido")

                    if (nav4 == 1):
                        DelLivros()
                        nav4 = 0
                        break
                    elif (nav4 == 2):
                        DelClientes()
                        nav4 = 0
                        break
                    elif (nav4 == 3):
                        DelReservas()
                        nav4 = 0
                        break
                    elif (nav4 == 4):
                        PagInicial()
                        break
                nav = 0

            # Navegação do menu "SAIR"

            elif(nav == 5):
                print("Obrigado por usar nosso programa. Ate mais!")
                exit()
                nav = 0
                break
        except ValueError:
            print("Digite um valor válido. Por favor, utilize apenas números inteiros.")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------- Funcoes --------------------------------------------------------------------------------------------------------

# Funcoes de Cadastro:

def CadNovosLivros():
    #este e o nosso navegador inicial
    nav_livros = 1
    while (nav_livros == 1):
        novo_titulo = str(input("Digite o titulo do livro: "))
        novo_autor = str(input("Digite o nome do autor: "))
        novo_ano = int(input("Digite o ano de publicacao do livro: "))
        nova_editora = str(input("Digite a editora do livro: "))
        nova_categoria = str(input("Digite a categoria do livro: "))

        if (novo_titulo is not None
            and novo_autor is not None
            and novo_ano is not None
            and nova_editora is not None
            and nova_categoria is not None):

            Sessao = sessionmaker(bind=engine)
            sessao = Sessao()

            novo_livro = Livro(titulo=novo_titulo, autor=novo_autor, editora=nova_editora, ano=novo_ano, categoria=nova_categoria)
            sessao.add(novo_livro)
            sessao.commit()
        else: 
            print("Valores incompletos. Tente novamente")
            CadNovosLivros()

        print("Voce deseja: \n 1 - Cadastrar um novo livro; \n 2 - Exibir a lista de livros; \n 3 - Voltar a pagina inicial.")

        nav_livros = int(input())

    if(nav_livros <= 0 or nav_livros >= 4):
        print("Digite um valor valido")
        PagInicial()

    elif(nav_livros == 2):
        Sessao = sessionmaker(bind=engine)
        sessao = Sessao()

        select_livros = select(Livro.id, Livro.titulo)
        results_livros = sessao.execute(select_livros).fetchall()
        print(" ID   |      TITULO  ")
        print("---------------------")
        for id, titulo in results_livros:
            print(f"    {id}    {titulo}")


        print("Voce deseja: \n 1 - Cadastrar novos livros ou \n 2 - Voltar a pagina inicial?")
        nav_livros2 = int(input())
        if (nav_livros2 < 1 or nav_livros2 > 2):
            print("Digite um valor valido")
            PagInicial()
        elif (nav_livros2 == 1):
            CadNovosLivros()
        elif(nav_livros2 == 2):
            PagInicial()

    elif(nav_livros == 3):
        PagInicial()
    
def CadNovosClientes():
    nav_clientes = 1

    while (nav_clientes == 1):
        novo_nome = str(input("Digite o primeiro nome do leitor: "))
        novo_sobrenome = str(input("Digite o sobrenome do leitor: "))
        novo_telefone = str(input("Digite o telefone: "))
        novo_email = str(input("Digite o email do leitor: "))
        novo_endereco = str(input("Digite o endereco do leitor: "))

        if (novo_nome is not None 
            and novo_sobrenome is not None 
            and novo_telefone is not None 
            and novo_email is not None 
            and novo_endereco is not None):

            Sessao = sessionmaker(bind=engine)
            sessao = Sessao()

            novo_leitor = Leitor(nome = novo_nome, sobrenome = novo_sobrenome, telefone = novo_telefone, email = novo_email, endereco = novo_endereco)
            sessao.add(novo_leitor)
            sessao.commit()
        else:
            print("Valores invalidos. Tente novamente.")
            CadNovosClientes()

        print("Voce deseja: \n 1 - Cadastrar um novo cliente; \n 2 - Exibir a lista de clientes; \n 3 - Voltar a pagina inicial.")

        nav_clientes = int(input())

    if(nav_clientes <= 0 or nav_clientes >= 4):
        print("Digite um valor valido")
        PagInicial()

    elif(nav_clientes == 2):
        Sessao = sessionmaker(bind=engine)
        sessao = Sessao()

        select_leitores = select(Leitor.id, Leitor.nome)
        results_leitores = sessao.execute(select_leitores).fetchall()
        print(" ID   |      NOME     ")
        print("----------------------")
        for id, nome in results_leitores:
            print(f"{id}      {nome}")

        print("Voce deseja: \n 1 - Cadastrar novos clientes ou \n 2 - Voltar a pagina inicial?")
        nav_clientes2 = int(input())

        if (nav_clientes2 < 1 or nav_clientes2 > 2):
            print("Digite um valor valido")
            PagInicial()
        elif (nav_clientes2 == 1):
            CadNovosClientes()
        elif(nav_clientes2 == 2):
            PagInicial()

    elif(nav_clientes == 3):
        PagInicial()

def CadReservas():
    nav_reservas = 1

    while (nav_reservas == 1):
        id_cliente = int(input("Digite o ID do cliente: "))
        id_livro = int(input("Digite o ID do livro: "))
        data_reserva = str(input("Digite a data da reserva (AAAA-MM-DD): "))
        data_prazo = str(input("Digite a data do prazo (AAAA-MM-DD): "))

        if (id_cliente is not None
            and id_livro is not None
            and data_reserva is not None
            and data_prazo is not None):

            Sessao = sessionmaker(bind=engine)
            sessao = Sessao()

            nova_reserva = Reserva(cod_leitor = id_cliente, cod_livro = id_livro, DataReserva = data_reserva, DataPrazo = data_prazo, Status = 1)
            sessao.add(nova_reserva)
            sessao.commit()
        else:
            print("Valores invalidos. Tente novamente")
            CadReservas()

        print("Voce deseja: \n 1 - Cadastrar uma nova reserva; \n 2 - Exibir a lista de reservas; \n 3 - Voltar a pagina inicial.")

        nav_reservas = int(input())

    if(nav_reservas <= 0 or nav_reservas >= 4):
        print("Digite um valor valido")
        PagInicial()

    elif(nav_reservas == 2):
        Sessao = sessionmaker(bind=engine)
        sessao = Sessao()

        select_reservas = select(Reserva.id, Leitor.nome, Leitor.sobrenome, Livro.titulo).join(Leitor, Livro, Reserva.cod_leitor == Leitor.id, Reserva.cod_livro == Livro.id)
        results_reservas = sessao.execute(select_reservas).fetchall()


        print(" ID   |      CLIENTE       |      LIVRO   ")
        print("------------------------------------------")
        for id, nome, sobrenome, titulo in results_reservas:
            print(f"{id}      {nome, sobrenome}           {titulo}")

        print("Voce deseja: \n 1 - Cadastrar novas reservas ou \n 2 - Voltar a pagina inicial?")
        nav_reservas2 = int(input())
        
        if (nav_reservas2 < 1 or nav_reservas2 > 2):
            print("Digite um valor valido")
            PagInicial()
        elif (nav_reservas2 == 1):
            CadReservas()
        elif(nav_reservas2 == 2):
            PagInicial()

    elif(nav_reservas == 3):
        PagInicial()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Funcoes de Consulta:

def cstLivros():
    Sessao = sessionmaker(bind=engine)
    sessao = Sessao()

    select_livros = select(Livro.id, Livro.titulo, Livro.autor, Livro.editora, Livro.ano, Livro.categoria)
    results_livros = sessao.execute(select_livros).fetchall()

    # Usando a biblioteca tabulate para exibir os resultados em formato de tabela

    rows = [list(row) for row in results_livros]
    headers = ["ID", "TITULO", "AUTOR", "EDITORA", "ANO", "CATEGORIA"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

    nav = ""

    while(nav != "b"):
        nav = str(input("Pressione 'b' para voltar: "))

        if (nav == "b" or nav == "B"):
            PagInicial()

def cstLeitores():
    Sessao = sessionmaker(bind=engine)
    sessao = Sessao()

    select_leitores = select(Leitor.id, Leitor.nome, Leitor.sobrenome, Leitor.telefone, Leitor.email, Leitor.endereco)
    results_leitores = sessao.execute(select_leitores).fetchall()
    
    rows = [list(row) for row in results_leitores]
    headers = ["ID", "NOME", "SOBRENOME", "TELEFONE", "E-MAIL", "ENDERECO"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

    nav = ""

    while(nav != "b"):
        nav = str(input("Pressione 'b' para voltar: "))

        if (nav == "b" or nav == "B"):
            PagInicial()

def cstReservas():
    Sessao = sessionmaker(bind=engine)
    sessao = Sessao()

    select_reservas = select(Reserva.id, Reserva.cod_leitor, Reserva.cod_livro, Reserva.DataReserva, Reserva.DataPrazo, Reserva.Status)
    results_reservas = sessao.execute(select_reservas).fetchall()

    rows = [list(row) for row in results_reservas]
    headers = ["ID", "COD_LEITOR", "COD_LIVRO", "DATA_RESERVA", "DATA_PRAZO", "STATUS"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

    nav = ""

    while(nav != "b"):
        nav = str(input("Pressione 'b' para voltar: "))

        if (nav == "b" or nav == "B"):
            PagInicial()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Funcoes de Atualizacao:

def UpdLivros():

    Sessao = sessionmaker(bind=engine)
    sessao = Sessao()

    select_livros = select(Livro.id, Livro.titulo, Livro.autor, Livro.ano, Livro.editora, Livro.categoria)
    results_livros = sessao.execute(select_livros).fetchall()

    rows = [list(row) for row in results_livros]
    headers = ["ID", "TITULO", "AUTOR", "ANO", "EDITORA", "CATEGORIA"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

    nav_upd_livros = 0

    while (nav_upd_livros == 0):
        print("Digite o ID do livro que deseja atualizar:")
        id_livro_upd = int(input())

        campo = 0

        while(campo != 1 or campo != 2 or campo != 3 or campo != 4):
            campo = int(input("Qual campo deseja atualizar? \n    1 - TITULO; \n    2 - AUTOR; \n    3 - ANO; \n    4 - EDITORA; \n    5 - CATEGORIA;\n"))

            if (campo <= 0 or campo > 5):
                print("Número inválido. Tente novamente")
            
            elif(campo == 1):
                new_title = str(input("Insira o novo titulo: "))
                update_titulo = update(Livro).where(Livro.id == id_livro_upd).values(titulo = new_title)
                sessao.execute(update_titulo)
                print("Titulo atualizado com sucesso!")
            elif(campo == 2):
                new_autor = str(input("Digite o nome do autor: "))
                update_autor = update(Livro).where(Livro.id == id_livro_upd).values(autor = new_autor)
                sessao.execute(update_autor)
                print("Autor atualizado com sucesso!")
            elif(campo == 3):
                new_ano = int(input("Digite o novo ano: "))
                update_ano = update(Livro).where(Livro.id == id_livro_upd).values(ano = new_ano)
                sessao.execute(update_ano)
                print("Ano de publicação atualizado com sucesso!")
            elif(campo == 4):
                new_editora = str(input("Digite a nova editora: "))
                update_editora = update(Livro).where(Livro.id == id_livro_upd).values(editora = new_editora)
                sessao.execute(update_editora)
                print("Editora atualizada com sucesso!")
            elif(campo == 5):
                new_categoria = str(input("Digite a nova categoria: "))
                update_categoria = update(Livro).where(Livro.id == id_livro_upd).values(categoria = new_categoria)
                sessao.execute(update_categoria)
                print("Categoria atualizada com sucesso!")

            cond = str(input("Deseja atualizar mais algum campo?(s/n) "))

            if(cond != "S" and cond != "s" and cond != "N" and cond != "n"):
                print("Comando não reconhecido. Te redirecionaremos a atualizacao de campos novamente")
                campo = 0
            elif(cond == "S" or cond == "s"):
                campo = 0
            elif(cond == "N" or cond == "n"):
                break
        

        cond = str(input("Voce deseja atualizar mais livros? (S/N) "))

        if(cond != "S" and cond != "s" and cond != "N" and cond != "n"):
            print("Comando não reconhecido. Te redirecionaremos a atualizacao de campos novamente")
        elif(cond == "N" or cond == "n"):
            nav_upd_livros = 1
    
    decisao = str(input("Voce deseja voltar a pagina inicial? (S/N) "))
    if(decisao != "S" and decisao != "s" and decisao != "N" and decisao != "n"):
        print("Comando não reconhecido. Te redirecionaremos a atualizacao de livros novamente")
        UpdLivros()
    elif(decisao == "S" or decisao == "s"):
        PagInicial()
    elif(decisao == "N" or decisao == "n"):
        UpdLivros()


def UpdClientes():
    Sessao = sessionmaker(bind=engine)
    sessao = Sessao()

    select_leitores = select(Leitor.id, Leitor.nome, Leitor.sobrenome, Leitor.telefone, Leitor.email, Leitor.endereco)
    results_leitores = sessao.execute(select_leitores).fetchall()

    rows = [list(row) for row in results_leitores]
    headers = ["ID", "NOME", "SOBRENOME", "TELEFONE", "E-MAIL", "ENDERECO"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

    nav_upd_leitores = 0

    while (nav_upd_leitores == 0):
        print("Digite o ID do livro que deseja atualizar:")
        id_leitor_update = int(input())

        campo = 0

        while(campo != 1 or campo != 2 or campo != 3 or campo != 4):
            campo = int(input("Qual campo deseja atualizar? \n    1 - NOME; \n    2 - TELEFONE; \n    3 - EMAIL; \n    4 - ENDERECO;\n"))

            if (campo <= 0 or campo > 4):
                print("Número inválido. Tente novamente")
            
            elif(campo == 1):
                new_nome = str(input("Insira o novo nome: "))
                new_sobrenome = str(input("Insira o novo sobrenome: "))
                update_nome = update(Leitor).where(Leitor.id == id_leitor_update).values(nome = new_nome, sobrenome = new_sobrenome)
                sessao.execute(update_nome)
                print("Nome atualizado com sucesso!")
            elif(campo == 2):
                new_telefone = str(input("Digite o novo telefone do leitor: "))
                update_telefone = update(Leitor).where(Leitor.id == id_leitor_update).values(telefone = new_telefone)
                sessao.execute(update_telefone)
                print("Telefone atualizado com sucesso!")
            elif(campo == 3):
                new_email = str(input("Digite o novo e-mail do leitor: "))
                update_email = update(Leitor).where(Leitor.id == id_leitor_update).values(ano = new_email)
                sessao.execute(update_email)
                print("E-mail atualizado com sucesso!")
            elif(campo == 4):
                new_end = str(input("Digite o novo endereco do leitor: "))
                update_end = update(Leitor).where(Leitor.id == id_leitor_update).values(descricao = new_end)
                sessao.execute(update_end)
                print("Endereco atualizado com sucesso!")
            
            cond = str(input("Deseja atualizar mais algum campo?(s/n) "))

            if(cond != "S" and cond != "s" and cond != "N" and cond != "n"):
                print("Comando não reconhecido. Te redirecionaremos a atualizacao de campos novamente")
                campo = 0
            elif(cond == "S" or cond == "s"):
                campo = 0
            elif(cond == "N" or "n"):
                break
        

        cond = str(input("Voce deseja atualizar mais dados de leitores? (S/N) "))

        if(cond != "S" and cond != "s" and cond != "N" and cond != "n"):
            print("Comando não reconhecido. Te redirecionaremos a atualizacao de campos novamente")
        elif(cond == "N" or "n"):
            nav_upd_leitores = 1
    
    decisao = str(input("Voce deseja voltar a pagina inicial? (S/N) "))
    if(decisao != "S" and decisao != "s" and decisao != "N" and decisao != "n"):
        print("Comando não reconhecido. Te redirecionaremos a atualizacao de dados de leitores novamente")
        UpdClientes()
    elif(decisao == "S" or decisao == "s"):
        PagInicial()
    elif(decisao == "N" or "n"):
        UpdClientes()

def UpdReservas():
    Sessao = sessionmaker(bind=engine)
    sessao = Sessao()

    select_reservas = select(Reserva.id, Reserva.cod_leitor, Reserva.cod_livro, Reserva.DataReserva, Reserva.DataPrazo, Reserva.Status)
    results_reservas = sessao.execute(select_reservas).fetchall()

    rows = [list(row) for row in results_reservas]
    headers = ["ID", "COD_LEITOR", "COD_LIVRO", "DATA_RESERVA", "DATA_PRAZO", "STATUS"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

    nav_upd_reservas = 0

    while (nav_upd_reservas == 0):
        print("Digite o ID da reserva que deseja atualizar:")
        id_reserva_update = int(input())

        campo = 0

        while(campo != 1 or campo != 2 or campo != 3 or campo != 4 or campo != 5):
            campo = int(input("Qual campo deseja atualizar? \n    1 - COD_LEITOR; \n    2 - COD_LIVRO; \n    3 - DATA_RESERVA; \n    4 - DATA_PRAZO;\n    5 - STATUS;\n"))

            if (campo <= 0 or campo > 5):
                print("Número inválido. Tente novamente")
            
            elif(campo == 1):
                new_id_leitor = int(input("Insira o novo ID do leitor: "))
                upd_id_leitor = update(Reserva).where(Reserva.id == id_reserva_update).values(cod_leitor = new_id_leitor)
                sessao.execute(upd_id_leitor)
                print("ID do leitor atualizado com sucesso!")
            elif(campo == 2):
                new_id_livro = int(input("Digite o novo ID do livro: "))
                upd_id_livro = update(Reserva).where(Reserva.id == id_reserva_update).values(cod_livro = new_id_livro)
                sessao.execute(upd_id_livro)
                print("ID do livro atualizado com sucesso!")
            elif(campo == 3):
                new_data_reserva = str(input("Digite a nova data da reserva: "))
                upd_DataReserva = update(Reserva).where(Reserva.id == id_reserva_update).values(DataReserva = new_data_reserva)
                sessao.execute(upd_DataReserva)
                print("Data da reserva atualizada com sucesso!")
            elif(campo == 4):
                new_data_prazo = str(input("Digite o novo endereco do leitor: "))
                upd_dataPrazo = update(Reserva).where(Reserva.id == id_reserva_update).values(DataPrazo = new_data_prazo)
                sessao.execute(upd_dataPrazo)
                print("Data do prazo atualizado com sucesso!")
            
            cond = str(input("Deseja atualizar mais algum campo?(s/n) "))

            if(cond != "S" and cond != "s" and cond != "N" and cond != "n"):
                print("Comando não reconhecido. Te redirecionaremos a atualizacao de campos novamente.")
                campo = 0
            elif(cond == "S" or cond == "s"):
                campo = 0
            elif(cond == "N" or "n"):
                break
        

        cond = str(input("Voce deseja atualizar mais dados de reservas? (S/N) "))

        if(cond != "S" and cond != "s" and cond != "N" and cond != "n"):
            print("Comando não reconhecido. Te redirecionaremos a atualizacao de campos novamente.")
        elif(cond == "N" or "n"):
            nav_upd_reservas = 1
    
    decisao = str(input("Voce deseja voltar a pagina inicial? (S/N) "))
    if(decisao != "S" and decisao != "s" and decisao != "N" and decisao != "n"):
        print("Comando não reconhecido. Te redirecionaremos a atualizacao de dados de reservas novamente.")
        UpdReservas()
    elif(decisao == "S" or decisao == "s"):
        PagInicial()
    elif(decisao == "N" or "n"):
        UpdClientes()

# ------------ -------------------------------------------------------------------------------------------------------------------------------------------------
# Funcoes de Exclusao:

def DelLivros():
    Sessao = sessionmaker(bind=engine)
    sessao = Sessao()

    select_livros = select(Livro.id, Livro.titulo, Livro.autor, Livro.ano, Livro.editora, Livro.categoria)
    results_livros = sessao.execute(select_livros).fetchall()

    rows = [list(row) for row in results_livros]
    headers = ["ID", "TITULO", "AUTOR", "ANO", "EDITORA", "CATEGORIA"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

    nav_del_livros = 0

    while (nav_del_livros == 0):
        print("Digite o ID do livro que deseja deletar:")
        id_livro_delete = int(input())

        del_livro = delete(Livro).where(Livro.id == id_livro_delete)
        sessao.execute(del_livro)
        print("Livro deletado com sucesso!")

        decisao = int(input("Voce deseja:    1 - Deletar mais livros; ou \n    2 - Voltar a pagina inicial ?"))

        if(decisao < 1 or decisao > 2):
            print("Digite uma opcao valida")
        elif(decisao == 1):
            DelLivros()
        elif(decisao == 2):
            nav_del_livros = 1
            PagInicial()

    
def DelClientes():
    Sessao = sessionmaker(bind=engine)
    sessao = Sessao()

    select_leitores = select(Leitor.id, Leitor.nome, Leitor.sobrenome, Leitor.telefone, Leitor.email, Leitor.endereco)
    results_leitores = sessao.execute(select_leitores).fetchall()

    rows = [list(row) for row in results_leitores]
    headers = ["ID", "NOME", "SOBRENOME", "TELEFONE", "E-MAIL", "ENDERECO"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

    nav_del_leitores = 0

    while (nav_del_leitores == 0):
        print("Digite o ID do livro que deseja deletar:")
        id_leitor_delete = int(input())

        del_leitor = delete(Leitor).where(Leitor.id == id_leitor_delete)
        sessao.execute(del_leitor)
        print("Leitor deletado com sucesso!")

        decisao = int(input("Voce deseja:    1 - Deletar mais leitores; ou \n    2 - Voltar a pagina inicial ?"))

        if(decisao < 1 or decisao > 2):
            print("Digite uma opcao valida")
        elif(decisao == 1):
            DelClientes()
        elif(decisao == 2):
            nav_del_leitores = 1
            PagInicial()

def DelReservas():
    Sessao = sessionmaker(bind=engine)
    sessao = Sessao()

    select_reservas = select(Reserva.id, Reserva.cod_leitor, Reserva.cod_livro, Reserva.DataReserva, Reserva.DataPrazo, Reserva.Status)
    results_reservas = sessao.execute(select_reservas).fetchall()

    rows = [list(row) for row in results_reservas]
    headers = ["ID", "COD_LEITOR", "COD_LIVRO", "DATA_RESERVA", "DATA_PRAZO", "STATUS"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

    nav_del_reservas = 0

    while (nav_del_reservas == 0):
        print("Digite o ID da reserva que deseja deletar:")
        id_reserva_delete = int(input())

        del_reserva = delete(Reserva).where(id = id_reserva_delete)
        sessao.execute(del_reserva)
        print("Reserva deletada com sucesso!")

        decisao = int(input("Voce deseja:    1 - Deletar mais reservas; ou \n    2 - Voltar a pagina inicial ?"))

        if(decisao < 1 or decisao > 2):
            print("Digite uma opcao valida")
        elif(decisao == 1):
            DelLivros()
        elif(decisao == 2):
            nav_del_reservas = 1
            PagInicial()

# "E sabemos que todas as coisas contribuem juntamente para o bem daqueles que amam a Deus, e são chamados segundo o Seu propósito." Rm 8:28
# Soli Deo Gloria!