
def get_idProfessor(cursor, nome):
    cursor.execute(f'select idProfessor from professor where nome="{nome}"')
    id = cursor.fetchone()
    print(f'id={id}')
    return id[0]

def get_professores(cursor):
    # executar o select:
    cursor.execute('select nome from professor')

    professores = cursor.fetchall()

    lista = []
    for p in professores:
        lista.append(p[0])

    print(lista)
    # Fechar o cursor
    cursor.close()

    return lista


def get_detalhes(cursor, nome):
    # executar o select:
    cursor.execute(f'select professor.nome, professor.DataNasc, professor.NomeMae, professor.Titulacao from professor where nome = "{ nome }"')
    info = cursor.fetchall()
    return info

def get_detalhes2(cursor, id):
    # executar o select:
    cursor.execute(f'select disciplina.Nome, disciplina.Curso, disciplina.CargaHoraria from disciplina where idProfessor = "{id}"')
    info2 = cursor.fetchall()
    cursor.close()

    print(info2)
    return info2



