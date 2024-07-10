# modulos que estão sendo importados 

import adicionar
import remover
import concluir
import listartarefas
import listatarefaporstatus

# menu
def menu():
    tarefas = []
    while True:
        print("\033[37m\nMenu:\033[37m")
        print("\033[32m1. Adicionar tarefa\033[32m")
        print("2. Remover tarefa")
        print("3. Concluir tarefa")
        print("4. Listar todas as tarefas")
        print("5. Listar tarefas concluídas")
        print("6. Listar tarefas não concluídas")
        print("\033[31m7. Sair\033[31m")
        
        # Estrutura
        opcao = input("\033[37mEscolha uma opção:\033[37m")

        if opcao == '1':
            descricao = input("Descrição da tarefa: ")
            adicionar.adicionartarefa(tarefas, descricao)
        elif opcao == '2':
            indice = input("Índice da tarefa a ser removida: ")
            if indice.isdigit():
                remover.removertarefa(tarefas, int(indice))
            else:
                print("\033[33mÍndice deve ser um número inteiro.\033[33m")
        elif opcao == '3':
             indice = input(" Índice da tarefa a ser concluída: ")
             if indice.isdigit():
                concluir.concluirtarefa(tarefas, int(indice))
             else:
                print("\033[33mÍndice deve ser um número inteiro.\033[33m")
        elif opcao == '4':
             listartarefas.listatarefas(tarefas)
        elif opcao == '5':
             listatarefaporstatus.listatarefasporstatus(tarefas, concluida=True)
        elif opcao == '6':
             listatarefaporstatus.listatarefasporstatus(tarefas, concluida=False)
        elif opcao == '7':
             print("Saindo...")
             break
        else:
            print("\033[31mOpção inválida. Tente novamente.\033[31m")

if __name__ == "__main__":
    menu()

