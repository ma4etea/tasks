CREATE SCHEMA catalog;

CREATE TABLE catalog.units
(
    id        serial PRIMARY KEY,
    code      text,
    name      text,
    precision integer
);

CREATE TABLE catalog.products
(
    id          serial PRIMARY KEY,
    name        text,
    description text,
    unit_id     integer   NOT NULL,
    create_at   TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_products_units
        FOREIGN KEY (unit_id) REFERENCES catalog.units (id) ON DELETE RESTRICT
);

CREATE TABLE catalog.prices
(
    id         serial PRIMARY KEY,
    product_id integer   NOT NULL,
    price      numeric(18, 3),
    create_at  TIMESTAMP NOT NULL DEFAULT now(),
    CONSTRAINT fk_prices_products
        FOREIGN KEY (product_id) REFERENCES catalog.products ON DELETE RESTRICT
);



CREATE SCHEMA warehouse;

CREATE TABLE warehouse.stock_movements
(
    id             serial PRIMARY KEY,
    product_id     integer NOT NULL,
    quantity_delta numeric(18, 3),
    CONSTRAINT fk_stock_movements_products
        FOREIGN KEY (product_id) REFERENCES catalog.products (id) ON DELETE RESTRICT
);

CREATE TABLE warehouse.product_stock
(
    product_id integer NOT NULL,
    quantity   numeric(18, 3),
    CONSTRAINT fk_product_stock_products
        FOREIGN KEY (product_id) REFERENCES catalog.products (id) ON DELETE CASCADE
);



CREATE SCHEMA employees;



CREATE SCHEMA operations;
CREATE TABLE operations.transactions
(
    id        serial PRIMARY KEY,
--     employe_id INTEGER
    create_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE operations.add_stocks
(
    id                serial PRIMARY KEY,
    transaction_id    INTEGER NOT NULL,
    stock_movement_id INTEGER NOT NULL,
    cost_price        NUMERIC(18, 3),
    CONSTRAINT fk_add_stocks_transactions
        FOREIGN KEY (transaction_id) REFERENCES operations.transactions (id),
    CONSTRAINT fk_add_stocks_stock_movement
        FOREIGN KEY (stock_movement_id) REFERENCES warehouse.stock_movements (id)
);

CREATE TABLE operations.stock_returns
(
    add_stock_id      integer NOT NULL,
    transaction_id    integer NOT NULL,
    stock_movement_id integer NOT NULL,
    CONSTRAINT fk_stock_returns_add_stocks
        FOREIGN KEY (add_stock_id)
            REFERENCES operations.add_stocks (id) ON DELETE RESTRICT,
    CONSTRAINT fk_stock_returns_transactions
        FOREIGN KEY (transaction_id)
            REFERENCES operations.transactions (id) ON DELETE RESTRICT,
    CONSTRAINT fk_stock_returns_stock_movements
        FOREIGN KEY (stock_movement_id)
            REFERENCES warehouse.stock_movements (id) ON DELETE RESTRICT
);

CREATE TABLE operations.new_prices
(
    price_id       integer NOT NULL,
    transaction_id integer NOT NULL,
    CONSTRAINT fk_new_prices_prices
        FOREIGN KEY (price_id) REFERENCES catalog.prices (id),
    CONSTRAINT fk_new_prices_transactions
        FOREIGN KEY (transaction_id) REFERENCES operations.transactions (id)
);

CREATE TABLE operations.write_off
(
    stock_movement_id integer NOT NULL,
    transaction_id    integer NOT NULL,
    CONSTRAINT fk_write_off_stock_movements
        FOREIGN KEY (stock_movement_id) REFERENCES warehouse.stock_movements (id),
    CONSTRAINT fk_write_off_transactions
        FOREIGN KEY (transaction_id) REFERENCES operations.transactions (id)
);

CREATE TABLE operations.sales
(
    id                serial PRIMARY KEY,
    stock_movement_id integer NOT NULL,
    price_id          integer NOT NULL,
    transaction_id    integer NOT NULL,
    final_price       numeric(18, 3),
    CONSTRAINT fk_sales_stock_movements
        FOREIGN KEY (stock_movement_id)
            REFERENCES warehouse.stock_movements (id) ON DELETE RESTRICT,
    CONSTRAINT fk_sales_prices
        FOREIGN KEY (price_id)
            REFERENCES catalog.prices (id) ON DELETE RESTRICT,
    CONSTRAINT fk_sales_transactions
        FOREIGN KEY (transaction_id)
            REFERENCES operations.transactions (id) ON DELETE RESTRICT
);

CREATE TABLE operations.sales_returns
(
    sale_id           integer NOT NULL,
    stock_movement_id integer NOT NULL,
    transaction_id    integer NOT NULL,
    CONSTRAINT fk_sales_returns_sales
        FOREIGN KEY (sale_id)
            REFERENCES operations.sales (id) ON DELETE RESTRICT,
    CONSTRAINT fk_sales_returns_stock_movements
        FOREIGN KEY (stock_movement_id)
            REFERENCES warehouse.stock_movements (id) ON DELETE RESTRICT,
    CONSTRAINT fk_sales_returns_transactions
        FOREIGN KEY (transaction_id)
            REFERENCES operations.transactions (id) ON DELETE RESTRICT
);
