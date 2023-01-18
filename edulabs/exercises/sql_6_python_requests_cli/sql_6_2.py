import configparser
import psycopg2


class DbConnection:
    def __init__(self, filename: str, section: str):
        self.__filename = filename
        self.__section = section
        self.__db_config: dict = dict()

        parser = configparser.ConfigParser()
        parser.read(self.__filename)
        if parser.has_section(section):
            parameters = parser.items(section)
            for param in parameters:
                self.__db_config[param[0]] = param[1]
        else:
            raise Exception()

        # connection
        self.__conn = psycopg2.connect(**self.__db_config)

    @property
    def conn(self):
        return self.__conn


class Bank(DbConnection):

    def __init__(self, account_id: int, owners: list[str], filename: str, section: str):
        super().__init__(filename, section)
        self.__account_num: int = account_id
        self.__owners: list[str] = owners
        self.__balance: float = 0
        self.set_balance()

    @property
    def account_num(self) -> float:
        return self.__account_num

    @property
    def balance(self):
        return self.__balance

    @property
    def owners(self) -> list[str]:
        return self.__owners

    @staticmethod
    def close_connection_and_commit(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            finally:
                args[0].conn.close()

        return wrapper

    def set_balance(self):
        with self.conn.cursor() as cur:
            _query = """ 
                    SELECT balance 
                    FROM accounts a 
                    JOIN account_owners ON a.id = %s;
                    """
            cur.execute(_query, (self.account_num,))
            query = cur.fetchone()
            self.__balance += query[0]


    def _subtract_balance(self, amount: int):
        with self.conn.cursor() as cur:
            _query = """
                    UPDATE accounts 
                    SET balance = balance - %s
                    WHERE id = %s;
            """
            cur.execute(_query, (amount, self.account_num))
        self.__balance -= amount


    def _add_balance(self, amount: int, to_account: int):
        with self.conn.cursor() as cur:
            _query = """
                   UPDATE accounts 
                   SET balance = balance + %s
                   WHERE id = %s;
               """
            cur.execute(_query, (amount, to_account))


    def _transfer_record(self, passport_num: str):
        with self.conn.cursor() as cur:
            _query1 = """
                   INSERT INTO transactions (initiated_by, ts, transaction_type)
                   VALUES
                   (%s, NOW(), 'transfer');
            """
            cur.execute(_query1, (passport_num,))
            query2 = """
                    INSERT INTO transaction_accounts (
                        account_role,
                        transaction_id,
                        account_id
                    )
                    VALUES (
                        'sender',
                        currval(pg_get_serial_sequence('transactions', 'id')),
                        %s
                    );
                    """
            cur.execute(query2, (self.account_num,))


    @close_connection_and_commit
    def transfer(self, to_account: int, amount, initiated_by: str):
        with self.conn:
            with self.conn.cursor() as cur:
                if amount <= self.balance:
                    self._subtract_balance(amount)
                    self._add_balance(amount, to_account)
                    _query = """
                               SELECT passport_num FROM customers
                               WHERE name = %s
                                               """
                    cur.execute(_query, (initiated_by,))
                    passport_num = cur.fetchone()
                    self._transfer_record(passport_num[0])
                    return True


if __name__ == '__main__':
    bank = Bank(2, ['liav', 'Brad Pitt'], 'config_bank.ini', 'postgresql')
    print(bank.transfer(1, 250, 'Brad Pitt'))
