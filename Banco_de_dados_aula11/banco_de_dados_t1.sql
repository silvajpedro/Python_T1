-- Criando um banco de dados chamado "db_restaurante_t1"
CREATE DATABASE db_restaurante_t1; 

-- Selecionando o banco de dados para uso
USE db_restaurante_t1; 

-- Criando a tabela "pratos" com as colunas:
-- - "id": identificador único, gerado automaticamente (AUTO_INCREMENT) e chave primária (PRIMARY KEY)
-- - "nome_prato": nome do prato, com no máximo 100 caracteres e obrigatório (NOT NULL)
-- - "preco": preço do prato, obrigatório (NOT NULL)
CREATE TABLE pratos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_prato VARCHAR(100) NOT NULL,
    preco INT NOT NULL
);

-- Exibindo todas as tabelas dentro do banco de dados selecionado
SHOW TABLES; 

-- Exibindo a estrutura da tabela "pratos"
DESC pratos; 

-- Inserindo registros (pratos) na tabela "pratos"
INSERT INTO pratos (nome_prato, preco) VALUES ('Churrasco com batata frita', 50);
INSERT INTO pratos (nome_prato, preco) VALUES ('Tacacá', 35);
INSERT INTO pratos (nome_prato, preco) VALUES ('Escondidinho', 45);

-- Inserindo múltiplos registros de uma vez
INSERT INTO pratos (nome_prato, preco) VALUES
    ('Feijoada', 45),
    ('Frango Assado', 50),
    ('Lasanha', 25),
    ('Escondidinho', 30);

-- Modificando a estrutura da tabela para garantir que a coluna "nome_prato" continue sendo VARCHAR(100)
ALTER TABLE pratos MODIFY COLUMN nome_prato VARCHAR(100); 

-- Selecionando e exibindo todos os registros da tabela "pratos"
SELECT * FROM pratos; 

-- Excluindo o prato com ID = 5 da tabela "pratos"
DELETE FROM pratos WHERE id = 5;

-- Desativando o modo de segurança do MySQL (cuidado ao executar DELETE sem WHERE!)
SET SQL_SAFE_UPDATES = 0; 

-- Excluindo todos os registros que possuem "nome_prato" = 'Lasanha'
DELETE FROM pratos WHERE nome_prato = 'Lasanha';

-- Tentativa de excluir um prato específico chamado "Lasanha" com ID = 2 
DELETE FROM pratos WHERE nome_prato = 'Lasanha' AND id = 2;

-- Excluindo todos os registros da tabela "pratos" (CUIDADO: Isso remove todos os dados!)
DELETE FROM pratos;
