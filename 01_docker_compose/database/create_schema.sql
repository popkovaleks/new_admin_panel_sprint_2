CREATE SCHEMA IF NOT EXISTS content;

--Создаем таблицу с фильмами
CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type TEXT NOT NULL,
    created TIMESTAMP WITH TIME ZONE,
    modified TIMESTAMP WITH TIME ZONE
);

-- Создаем таблицу person
CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name TEXT NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
);

-- Создаем связующую таблицу для film_work и person
CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL,
    person_id uuid NOT NULL,
    role TEXT NOT NULL,
    created timestamp with time zone
); 

-- Создаем таблицу жанров
CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created timestamp with time zone,
    modified timestamp with time zone
);

-- Создаем связующую таблицу для жанров и фильмов
CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid PRIMARY KEY,
    genre_id uuid NOT NULL,
    film_work_id uuid NOT NULL,
    created timestamp with time zone
);

-- Создаем индекс для таблицы film_work по полю creation_date
create index film_work_creation_date_idx on content.film_work(creation_date);


-- Создаем индекс по имени для таблицы person
CREATE INDEX person_full_name_idx on content.person (full_name);

-- Создаем индекс по названию для таблицы genre
CREATE INDEX genre_name_idx on content.genre (name);

-- Уникальный индекс для таблицы genre_film_work
CREATE UNIQUE INDEX genre_film_work_idx on content.genre_film_work (film_work_id, genre_id);