import mariadb
import flask
from flask import request, jsonify
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

config = {
    'host': '127.0.0.1',
    'user': 'app_user',
    'password': 'Password123!',
    'database': 'todo'
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

@app.route('/api/output', methods = 'POST')
def post_output():
    imagem_equipamento = request.files['imagem_equipamento']
    imagem_total = request.files['imagem_total']

    equipamento_path = os.path.join(app.config['UPLOAD_FOLDER'], 'imagem_equipamento.png')
    total_path = os.path.join(app.config['UPLOAD_FOLDER'], 'imagem_total.png')

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
        'mensagem_maritaka':mensagem_maritaka
    }), 200

if __name__ == '__main__':
    app.run(port=8080)
