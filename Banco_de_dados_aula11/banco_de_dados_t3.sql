-- Criando um novo banco de dados chamado "db_restaurante_t3"
CREATE DATABASE db_restaurante_t3; 

-- Selecionando o banco de dados para uso
USE db_restaurante_t3; 

-- Desativando o modo de segurança do MySQL, permitindo atualizações e exclusões sem restrições
SET SQL_SAFE_UPDATES = 0; 

-- Criando a tabela "pratos" com as colunas:
-- - "id": identificador único, gerado automaticamente (AUTO_INCREMENT) e chave primária (PRIMARY KEY)
-- - "nome_do_prato": nome do prato, obrigatório (NOT NULL)
-- - "preco": preço do prato, podendo aceitar valores decimais (FLOAT)
CREATE TABLE pratos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_do_prato VARCHAR(80) NOT NULL,
    preco FLOAT
);

-- Criando a tabela "sobremesa" com a mesma estrutura da tabela "pratos"
CREATE TABLE sobremesa(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_do_prato VARCHAR(80) NOT NULL,
    preco FLOAT
);

-- Inserindo registros na tabela "sobremesa"
INSERT INTO sobremesa (nome_do_prato, preco) VALUES 
    ("Pudim", 12),
    ("Pavê", 10.99),
    ("Bolo de Pote", 14),
    ("Mousse de Maracujá", 8.99),
    ("2 Litros de Açaí", 89.99);

-- Exibindo todos os registros da tabela "pratos" (neste momento, ela está vazia)
SELECT * FROM pratos;

-- Exibindo todos os registros da tabela "sobremesa"
SELECT * FROM sobremesa; 

-- Inserindo um novo registro na tabela "sobremesa"
INSERT INTO sobremesa (nome_do_prato, preco) VALUES ("Torta de Queijo com Goiabada", 14.99);

-- Tentativa de excluir um registro pelo ID (falhará se o ID 10 não existir)
DELETE FROM sobremesa WHERE id = 10;

-- Excluindo todos os registros onde "nome_do_prato" for "2 Litros de Açaí"
DELETE FROM sobremesa WHERE nome_do_prato = "2 Litros de Açaí";

-- Tentativa de excluir um registro com "TORTA DE QUEIJO COM GOIABADA" (sensível a maiúsculas/minúsculas no MySQL por padrão)
DELETE FROM sobremesa WHERE nome_do_prato = "TORTA DE QUEIJO COM GOIABADA";

-- Excluindo todos os registros da tabela "sobremesa", mas mantendo sua estrutura
DELETE FROM sobremesa;

-- Exibindo todos os registros da tabela "sobremesa" (agora vazia)
SELECT * FROM sobremesa;
