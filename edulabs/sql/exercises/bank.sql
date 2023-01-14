
CREATE TABLE accounts(
	id SERIAL PRIMARY KEY,
	account_num BIGINT UNIQUE NOT NULL,
	max_limit BIGINT NOT NULL,
	balance NUMERIC NOT NULL,
	allowd_usd BOOL NOT NULL
);



CREATE TABLE customers(
	id SERIAL PRIMARY KEY,
	passport_num BIGINT NOT NULL,
	customer_name VARCHAR(64) NOT NULL,
	address VARCHAR(128) NOT NULL
);



CREATE TABLE customers_accounts(
	id SERIAL PRIMARY KEY,
	account_id INT NOT NULL,
	customer_id INT NOT NULL,
	FOREIGN KEY (customer_id) REFERENCES customers(id),
	FOREIGN KEY (account_id) REFERENCES accounts(id)
);



CREATE TABLE transactions(
	id SERIAL PRIMARY KEY,
	t_type VARCHAR(64) CHECK (t_type IN ('withdraw','deposit','transfer')),
	amount BIGINT NOT NULL,
	t_timestamp TIMESTAMP NOT NULL,
	t_action_placer INT NOT NULL,
	sender INT,
	resiver INT,
	FOREIGN KEY (t_action_placer) REFERENCES customers(id),
	FOREIGN KEY (sender) REFERENCES accounts(id),
	FOREIGN KEY (resiver) REFERENCES accounts(id)
);
















