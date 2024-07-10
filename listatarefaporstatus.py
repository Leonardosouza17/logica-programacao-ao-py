def listartarefasporstatus(tarefas, concluida=True):
    statustexto = "concluídas" if concluida else "não concluídas"
    tarefasfiltradas = [tarefa for tarefa in tarefas if tarefa.concluida == concluida]
    if tarefasfiltradas:
        for i, tarefa in enumerate(tarefasfiltradas):
            print(f"{i}. {tarefa.descricao}")
    else:
        print(f"Nenhuma tarefa {statustexto}.")
