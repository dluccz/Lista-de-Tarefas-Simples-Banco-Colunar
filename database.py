from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import uuid

# Conectar ao cluster Cassandra local
cluster = Cluster(["127.0.0.1"])
session = cluster.connect()

# Criação do keyspace e tabela se não existirem
session.execute("CREATE KEYSPACE IF NOT EXISTS todolist WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};")
session.execute("USE todolist;")
session.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id UUID PRIMARY KEY,
        titulo TEXT,
        descricao TEXT
    );
""")

# Funções para manipular as tarefas

def adicionar_tarefa(titulo, descricao):
    tarefa_id = uuid.uuid4()
    session.execute(
        "INSERT INTO tarefas (id, titulo, descricao) VALUES (%s, %s, %s)",
        (tarefa_id, titulo, descricao)
    )
    return f"Tarefa adicionada com ID: {tarefa_id}"

def listar_tarefas():
    rows = session.execute("SELECT id, titulo FROM tarefas")
    return [(row.id, row.titulo) for row in rows]

def visualizar_descricao(id):
    row = session.execute("SELECT descricao FROM tarefas WHERE id=%s", (id,)).one()
    return row.descricao if row else "Tarefa não encontrada."

def remover_tarefa(id):
    session.execute("DELETE FROM tarefas WHERE id=%s", (id,))
    return f"Tarefa com ID {id} removida."
