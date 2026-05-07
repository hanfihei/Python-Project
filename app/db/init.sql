CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price INT,
    description TEXT,
    tags TEXT,
    weight DOUBLE PRECISION,
    embedding VECTOR(1536)
);