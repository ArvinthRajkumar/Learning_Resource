CREATE TABLE accounts (
    id        INTEGER PRIMARY KEY,
    email     TEXT    NOT NULL UNIQUE,
    balance   INTEGER NOT NULL DEFAULT 0 CHECK (balance >= 0),
    owner_id  INTEGER REFERENCES accounts(id),
    created   TEXT    DEFAULT CURRENT_DATE
);
INSERT INTO accounts (email, balance) VALUES ('a@x.com', 50), ('b@x.com', 0);
SELECT id, email, balance FROM accounts;
