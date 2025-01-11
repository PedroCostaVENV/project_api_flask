-- Cria um banco de dados para armazenar informações sobre carros

USE Pycodebr;

-- Cria a tabela 'carros' com as colunas:
--  - id: Identificador único para cada carro
--  - marca: Marca do carro
--  - modelo: Modelo do carro
--  - ano: Ano de fabricação
CREATE TABLE carros (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, -- Chave primária auto-incremental
    marca VARCHAR(100) NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    ano INT
);

SET character set_client = utf8;
SET character set connection = utf8;
SET character set results = utf8;
SET collation connection = utf8_general_ci;

-- Insere vários carros na tabela
INSERT INTO carros (marca, modelo, ano) VALUES
    ('Fiat', 'Marea', 1999),
    ('Fiat', 'Uno', 1992),
    ('Ford', 'Escort', 1985),
    ('Chevrolet', 'Chevette', 1978),
    ('Volkswagen', 'Fusca', 1962);