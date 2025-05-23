import psycopg2


def insert_employee(first_name, last_name, d_o_b, age, phone_no):
    try:
        conn = psycopg2.connect(
            database="person_data",
            user="postgres",
            password="jaihind",
            host="127.0.0.1",
            port="5432",
        )

        cur = conn.cursor()

        cur.execute(
            "CREATE TABLE IF NOT EXISTS employees (id SERIAL PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), d_o_b VARCHAR(255), age int, phone_no VARCHAR(255))"
        )
        conn.commit()

        cur.execute(
            "INSERT INTO employees (first_name, last_name, d_o_b, age, phone_no) VALUES (%s, %s, %s, %s, %s)",
            (first_name, last_name, d_o_b, age, phone_no),
        )
        conn.commit()

        cur.close()
        conn.close()
        return True 

    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return False  
