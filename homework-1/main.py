"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv
import psycopg2


def insert_tables(file, insert_param, tabl_name):
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='71806')
    try:
        with conn.cursor() as cur:
            with open(file, newline='', encoding='cp1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for read in reader:
                    cur.execute(f'INSERT INTO {tabl_name} VALUES ({insert_param})', read)
                    conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":

    file_customers_data = 'north_data/customers_data.csv'
    tabl_name_customers = 'customers'
    insert_param_customers_data = "%(customer_id)s, %(company_name)s, %(contact_name)s"
    insert_tables(file_customers_data, insert_param_customers_data, tabl_name_customers)

    file_employees_data = 'north_data/employees_data.csv'
    tabl_name_employees = 'employees'
    insert_param_employees_data = "%(first_name)s, %(last_name)s, %(title)s, %(birth_date)s, %(notes)s"
    insert_tables(file_employees_data, insert_param_employees_data, tabl_name_employees)

    file_orders_data = 'north_data/orders_data.csv'
    tabl_name_orders = 'orders'
    insert_param_orders_data = "%(order_id)s, %(customer_id)s, %(employee_id)s, %(order_date)s, %(ship_city)s"
    insert_tables(file_orders_data, insert_param_orders_data, tabl_name_orders)
