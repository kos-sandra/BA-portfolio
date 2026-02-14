import pandas as pd
import psycopg2

# Параметры подключения
conn_params = {
    "host": "localhost",
    "database": "opensource_minfin",
    "user": "postgres",
    "password": "123",
    "port": "5432"
}

with psycopg2.connect(**conn_params) as conn:
    df = pd.read_sql("SELECT * FROM repayment_schedule_of_the_state_external_debt", conn)


print(df.head())


# print(len(df))