import mariadb
import flask
from flask import request, jsonify
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'algorithms')))
import total
from total import grafico_total
import equipamento
from equipamento import grafico_equipamento

app = flask.Flask(__name__)
app.config["DEBUG"] = True

config = {
    'host': '127.0.0.1',
    'user': 'leodiasdc',
    'password': 'senha123',
    'database': 'database_0'
}

def db_connection():
    conn = mariadb.connect(**config)
    return conn

@app.route('/api/equipamento', methods=['POST'])
def add_equipamento():
    conn = db_connection()
    cur = conn.cursor()
    data = request.json
    cur.callproc('AddEquipamento', [
        data['nome_equipamento'],
        data.get('nome_fabricante'),
        data['potencia'],
        data['eh_input_do_usuario'],
        data['rigidez_de_horario']
    ])
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
    conn = db_connection()
    cur = conn.cursor()
    data = request.json
    cur.callproc('AddUsuario', [
        data['nome'],
        data['email'],
        data['senha']
    ])
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"success": True})

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

UPLOAD_FOLDER = '/api/output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/output', methods = ['POST'])
def post_output():
    imagem_equipamento = request.files['imagem_equipamento']
    imagem_total = request.files['imagem_total']
    total.grafico_total(dados)
    total.grafico_equipamento(dados)
    equipamento_path = os.path.join(app.config['UPLOAD_FOLDER'], '../algorithms/grafico_equipamento.png')
    total_path = os.path.join(app.config['UPLOAD_FOLDER'], '../algorithms/grafico_equipamento.png')

    imagem_equipamento.save(equipamento_path)
    imagem_total.save(total_path)
    numero_tarifabranca = float(request.get['numero_tarifabranca'])
    numero_tarifaconvencional = float(request.get['numero_tarifaconvencional'])
    mensagem_maritaka = request.get['mensagem_maritaka']
    return jsonify({
        'message': 'Arquivos e variáveis recebidos com sucesso!',
        'numero_tarifabranca': numero_tarifabranca,
        'numero_tarifaconvencional': numero_tarifaconvencional,
        'equipamento_path': equipamento_path,
        'total_path': total_path,
        'mensagem_maritaka': mensagem_maritaka
    }), 200

@app.route('/login', methods=['POST'])
def login_usuario():
    data = request.get_json()
    nome = data.get('nome')
    senha = data.get('senha')

    if not nome or not senha:
        return jsonify({'error': 'Nome e senha são obrigatórios'}), 400
    
    conn = db_connection()
    cursor = conn.cursor()

    # Chama o procedimento armazenado
    cursor.callproc('LoginUsuario', [nome, senha, 0])
    p_result = cursor.fetchall()

    cursor.close()
    conn.close()
    if p_result[0][0] == 1:
        return jsonify({'message': 'Login bem-sucedido'}), 200
    else:
        return jsonify({'error': 'Usuário ou senha incorretos'}), 401

@app.route('/equipamentos', methods=['GET'])
def get_equipamentos():
    usuario_id = request.args.get('usuario_id', type=int)

    if not usuario_id:
        return jsonify({'error': 'ID do usuário é obrigatório'}), 400

    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc('GetEquipamentosByUsuario', [usuario_id])
    
    equipamentos = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify({'equipamento': f'{equipamentos}'}), 404

@app.route('/equipamentos/equipamentosbyusuario', methods=['GET'])
def get_equipamentos_by_usuario(usuario_id):
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc('GetEquipamentosByUsuario', [usuario_id])
    
    # Recuperar os resultados da procedure
    equipamentos = []
    for row in cursor:
        equipamentos.append(row)
    
    cursor.close()
    conn.close()
    return jsonify(equipamentos), 200


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

if __name__ == '__main__':
    app.run(port=8080)
