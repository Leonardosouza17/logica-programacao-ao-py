# Sua tarefa é criar um programa em Python que permita ao usuário gerenciar uma lista de tarefas. O programa deve ter recursos para adicionar tarefas, remover tarefas, marcar tarefas como concluídas, listar todas as tarefas e listar apenas tarefas concluídas ou não concluídas.

print('menu')
print('1. Adicionar tarefa')
print('2. Remover tarefa')
print('3. Conclui tarefa')
print('4. Lista tarefa')
print('5. Lista tarefa por status')
print('6. Sair')

tarefas = ["css","html","js"]
status = ["pendente","concluida"]
while True:
     opcao = int(input('Digite a opção: '))
     if opcao == 1:
         tarefa = input('Digite a tarefa:')
         tarefas.append(tarefas)
         status.append('pendente')
         break
     elif opcao == 2:
         tarefa = input('Digite a tarefa: ')
         tarefas.remove(tarefa)
     elif opcao == 3:
          tarefa = input('Digite a tarefa: ')
          status.remove('pendente')
          status.append('concluída')    
     elif opcao == 4:
          print(tarefas)
     elif opcao == 5:
         print(status)
     elif opcao == 6:
         print('sair')
          
        



    

        

