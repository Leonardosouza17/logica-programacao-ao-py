def removertarefa(tarefas, indice):
     if 0 <= indice < len(tarefas):
         tarefa = tarefas.pop(indice)
         print(f"Tarefa '{tarefa['descricao']}' removida com sucesso.")
     else:
         print("\033[31mÍndice da tarefa inválido.\033[31m")