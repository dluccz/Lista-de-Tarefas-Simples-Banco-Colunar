from database import adicionar_tarefa, listar_tarefas, visualizar_descricao, remover_tarefa
import uuid

def main():
    while True:
        print("\nMenu de Tarefas:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Visualizar Descrição da Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção (1-5): ")

        if opcao == "1":
            titulo = input("\nDigite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            print(adicionar_tarefa(titulo, descricao))

        elif opcao == "2":
            tarefas = listar_tarefas()
            print("\nTarefas:")
            for tarefa_id, titulo in tarefas:
                print(f"ID: {tarefa_id} - Título: {titulo}")

        elif opcao == "3":
            tarefa_id = input("\nDigite o ID da tarefa que deseja visualizar: ")
            try:
                tarefa_uuid = uuid.UUID(tarefa_id)
                print(visualizar_descricao(tarefa_uuid))
            except ValueError:
                print("ID inválido.")

        elif opcao == "4":
            tarefa_id = input("\nDigite o ID da tarefa que deseja remover: ")
            try:
                tarefa_uuid = uuid.UUID(tarefa_id)
                print(remover_tarefa(tarefa_uuid))
            except ValueError:
                print("ID inválido.")

        elif opcao == "5":
            print("\nSaindo...")
            break

        else:
            print("\nOpção inválida. Por favor, escolha entre 1 e 5.")

if __name__ == "__main__":
    main()
