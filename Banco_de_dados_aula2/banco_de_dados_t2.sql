CREATE DATABASE db_restaurante_t2;

USE db_restaurante_t2;

CREATE TABLE pratos(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(80) NOT NULL,
preco INT
);

DESC pratos;

INSERT INTO pratos(nome) VALUES ("Tacacá");

SELECT * FROM pratos;

DROP TABLE pratos;
