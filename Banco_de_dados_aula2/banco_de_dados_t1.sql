-- Criando o banco de dados chamado "db_restaurante_t1"
CREATE DATABASE db_restaurante_t1;

-- Selecionando o banco de dados para uso (antes de criar tabelas ou inserir dados)
USE db_restaurante_t1;

-- Criando a tabela "pratos"
CREATE TABLE pratos(
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Coluna "id" será a chave primária e terá incremento automático
    nome_prato VARCHAR(100) NOT NULL,     -- Coluna "nome_prato" para armazenar o nome do prato
    preco INT NOT NULL                  -- Coluna "preco" armazenando o preço do prato (em número inteiro, sem casas decimais)
);

-- Exibindo todas as tabelas existentes dentro do banco de dados atual
SHOW TABLES;

-- Exibindo a estrutura da tabela "pratos" (mostra colunas, tipos de dados e restrições)
DESC pratos;

-- Inserindo registros (pratos) na tabela "pratos"
INSERT INTO pratos (nome_prato, preco) VALUES ('Churrasco com batata frita', 50);  
INSERT INTO pratos (nome_prato, preco) VALUES ('Tacacá', 35);
INSERT INTO pratos (nome_prato, preco) VALUES ('Escondidinho', 45);

-- Selecionando todos os registros da tabela "pratos" (exibe os dados armazenados)
SELECT * FROM pratos;
