-- Criando um novo banco de dados chamado "db_restaurante_t2"
CREATE DATABASE db_restaurante_t2; 

-- Selecionando o banco de dados para utilização
USE db_restaurante_t2; 

-- Criando a tabela "pratos" com as colunas:
-- - "id": identificador único (chave primária), gerado automaticamente (AUTO_INCREMENT)
-- - "nome": nome do prato, obrigatório (NOT NULL)
-- - "preco": preço do prato, podendo ser nulo
CREATE TABLE pratos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    preco INT
);

-- Criando a tabela "sobremesas" com a mesma estrutura da tabela "pratos"
CREATE TABLE sobremesas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    preco INT
);

-- Exibindo a estrutura da tabela "pratos"
DESC pratos; 

-- Inserindo registros na tabela "pratos"
-- Apenas o nome do prato, sem definir um preço (o valor de "preco" será NULL)
INSERT INTO pratos(nome) VALUES ("Tacacá"); 

-- Inserindo um prato com nome e preço
INSERT INTO pratos(nome, preco) VALUES ('Lasanha de Macarrão com Queijo', 50);

-- Inserindo outro prato sem especificar o preço
INSERT INTO pratos(nome) VALUES ("Baião De Dois");

-- Exibindo todos os registros da tabela "pratos"
SELECT * FROM pratos; 

-- Exibindo todos os registros da tabela "sobremesas"
SELECT * FROM sobremesas;

-- Apagando a tabela "pratos", removendo sua estrutura e todos os dados armazenados
DROP TABLE pratos; 

-- Tentativa de modificar a coluna "preco" para FLOAT (este comando falhará se a tabela "pratos" já tiver sido deletada)
ALTER TABLE pratos MODIFY COLUMN preco FLOAT; 

-- Inserindo um novo prato com nome e preço decimal
INSERT INTO pratos(nome, preco) VALUES ("Baião De Dois", 29.90);

-- Exibindo os dados da tabela "pratos"
SELECT * FROM pratos;

-- Inserindo múltiplos registros de pratos de uma vez
INSERT INTO pratos (nome, preco) VALUES 
    ("Macarrão ao Molho Branco", 25.99),
    ("X-tudo", 12.99),
    ("Estrogonofe de Frango", 49.99),
    ("Pizza", 29.99),
    ("Hambúrguer", 16.99);

-- Exibindo novamente todos os pratos cadastrados
SELECT * FROM pratos;

-- Excluindo todos os registros que tenham o nome "Baião De Dois"
DELETE FROM pratos WHERE nome = "Baião De Dois"; 

-- Excluindo o registro específico onde o nome seja "Macarrão ao Molho Branco" e o ID seja 10
DELETE FROM pratos WHERE nome = "Macarrão ao Molho Branco" AND id = 10; 

-- Exibindo novamente os registros para conferir as exclusões
SELECT * FROM pratos;

-- Excluindo todos os registros da tabela "pratos" (mas mantendo a estrutura da tabela)
DELETE FROM pratos;

-- Exibindo a tabela novamente (agora vazia)
SELECT * FROM pratos;

-- Desativando o modo de segurança do MySQL, permitindo updates e deletes sem WHERE
SET SQL_SAFE_UPDATES = 0;
