def adicionartarefa(tarefas, descricao):
    tarefa = {'descricao': descricao, 'concluida': False}
    tarefas.append(tarefa)
    print(f"Tarefa '{descricao}' adicionada com sucesso.")

