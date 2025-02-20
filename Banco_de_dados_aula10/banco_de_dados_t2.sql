-- Criando um novo banco de dados chamado "db_restaurante_t2"
CREATE DATABASE db_restaurante_t2;

-- Selecionando o banco de dados "db_restaurante_t2" para uso
USE db_restaurante_t2;

-- Criando a tabela "pratos"
CREATE TABLE pratos(
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Coluna "id" será a chave primária e terá incremento automático
    nome VARCHAR(80) NOT NULL,          -- Coluna "nome" armazena o nome do prato, com limite de 80 caracteres e sem permitir valores nulos
    preco INT                            -- Coluna "preco" armazenará o preço do prato (pode ser nulo)
);

-- Exibindo a estrutura da tabela "pratos" (mostra colunas, tipos de dados e restrições)
DESC pratos;

-- Inserindo um prato chamado "Tacacá" na tabela "pratos"
-- A coluna "preco" permite NULL, mas não foi informada.
INSERT INTO pratos(nome) VALUES ("Tacacá");

-- Selecionando todos os registros da tabela "pratos" (exibe os dados armazenados)
SELECT * FROM pratos;

-- Excluindo a tabela "pratos" (remove todos os dados e a estrutura da tabela permanentemente)
DROP TABLE pratos;