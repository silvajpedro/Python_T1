CREATE DATABASE db_restaurante_t3;
USE db_restaurante_t3;

CREATE TABLE pratos(
id INT AUTO_INCREMENT PRIMARY KEY,
nome_do_prato VARCHAR(80) NOT NULL,
preco FLOAT
);

INSERT INTO pratos (nome_do_prato, preco) VALUES ('Tacacá', 19.99);
INSERT INTO pratos (nome_do_prato) VALUES ('Escondidinho de Carne Seca');

SELECT * FROM pratos;