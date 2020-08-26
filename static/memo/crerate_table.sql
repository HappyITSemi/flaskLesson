create table todo_category
(
    id   serial      not null
        constraint todo_category_pk
            primary key,
    name varchar(24) not null,
    due  timestamp
);

alter table category
    owner to admin;

create table todo
(
    id                  serial   not null
        constraint todo_pk
            primary key,
    name                char(24) not null,
    description         char(128),
    due_date            timestamp,
    created_at          timestamp,
    updated_at          timestamp,
    "todo_category_id " integer
        constraint todo_todo_category_fk
            references category
);

alter table todo
    owner to admin;