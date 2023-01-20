from flask import Flask, jsonify, request
from handy_funcs.configs.ini_config import get_config
import psycopg2

conn = psycopg2.connect(**get_config('config.ini', 'postgresql'))

app = Flask('webank')


@app.route('/api/v1/accounts/<int:account_id>', methods=['GET'])
def accounts(customer_id):
    with conn:
        try:
            with conn.cursor() as cur:
                query = r'SELECT * FROM accounts a WHERE a.id = %s'
                cur.execute(query, (customer_id,))
                return jsonify(cur.fetchone())
        except Exception as e:
            message = {
                "status": 404,
                "message": "Account not found",
                "error": str(e)
            }
            return jsonify(message), 404


@app.route('/api/v1/accounts/all', methods=['GET'])
def accounts_all():
    with conn:
        try:
            with conn.cursor() as cur:
                query = r'SELECT * FROM accounts a'
                cur.execute(query)
                return jsonify(cur.fetchall())
        except Exception as e:
            message = {
                "status": 404,
                "message": "Accounts not found",
                "error": str(e)
            }
            return jsonify(message), 404


@app.route('/api/v1/accounts/<int:account_id>')
def accounts_balance_params():
    balance = request.args.get('balance', default=None, type=int)
    max_limit = request.args.get('limit', default=None, type=int)
    query = """SELECT * FROM accounts a WHERE 1=1"""
    with conn:
        try:
            with conn.cursor() as cur:
                if balance:
                    query += "AND a.balance = %s "
                    cur.execute(query, (balance,))
                    return jsonify(cur.fetchall())
                if max_limit:
                    query += "LIMIT %s"
                    cur.execute(query, (max_limit,))
                    return jsonify(cur.fetchall())
        except Exception as e:
            message = {
                "status": 400,
                "message": "Request failed",
                "error": str(e)
            }
            return jsonify(message), 400


@app.route('/api/v1/accounts/', methods=['POST'])
def accounts_add():
    account_id = request.form.get('account_id', default=None, type=int)
    customer_ids = request.form.getlist('customer_ids', type=int)
    with conn:
        try:
            with conn.cursor() as cur:
                query = r"""
                    INSERT INTO accounts(customer_id, account_id)
                    VALUES( %s, %s)
                    """
                for customer in customer_ids:
                    cur.execute(query, (customer, account_id))
                return 'True'
        except Exception as e:
            message = {
                "status": 400,
                "message": "Bad request",
                "error": str(e)
            }
            return jsonify(message), 400


@app.route('/api/v1/accounts/<int:account_id>/deposit')
def account_deposit(account_id):
    amount = request.form.get('amount', default=0, type=int)
    with conn:
        try:
            with conn.cursor() as cur:
                query1 = """ 
                INSERT INTO
                transactions(initiated_by, ts, transaction_type)
                VALUES
                (%s, NOW(), 'deposit');
                """

                query2 = """
                UPDATE accounts a
                SET a.balance = a.balance + %s
                WHERE a.id = %s
                """
            cur.execute(query2, (amount, account_id))
            cur.execute(query1, account_id)
            return True

        except Exception as e:
            message = {
                "status": 400,
                "message": "Bad request",
                "error": str(e)
            }
            return jsonify(message), 400


@app.route('/api/v1/accounts/<int:account_id>/withdraw')
def account_withdraw(account_id):
    amount = request.form.get('amount', default=0, type=int)
    with conn:
        try:
            with conn.cursor() as cur:
                query1 = """ 
                INSERT INTO
                transactions(initiated_by, ts, transaction_type)
                VALUES
                (%s, NOW(), 'withdraw');
                """

                query2 = """
                UPDATE accounts a
                SET a.balance = a.balance - %s
                WHERE a.id = %s
                """
            cur.execute(query2, (amount, account_id))
            cur.execute(query1, account_id)
            return True

        except Exception as e:
            message = {
                "status": 400,
                "message": "Bad request",
                "error": str(e)
            }
            return jsonify(message), 400


@app.route('/api/v1/accounts/<int:account_id>/transfer')
def account_transfer(account_id):
    amount = request.form.get('amount', default=0, type=int)
    to_account = request.form.get('to_account_id', default=0, type=int)
    with conn:
        try:
            with conn.cursor() as cur:
                query0 = """ 
                SELECT passport_num 
                FROM customers
                WHERE id = %s
                """

                query1 = """ 
                INSERT INTO
                transactions(initiated_by, ts, transaction_type)
                VALUES
                (%s, NOW(), 'transfer');
                """

                query2 = """
                UPDATE accounts a
                SET a.balance = a.balance - %s
                WHERE a.id = %s
                """

                query3 = """
                UPDATE accounts a
                SET a.balance = a.balance + %s
                WHERE a.id = %s
                """

                query4 = """
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
            cur.execute(query0, account_id)
            passport_num = cur.fetchone()[0]
            cur.execute(query1, passport_num)
            cur.execute(query2, (amount, account_id))
            cur.execute(query3, (amount, to_account))
            cur.execute(query4, (amount, account_id))
            return True
        except Exception as e:
            message = {
                "status": 400,
                "message": "Bad request",
                "error": str(e)
            }
            return jsonify(message), 400


@app.route('/api/v1/accounts/<int:account_id>', methods=['DELETE'])
def accounts_delete(account_id):
    with conn:
        try:
            with conn.cursor() as cur:
                query1 = """
                DELETE FROM transaction_accounts 
                WHERE account_id = %s;
                """

                query2 = """
                DELETE FROM account_owners
                WHERE account_id = %s;
                """

                query3 = """
                DELETE FROM accounts a
                WHERE a.id = %s
                """
                cur.execute(query1, (account_id,))
                cur.execute(query2, (account_id,))
                cur.execute(query3, (account_id,))
                return 'True'
        except Exception as e:
            message = {
                "status": 404,
                "message": "Accounts not found",
                "error": str(e)
            }
            return jsonify(message), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)
