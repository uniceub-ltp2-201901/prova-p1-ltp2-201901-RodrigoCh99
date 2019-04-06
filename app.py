# Importando as bibliotecas:
from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from bd import *

# Instanciando  o Flask
app = Flask(__name__)

# Instanciando o MySQL
mysql = MySQL()

# Ligação MySQL com Flask
mysql.init_app(app)

# configurando o acesso ao MySQL:

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'faculdade'

# rota para "/"
@app.route('/')
def principal():
    return render_template('index.html')


@app.route('/listarProfessores/<numero>')
def questao(numero):

    if numero == '2':

        # Atribuindo o cursor do banco de dados a uma variavel
        cursor = mysql.get_db().cursor()

        return render_template('questao2.html', nomes=get_professores(cursor))


@app.route('/exibirProfessor/<professor>')
def professor(professor):
    cursor = mysql.get_db().cursor()
    id = get_idProfessor(cursor, professor)
    cursor = mysql.get_db().cursor()
    return render_template('prof.html', info=get_detalhes(cursor, professor), info2=get_detalhes2(cursor, id))




@app.route('/consultarApenasComputacao')
def consulta(computação):









# Loop de execução do app:
if __name__ == '__main__':
    app.run(debug=True)