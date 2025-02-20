-- Criando um novo banco de dados chamado "db_restaurante_t3"
CREATE DATABASE db_restaurante_t3;

-- Selecionando o banco de dados "db_restaurante_t3" para ser utilizado
USE db_restaurante_t3;

-- Criando a tabela "pratos"
CREATE TABLE pratos(
    id INT AUTO_INCREMENT PRIMARY KEY,   -- Coluna "id" será a chave primária e terá incremento automático
    nome_do_prato VARCHAR(80) NOT NULL,  -- Coluna "nome_do_prato" armazena o nome do prato (obrigatório)
    preco FLOAT                           -- Coluna "preco" armazenará o preço do prato (pode ser NULL)
);

-- Inserindo um prato com nome e preço
INSERT INTO pratos (nome_do_prato, preco) VALUES ('Tacacá', 19.99);

-- Inserindo um prato sem preço (o valor de "preco" será NULL)
INSERT INTO pratos (nome_do_prato) VALUES ('Escondidinho de Carne Seca');

-- Selecionando todos os registros da tabela "pratos" para visualizar os dados inseridos
SELECT * FROM pratos;
