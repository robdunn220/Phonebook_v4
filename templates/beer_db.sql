CREATE TABLE user (
  id serial PRIMARY KEY,
  name varchar,
  age integer,
  email varchar
);

create table beer (
  id serial PRIMARY KEY,
  name varchar,
  sub-type varchar,
  abv decimal(4,2),
  brewery_id integer REFERENCES brewery (id),
  sub_style_id integer REFERENCES sub_style (id)
);

create table brewery (
  id serial PRIMARY KEY,
  name varchar,
  location varchar
);

create table category (
  id serial PRIMARY KEY,
  name varchar
);

create table style (
  id serial PRIMARY KEY,
  name varchar,
  category_id integer REFERENCES category (id)
);

create table sub_style (
  id serial PRIMARY KEY,
  name varchar,
  style_id integer REFERENCES style (id)
);
