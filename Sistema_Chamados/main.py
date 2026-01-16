import sqlite3

#conexão com o bando de dados
conn = sqlite3.connect("chamados.db")
cursor = conn.cursor()
STATUS_VALIDOS = ["Aberto", "Em Andamento", "Resolvido"]

#Criar a tabela de chamados
cursor.execute("""
CREATE TABLE IF NOT EXISTS chamados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT,
    problema TEXT,
    status TEXT
)
""")
conn.commit()

from funcoes import (
   abrir_chamado,
   listar_chamados,
   atualizar_status,
   deletar_chamado,
   listar_por_status,
   buscar_por_cliente,
   relatorio_chamados,
   exportar_relatorio_txt,
)
from database import conn

try:
    while True:
        print("\n=== SISTEMA DE CHAMADOS ===")
        print("1 - Abrir chamado")
        print("2 - Listar chamados")
        print("3 - Atualizar status")
        print("4 - Deletar chamado")
        print("5 - Listar por status")
        print("6 - Buscar cliente")
        print("7 - Relatório de chamados")
        print("8 - Exportar relatório (TXT)")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            abrir_chamado()
        elif opcao == "2":
            listar_chamados()
        elif opcao == "3":
            atualizar_status()
        elif opcao == "4":
            deletar_chamado()
        elif opcao == "5":
            listar_por_status()
        elif opcao == "6":
            buscar_por_cliente()
        elif opcao == "7":
            relatorio_chamados()
        elif opcao == "8":
            exportar_relatorio_txt()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

finally:
    conn.close()
    print("Conexão com o banco encerrada.")


