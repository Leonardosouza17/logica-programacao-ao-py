def concluirtarefa(tarefas, indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]['concluida'] = True
        print(f"Tarefa '{tarefas[indice]['descricao']}' marcada como concluída.")
    else:
        print(" Índice de tarefa inválido.")