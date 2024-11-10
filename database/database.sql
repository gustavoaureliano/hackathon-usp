
CREATE DATABASE BancoDeDados;

use BancoDeDados;

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

CREATE TABLE IF NOT EXISTS 
HORARIOS_DE_USO (
    horario_de_uso_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    inicio TIME, 
    fim TIME, 
    equipamento_usuario_id BIGINT UNSIGNED NOT NULL, 
    FOREIGN KEY (equipamento_usuario_id) REFERENCES EQUIPAMENTO_USUARIO(equipamento_usuario_id) ON DELETE CASCADE
);



DELIMITER //

CREATE PROCEDURE AddEquipamento(
    IN p_nome_equipamento VARCHAR(255),
    IN p_nome_fabricante VARCHAR(255),
    IN p_potencia DECIMAL(6, 2),
    IN p_eh_input_do_usuario BOOL,
    IN p_rigidez_de_horario TINYINT,
    OUT p_equipamento_id BIGINT UNSIGNED
)
BEGIN
    INSERT INTO EQUIPAMENTOS (nome_equipamento, nome_fabricante, potencia, eh_input_do_usuario, rigidez_de_horario)
    VALUES (p_nome_equipamento, p_nome_fabricante, p_potencia, p_eh_input_do_usuario, p_rigidez_de_horario);
    SET p_equipamento_id = LAST_INSERT_ID();
END //

DELIMITER;

DELIMITER //
CREATE PROCEDURE AddUsuario(
    IN p_nome VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_senha VARCHAR(255),
    OUT p_usuario_id BIGINT UNSIGNED
)
BEGIN
    INSERT INTO USUARIOS (nome, email, senha)
    VALUES (p_nome, p_email, p_senha);
    SET p_usuario_id = LAST_INSERT_ID();
END //
DELIMITER;

DELIMITER //
CREATE PROCEDURE AddHorarioDeUso(
    IN p_inicio TIME,
    IN p_fim TIME,
    IN p_equipamento_usuario_id BIGINT UNSIGNED
)
BEGIN
    INSERT INTO HORARIOS_DE_USO (inicio, fim, equipamento_usuario_id)
    VALUES (p_inicio, p_fim, p_equipamento_usuario_id);
END //
DELIMITER;

DELIMITER //
CREATE PROCEDURE AddEquipamentoUsuario(
    IN p_equipamento_id BIGINT UNSIGNED,
    IN p_usuario_id BIGINT UNSIGNED,
    OUT p_EquipamentoUsuario_id BIGINT UNSIGNED
)
BEGIN
    INSERT INTO EQUIPAMENTO_USUARIO (equipamento_id, usuario_id)
    VALUES (p_equipamento_id, p_usuario_id);
    SET p_EquipamentoUsuario_id = LAST_INSERT_ID();
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

CREATE PROCEDURE RemoveEquipamentoUsuario(
    IN p_equipamento_usuario_id BIGINT UNSIGNED
)
BEGIN
    DELETE FROM EQUIPAMENTO_USUARIO WHERE equipamento_usuario_id = p_equipamento_usuario_id;
END //

DELIMITER ;


DELIMITER //
CREATE PROCEDURE LoginUsuario(
    IN p_nome VARCHAR(255),
    IN p_senha VARCHAR(255),
    OUT p_result INT
)
BEGIN
    DECLARE usuario_count INT;

    SELECT COUNT(*)
    INTO usuario_count
    FROM USUARIOS
    WHERE nome = p_nome AND senha = p_senha;

    IF usuario_count = 1 THEN
        SET p_result = 1;
    ELSE
        SET p_result = 0;
    END IF;
END //

DELIMITER ; 

DELIMITER //


DELIMITER //

CREATE PROCEDURE GetEquipamentosByUsuario(
    IN p_usuario_id BIGINT UNSIGNED
)
BEGIN
    SELECT e.equipamento_id, e.nome_equipamento, e.nome_fabricante, e.potencia
    FROM EQUIPAMENTOS e
    JOIN EQUIPAMENTO_USUARIO eu ON e.equipamento_id = eu.equipamento_id
    WHERE eu.usuario_id = p_usuario_id;
END //

DELIMITER ;


DELIMITER //

CREATE PROCEDURE GetEquipamentosEHorariosByUsuario(
    IN p_usuario_id BIGINT UNSIGNED
)
BEGIN
    SELECT 
        e.equipamento_id,
        e.nome_equipamento,
        e.nome_fabricante,
        e.potencia,
        h.inicio AS horario_inicio,
        h.fim AS horario_fim
    FROM 
        EQUIPAMENTOS e
    JOIN 
        EQUIPAMENTO_USUARIO eu ON e.equipamento_id = eu.equipamento_id
    JOIN 
        HORARIOS_DE_USO h ON eu.equipamento_usuario_id = h.equipamento_usuario_id
    WHERE 
        eu.usuario_id = p_usuario_id;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetHorariosByEquipamentoUsuario(
    IN p_equipamento_usuario_id BIGINT UNSIGNED
)
BEGIN
    SELECT 
        horario_de_uso_id,
        inicio AS horario_inicio,
        fim AS horario_fim
    FROM 
        HORARIOS_DE_USO
    WHERE 
        equipamento_usuario_id = p_equipamento_usuario_id;
END //

DELIMITER ;