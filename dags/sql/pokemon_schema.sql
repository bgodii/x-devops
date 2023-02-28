-- create pet table
CREATE TABLE IF NOT EXISTS pokemon (
    create_on DATE not null default CURRENT_DATE,
    update_on DATE not null default CURRENT_DATE,
    pokemon_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    weight INTEGER NOT NULL,
    abilities VARCHAR[]);