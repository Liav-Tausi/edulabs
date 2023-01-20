from flask import Flask, jsonify, request
from handy_funcs.configs.ini_config import get_config
import psycopg2

conn = psycopg2.connect(**get_config('config.ini', 'postgresql'))

app = Flask('webank')


# GET user's info
@app.route('/api/v1/customers/<int:customer_id>', methods=['GET'])
def customers(customer_id):
    with conn:
        try:
            with conn.cursor() as cur:
                query = r'SELECT * FROM customers c WHERE c.id = %s'
                cur.execute(query, (customer_id,))
                return jsonify(cur.fetchone())
        except Exception as e:
            message = {
                "status": 404,
                "message": "Customer not found",
                "error": str(e)
            }
            return jsonify(message), 404


# GET all users
@app.route('/api/v1/customers/all', methods=['GET'])
def customers_all():
    with conn:
        try:
            with conn.cursor() as cur:
                query = r'SELECT * FROM customers c'
                cur.execute(query)
                return jsonify(cur.fetchall())
        except Exception as e:
            message = {
                "status": 404,
                "message": "Customer not found",
                "error": str(e)
            }
            return jsonify(message), 404


# GET user's accounts
@app.route('/api/v1/customers/<int:customer_id>/accounts', methods=['GET'])
def customers_accounts(customer_id):
    with conn:
        try:
            with conn.cursor() as cur:
                query = r"""
                    SELECT ac.* 
                    FROM customers c 
                    JOIN account_owners ao ON ao.customer_id = c.id 
                    JOIN accounts ac ON ac.id = ao.account_id 
                    WHERE c.id = %s
                    """
                cur.execute(query, (customer_id,))
                return jsonify(cur.fetchone())
        except Exception as e:
            message = {
                "status": 404,
                "message": "Customer not found",
                "error": str(e)
            }
            return jsonify(message), 404


# GET customer by params
@app.route('/api/v1/customers/', methods=['GET'])
def customers_params():
    name = request.args.get('name', default=None, type=str)
    address = request.args.get('address', default=None, type=str)
    page_num = request.args.get('page_num', default=1, type=int)
    result_per_page = request.args.get('result_per_page', default=20, type=int)
    if name and address is not None:
        with conn:
            try:
                with conn.cursor() as cur:
                    if name is None:
                        query = r"""
                            SELECT * 
                            FROM customers c 
                            WHERE c.address ILIKE %s
                            LIMIT %s OFFSET (%s - 1) * %s
                            """
                        cur.execute(query, (name, result_per_page, page_num, result_per_page))
                        return cur.fetchmany(result_per_page)
                    elif address is None:
                        query = r"""
                           SELECT * 
                           FROM customers c 
                           WHERE c.name ILIKE %s
                           LIMIT %s OFFSET (%s - 1) * %s
                           """
                        cur.execute(query, (name, result_per_page, page_num, result_per_page))
                        return cur.fetchmany(result_per_page)
                    else:
                        query = r"""
                           SELECT * 
                           FROM customers c 
                           WHERE c.name ILIKE %s AND c.address ILIKE %s
                           LIMIT %s OFFSET (%s - 1) * %s
                           """
                        cur.execute(query, (name, result_per_page, page_num, result_per_page))
                        return cur.fetchmany(result_per_page)
            except Exception as e:
                message = {
                    "status": 404,
                    "message": "Customer not found",
                    "error": str(e)
                }
                return jsonify(message), 404
    else:
        message = {
            "status": 400,
            "message": "Customer not found",
        }
        return jsonify(message), 400


# ADD customer
@app.route('/api/v1/customers/', methods=['POST'])
def customers_add():
    name = request.form.get('name', default=None, type=str)
    address = request.form.get('address', default=None, type=str)
    passport = request.form.get('passport', default=None, type=int)
    with conn:
        try:
            with conn.cursor() as cur:
                query = r"""
                    INSERT INTO customers(passport_num, name, address)
                    VALUES(%s, %s, %s)
                    """
                cur.execute(query, (passport, name, address))
                return 'True'
        except Exception as e:
            message = {
                "status": 400,
                "message": "Bad request",
                "error": str(e)
            }
            return jsonify(message), 400


# UPDATE customer
@app.route('/api/v1/customers/<int:customer_id>', methods=['PUT'])
def customers_update(customer_id):
    name = request.form.get('name', default=None, type=str)
    address = request.form.get('address', default=None, type=str)
    passport = request.form.get('passport', default=None, type=int)
    with conn:
        try:
            with conn.cursor() as cur:
                query = r"""
                    UPDATE customers c
                    SET passport_num = %s, address = %s, name = %s
                    WHERE c.id = %s
                    """
                cur.execute(query, (passport, name, address, customer_id))
                return 'True'
        except Exception as e:
            message = {
                "status": 404,
                "message": "Customer not found",
                "error": str(e)
            }
            return jsonify(message), 400


# DELETE customer
@app.route('/api/v1/customers/<int:customer_id>', methods=['DELETE'])
def customers_delete(customer_id):
    with conn:
        try:
            with conn.cursor() as cur:
                query = r"""
                    DELETE FROM customers c
                    WHERE c.id = %s
                    """
                cur.execute(query, (customer_id,))
                return 'True'
        except Exception as e:
            message = {
                "status": 404,
                "message": "Customer not found",
                "error": str(e)
            }
            return jsonify(message), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)
