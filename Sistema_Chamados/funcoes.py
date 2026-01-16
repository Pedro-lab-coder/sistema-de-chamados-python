from database import cursor, conn
from datetime import datetime

STATUS_VALIDOS = ["Aberto", "Em andamento", "Resolvido"]

def abrir_chamado():
    cliente = input("Nome do cliente: ").strip()
    problema = input("Descreva o problema: ").strip()

    if cliente == "" or problema == "":
        print("X cliente e problema não podem ficar vazios!\n")
        return #sai da função de abrir chamado
    status = "Aberto"

    cursor.execute(
        "INSERT INTO chamados (cliente, problema, status) VALUES (?, ?, ?)",
        (cliente, problema, status)
    )
    conn.commit()
    print("Chamado aberto com sucesso!\n")

def atualizar_status():
    id_chamado = input("Digite o ID do chamado: ").strip()

    while True:
        novo_status = input("Novo status (Aberto / Em Andamento / Resolvido): ").strip().capitalize()

        if novo_status not in STATUS_VALIDOS:
            print("X Status inválido. Tente novamente.")
        else:
            break

    cursor.execute("SELECT id FROM chamados WHERE id = ?", (id_chamado,))
    if cursor.fetchone() is None:
        print("X Nenhum chamado encontrado com esse ID.\n")
        return

    cursor.execute(
        "UPDATE chamados SET status = ? WHERE id = ?",
        (novo_status, id_chamado)
    )
    conn.commit()

    print("Status atualizado com sucesso!\n")



def listar_chamados():
    cursor.execute("SELECT * FROM chamados")
    chamados = cursor.fetchall()

    if not chamados:
        print("Nenhum chamado cadastrado.\n")
        return

    print("\n LISTA DE CHAMADOS")
    for c in chamados:
        print(f"ID: {c[0]} | Cliente: {c[1]} | Status: {c[3]}")
        print(f"Problema: {c[2]}")
        print("-" * 30)

def listar_por_status():
    status = input("Digite o status (Aberto / Em Andamento / Resolvido): ").strip()

    cursor.execute(
        "SELECT * FROM chamados WHERE status = ?",
        (status,)
    )
    chamados = cursor.fetchall()

    if not chamados:
        print("Nenhum chamado encontrado com esse status.\n")
        return

    print(f"\n CHAMADOS COM STATUS: {status}")
    for c in chamados:
        print(f"ID: {c[0]} | Cliente: {c[1]}")
        print(f"Problema: {c[2]}")
        print("-" * 30)

def buscar_por_cliente():
            nome = input("Digite o nome do cliente: ").strip()

            cursor.execute(
                "SELECT * FROM chamados WHERE cliente LIKE ?",
                (f"%{nome}%",)
            )
            chamados = cursor.fetchall()

            if not chamados:
                print("Nenhum chamado encontrado para esse cliente.\n")
                return

            print("\n CHAMADOS ENCONTRADOS:")
            for c in chamados:
                print(f"ID: {c[0]} | Cliente: {c[1]} | Status: {c[3]}")
                print(f"Problema: {c[2]}")
                print("-" * 30)


def deletar_chamado():
    id_chamado = input("Digite o ID do chamado que deseja deletar: ")

    # verifica se existe
    cursor.execute("SELECT id FROM chamados WHERE id = ?", (id_chamado,))
    resultado = cursor.fetchone()

    if resultado is None:
        print("X Nenhum chamado encontrado com esse ID.\n")
        return

    # pede confirmação só se existir
    confirmacao = input("Tem certeza que deseja deletar? (sim/não): ").strip().lower()

    if confirmacao == "sim":
        cursor.execute(
            "DELETE FROM chamados WHERE id = ?",
            (id_chamado,)
        )
        conn.commit()
        print("Chamado deletado com sucesso!\n")
    else:
        print("Ação cancelada.\n")

def relatorio_chamados():
    cursor.execute("SELECT COUNT(*) FROM chamados")

    total = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM chamados WHERE status = 'Aberto'")
    abertos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM chamados WHERE status = 'Em Andamento'")
    Andamento = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM chamados WHERE status = 'Resolvido'")
    resolvidos = cursor.fetchone()[0]

    print("\n=== RELATÓRIO DE CHAMADOS ===")
    print(f"Total: {total}")
    print(f"Abertos: {abertos}")
    print(f"Em Andamento: {Andamento}")
    print(f"Resolvidos: {resolvidos}\n")

def exportar_relatorio_txt():
    cursor.execute("SELECT * FROM chamados")
    chamados = cursor.fetchall()

    if not chamados:
        print("Nenhum chamado para exportar.\n")
        return
    with open("relatorio_chamados.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("RELATÓRIO DE CHAMADOS\n\n")
        for c in chamados:
            arquivo.write(f"ID: {c[0]}\n")
            arquivo.write(f"Clientes: {c[1]}\n")
            arquivo.write(f"Problema: {c[2]}\n")
            arquivo.write(f"ID:Status: {c[3]}\n")
            arquivo.write("-" * 30 + "\n")

    print("Relatório exportado para 'relatorio_chamado.txt'\n")
