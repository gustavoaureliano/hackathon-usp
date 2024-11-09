CREATE TABLE IF NOT EXISTS 
EQUIPAMENTOS (
    equipamento_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    nome_equipamento VARCHAR(255) NOT NULL, 
    nome_fabricante VARCHAR(255),
    potencia DECIMAL(6, 2) NOT NULL,  
    eh_input_do_usuario BOOL, 
    rigidez_de_horario TINYINT
);

CREATE TABLE IF NOT EXISTS 
HORARIOS_DE_USO (
    horario_de_uso_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    inicio TIME, 
    fim TIME, 
    equipamento_id BIGINT UNSIGNED NOT NULL, 
    FOREIGN KEY (equipamento_id) REFERENCES EQUIPAMENTOS(equipamento_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS
USUARIOS (
    usuario_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL, 
    email VARCHAR(255) NOT NULL, 
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS 
EQUIPAMENTO_USUARIO (
    equipamento_usuario_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    equipamento_id BIGINT UNSIGNED NOT NULL, 
    usuario_id BIGINT UNSIGNED NOT NULL, 
    FOREIGN KEY (equipamento_id) REFERENCES EQUIPAMENTOS(equipamento_id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_id) REFERENCES USUARIOS(usuario_id) ON DELETE CASCADE
);

DELIMITER //

CREATE PROCEDURE AddEquipamento(
    IN p_nome_equipamento VARCHAR(255),
    IN p_nome_fabricante VARCHAR(255),
    IN p_potencia DECIMAL(6, 2),
    IN p_eh_input_do_usuario BOOL,
    IN p_rigidez_de_horario TINYINT
)
BEGIN
    INSERT INTO EQUIPAMENTOS (nome_equipamento, nome_fabricante, potencia, eh_input_do_usuario, rigidez_de_horario)
    VALUES (p_nome_equipamento, p_nome_fabricante, p_potencia, p_eh_input_do_usuario, p_rigidez_de_horario);
END //

CREATE PROCEDURE AddUsuario(
    IN p_nome VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_senha VARCHAR(255)
)
BEGIN
    INSERT INTO USUARIOS (nome, email, senha)
    VALUES (p_nome, p_email, p_senha);
END //

CREATE PROCEDURE AddHorarioDeUso(
    IN p_inicio TIME,
    IN p_fim TIME,
    IN p_equipamento_id BIGINT UNSIGNED
)
BEGIN
    INSERT INTO HORARIOS_DE_USO (inicio, fim, equipamento_id)
    VALUES (p_inicio, p_fim, p_equipamento_id);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE RemoveEquipamento(
    IN p_equipamento_id BIGINT UNSIGNED
)
BEGIN
    DELETE FROM EQUIPAMENTOS WHERE equipamento_id = p_equipamento_id;
END //

CREATE PROCEDURE RemoveUsuario(
    IN p_usuario_id BIGINT UNSIGNED
)
BEGIN
    DELETE FROM USUARIOS WHERE usuario_id = p_usuario_id;
END //

CREATE PROCEDURE RemoveHorarioDeUso(
    IN p_horario_de_uso_id BIGINT UNSIGNED
)
BEGIN
    DELETE FROM HORARIOS_DE_USO WHERE horario_de_uso_id = p_horario_de_uso_id;
END //

DELIMITER ;