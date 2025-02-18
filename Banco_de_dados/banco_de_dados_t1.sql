-- Cria um novo banco de dados chamado "db_restaurante_t1"
CREATE DATABASE db_restaurante_t1;

-- Seleciona o banco de dados "db_restaurante_t1" para ser utilizado nas próximas operações
USE db_restaurante_t1;

-- Cria uma tabela chamada "PRATOS"
CREATE TABLE PRATOS(
    -- Define a coluna "id" como um número inteiro, que será incrementado automaticamente a cada novo registro
    -- Também a define como PRIMARY KEY, ou seja, uma chave primária única para identificar cada prato
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- Define a coluna "idade" como um número inteiro (aparentemente não faz sentido para pratos, talvez tenha sido um erro)
    preco INT,

    -- Define a coluna "nome" como um campo de texto do tipo VARCHAR, podendo armazenar até 50 caracteres
    nome VARCHAR(50)
);
