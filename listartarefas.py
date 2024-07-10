def listatarefas(tarefas):
    if tarefas:
        for i, tarefa in enumerate(tarefas):
            status = "Concluída" if tarefa['concluida'] else "Pendente"
            print(f"{i}. {tarefa['descricao']} - {status}")
    else:
        print("Nenhuma tarefa na lista.")