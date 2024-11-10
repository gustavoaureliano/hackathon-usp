import mariadb
import flask
from flask import request, jsonify
from flask_cors import CORS
from datetime import timedelta
import total
import equipamento
import base64
import algorithm,maritalk,tarifabranca

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
config = {
    'host': '127.0.0.1',
    'user': 'leodiasdc',
    'password': 'senha123',
    'database': 'database_2'
}

def db_connection():
    conn = mariadb.connect(**config)
    return conn

@app.route('/api/equipamento', methods=['POST'])
def add_equipamento():
    conn = db_connection()
    cur = conn.cursor()
    data = request.json
    usuario_id = data['usuario_id']
    cur.callproc('AddEquipamento', [
        data['nome_equipamento'],
        data.get('nome_fabricante'),
        data['potencia'],
        data['eh_input_do_usuario'],
        data['rigidez_de_horario'],
        0
    ])
    equipamento_id = cur.fetchall()[0][0]
    for periodo in data['periodos']:
        cur.callproc('AddEquipamentoUsuario', [equipamento_id, usuario_id, 0])
        equipamentousuarioid = cur.fetchall()[0][0]
        cur.callproc('AddHorarioDeUso', [
            periodo['inicio'],
            periodo['fim'],
            equipamentousuarioid]
        )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"success": True})


@app.route('/api/add_equipamento_usuario', methods=['POST'])
def add_equipamento_usuario():
    data = request.get_json()
    equipamento_id = data.get('equipamento_id')
    usuario_id = data.get('usuario_id')
    
    # Conectar ao banco e chamar a procedure
    conn = db_connection()

    cursor = conn.cursor()
    cursor.callproc('AddEquipamentoUsuario', [equipamento_id, usuario_id])
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'success': 'Equipamento adicionado ao usuário com sucesso'}), 200

@app.route('/api/usuario', methods=['POST'])
def add_usuario():
    data = request.get_json()
    conn = db_connection()
    cursor= conn.cursor()
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')
    cursor.callproc('AddUsuario', [nome, email, senha, 0])

    p_usuario_id = cursor.fetchall()[0][0]
    cursor.close()
    conn.close()

    # Retornando a resposta com o ID do novo usuário
    return jsonify({"usuario_id": p_usuario_id}), 201

@app.route('/api/horario_de_uso', methods=['POST'])
def add_horario_de_uso():
    conn = db_connection()
    cur = conn.cursor()
    data = request.json
    cur.callproc('AddHorarioDeUso', [
        data['inicio'],
        data['fim'],
        data['equipamento_id']
    ])
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"success": True})

@app.route('/api/equipamento', methods=['DELETE'])
def remove_equipamento():
    conn = db_connection()
    cur = conn.cursor()
    equipamento_id = request.args.get('equipamento_id')
    cur.callproc('RemoveEquipamento', [equipamento_id])
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"success": True})

@app.route('/api/usuario', methods=['DELETE'])
def remove_usuario():
    conn = db_connection()
    cur = conn.cursor()
    usuario_id = request.args.get('usuario_id')
    cur.callproc('RemoveUsuario', [usuario_id])
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"success": True})

@app.route('/api/horario_de_uso', methods=['DELETE'])
def remove_horario_de_uso():
    conn = db_connection()
    cur = conn.cursor()
    horario_de_uso_id = request.args.get('horario_de_uso_id')
    cur.callproc('RemoveHorarioDeUso', [horario_de_uso_id])
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"success": True})

@app.route('/api/output', methods = ['POST'])
def post_output():
    data = request.get_json()
    usuario_id = data.get('usuario_id')

    conn = db_connection()
    cursor = conn.cursor()
    cursor.callproc('GetEquipamentosEHorariosByUsuario', [usuario_id])

    dados_tratados = []
    dados = []
    for row in cursor:
        dados.append(row)
    print(dados)
    for dado in dados:
        dict = {
            "equipamento":dado[1],
            "potencia":float(dado[3]),
            "comeco":dado[4],
            "fim":dado[5]
        }
        dados_tratados.append(dict)
    total.grafico_total(dados_tratados)
    equipamento.grafico_equipamento(dados_tratados)

    caminho_total = "grafico_total.png"
    caminho_equipamento = "grafico_equipamento.png"

    with open(caminho_total, "rb") as imagem_file:
        total_base64 = base64.b64encode(imagem_file.read()).decode('utf-8')
    
    with open(caminho_equipamento, "rb") as imagem_file:
        equipamento_base64 = base64.b64encode(imagem_file.read()).decode('utf-8')


    numero_tarifabranca = algorithm.total_tarifabranca(dados_tratados)
    numero_tarifaconvencional = algorithm.total_tarifaconvencional(dados_tratados)

    mensagem_maritaka =  maritalk.message(dados_tratados)

    return jsonify({
        'message': 'Arquivos e variáveis recebidos com sucesso!',
        'numero_tarifabranca': numero_tarifabranca,
        'numero_tarifaconvencional': numero_tarifaconvencional,
        'equipamento_imagem': total_base64,
        'total_imagem': equipamento_base64,
        'mensagem_maritaka': mensagem_maritaka
    }), 200

@app.route('/login', methods=['POST'])
def login_usuario():
    data = request.get_json()
    nome = data.get('nome')
    senha = data.get('senha')

    conn = db_connection()
    cursor = conn.cursor()

    # Chama o procedimento armazenado
    cursor.callproc('LoginUsuario', [nome, senha, 0])
    p_result = cursor.fetchall()[0][0]

    cursor.close()
    conn.close()
    try:
        return jsonify({'message': f'{p_result}'}), 200
    except:
        return jsonify({'message':'Usuário ou senha incorretos!'})
@app.route('/equipamentos', methods=['POST'])
def get_equipamentos():
    data = request.get_json()
    usuario_id = data.get('usuario_id')

    if not usuario_id:
        return jsonify({'error': 'ID do usuário é obrigatório'}), 400

    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc('GetEquipamentosByUsuario', [usuario_id])
    
    equipamentos = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify({'equipamento': f'{equipamentos}'}), 404


@app.route('/horarios/horariosbyequipamentousuario', methods=['GET'])
def get_horarios_by_equipamento_usuario(equipamento_usuario_id):
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc('GetHorariosByEquipamentoUsuario', [equipamento_usuario_id])
    
    # Recuperar os resultados da procedure
    horarios = []
    for row in cursor:
        horarios.append(row)
    
    cursor.close()
    conn.close()
    return jsonify(horarios), 200

@app.route('/horarios/infos', methods = ['GET'])
def get_equipamentos_e_horarios_by_usuario():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    data = request.get_json()
    usuario_id = data.get('usuario_id')

    cursor.callproc('GetEquipamentosEHorariosByUsuario', [usuario_id])
    
    # Recuperar os resultados da procedure
    equipamentos_e_horarios = []
    for row in cursor:
        equipamentos_e_horarios.append(row)
    
    cursor.close()
    conn.close()
    return jsonify(equipamentos_e_horarios), 200

if __name__ == '__main__':
    app.run(port=8080)
