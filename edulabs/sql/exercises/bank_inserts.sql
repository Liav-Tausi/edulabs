

INSERT INTO
	customers (passport_num, customer_name, address)
values
	(123456789, 'Brad Pitt', 'California');

INSERT INTO
	customers (passport_num, customer_name, address)
values
	(101010101, 'Angelina Jolie', 'California');


INSERT INTO
	accounts(account_num, max_limit, balance, allowd_usd)
values
	(123, 10000000, 50000, TRUE);

INSERT INTO
	accounts (account_num, max_limit, balance, allowd_usd)
values
	(3432, 5000000, 20000, FALSE);


INSERT INTO customers_accounts (customer_id, account_id)
VALUES(2, 2);
