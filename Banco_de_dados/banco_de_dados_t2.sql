-- Cria um novo banco de dados chamado "db_restaurante_t2"
CREATE DATABASE db_restaurante_t2;

-- Seleciona o banco de dados "db_restaurante_t2" para ser utilizado nas próximas operações
USE db_restaurante_t2;

-- Cria uma tabela chamada "PRATOS"
CREATE TABLE PRATOS(
    -- Define a coluna "id" como um número inteiro que será incrementado automaticamente a cada novo registro
    -- Também define como PRIMARY KEY, garantindo que cada prato tenha um identificador único
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- Define a coluna "nome" como um campo de texto do tipo VARCHAR, permitindo até 30 caracteres
    nome VARCHAR(30)
);
