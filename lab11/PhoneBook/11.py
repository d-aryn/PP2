import psycopg2
import csv
from config import load_config

def connect(config):
    conn = psycopg2.connect(**config)
    print('Connected')
    return conn

def create_table(conn):
    command = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) UNIQUE NOT NULL,
        phone VARCHAR(20)
    );
    """
    cur = conn.cursor()
    cur.execute(command)
    conn.commit()
    cur.close()

def insert_from_csv(conn, csv_path):
    csvfile = open(csv_path, mode='r', newline='', encoding='utf-8')
    reader = csv.DictReader(csvfile)
    cur = conn.cursor()
    for row in reader:
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s) ON CONFLICT (name) DO NOTHING;", 
                    (row['name'], row['phone']))
    conn.commit()
    cur.close()
    csvfile.close()
    print("Data inserted successfully")

def insert_console(conn):
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s) ON CONFLICT (name) DO NOTHING;", 
                (name, phone))
    conn.commit()
    cur.close()
    print("Record inserted successfully")

def update(conn):
    name = input("Enter the name to update: ").strip()
    new_value = input("Enter new phone: ").strip()
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s;", (new_value, name))
    conn.commit()
    cur.close()
    print("Updated successfully")

def query(conn):
    print("Query options:\n1. All records\n2. Filter by name\n3. Filter by phone")
    choice = input("Enter your choice (1/2/3): ").strip()
    sql = ""
    value = None
    if choice == "1":
        sql = "SELECT id, name, phone FROM phonebook;"
    elif choice == "2":
        name = input("Enter the name to search: ").strip()
        sql = "SELECT id, name, phone FROM phonebook WHERE name ILIKE %s;"
        value = f"%{name}%"
    elif choice == "3":
        phone = input("Enter the phone to search: ").strip()
        sql = "SELECT id, name, phone FROM phonebook WHERE phone ILIKE %s;"
        value = f"%{phone}%"
    else:
        print("Invalid option")
        return
    cur = conn.cursor()
    if value is None:
        cur.execute(sql)
    else:
        cur.execute(sql, (value,))
    records = cur.fetchall()
    cur.close()
    if records:
        for record in records:
            print(f"ID: {record[0]}, Name: {record[1]}, Phone: {record[2]}")
    else:
        print("No records found")

def delete(conn):
    name = input("Enter the name of the record to delete: ").strip()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name = %s;", (name,))
    conn.commit()
    cur.close()
    print("Record deleted successfully")

def clear_db(conn):
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS phonebook;")
    conn.commit()
    cur.close()
    print("Database cleared successfully")

def search_by_pattern(conn):
    pattern = input("Enter search pattern: ").strip()
    search_pattern = f"%{pattern}%"
    sql = "SELECT id, name, phone FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s;"
    cur = conn.cursor()
    cur.execute(sql, (search_pattern, search_pattern))
    records = cur.fetchall()
    cur.close()
    if records:
        for record in records:
            print(f"ID: {record[0]}, Name: {record[1]}, Phone: {record[2]}")
    else:
        print("No records found")

def upsert_by_name_phone(conn):
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s) ON CONFLICT (name) DO UPDATE SET phone = EXCLUDED.phone;", 
                (name, phone))
    conn.commit()
    cur.close()
    print("User upserted successfully")

def batch_upsert_users(conn):
    names = []
    phones = []
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        phone = input("Phone: ").strip()
        names.append(name)
        phones.append(phone)
    cur = conn.cursor()
    cur.execute("SELECT * FROM upsert_many_users(%s, %s);", (names, phones))
    incorrect = cur.fetchall()
    conn.commit()
    cur.close()
    if incorrect:
        for row in incorrect:
            print(f"Name: {row[0]}, Phone: {row[1]}")
    else:
        print("Все пользователи обработаны корректно")

def query_with_pagination(conn):
    limit = int(input("Введите лимит: ").strip())
    offset = int(input("Введите смещение (offset): ").strip())
    cur = conn.cursor()
    cur.execute("SELECT id, name, phone FROM phonebook LIMIT %s OFFSET %s;", (limit, offset))
    records = cur.fetchall()
    cur.close()
    if records:
        for record in records:
            print(f"ID: {record[0]}, Name: {record[1]}, Phone: {record[2]}")
    else:
        print("Записи не найдены для данной страницы")

def delete_by_username_or_phone(conn):
    choice = input("Удалить по:\n1. Name\n2. Phone\nВведите выбор (1/2): ").strip()
    if choice == "1":
        value = input("Введите name: ").strip()
        field = "name"
    elif choice == "2":
        value = input("Введите phone: ").strip()
        field = "phone"
    else:
        print("Неверный выбор")
        return
    cur = conn.cursor()
    cur.execute(f"DELETE FROM phonebook WHERE {field} = %s;", (value,))
    conn.commit()
    cur.close()
    print("Запись удалена успешно")

def upsert(conn):
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s) ON CONFLICT (name) DO UPDATE SET phone = EXCLUDED.phone;", (name, phone))
    conn.commit()
    cur.close()
    print("User upserted successfully")

def batch_upsert(conn):
    limit = int(input("Введите лимит записей для пакетного обновления: ").strip())
    records = []
    for i in range(limit):
        name = input("Имя: ").strip()
        if not name:
            break
        phone = input("Телефон: ").strip()
        records.append((name, phone))
    cur = conn.cursor()
    cur.executemany(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s) ON CONFLICT (name) DO UPDATE SET phone = EXCLUDED.phone;", 
        records
    )
    conn.commit()
    cur.close()
    print("Все пользователи обработаны корректно")

def paginated_query(conn):
    limit = int(input("Введите лимит: ").strip())
    offset = int(input("Введите (offset): ").strip())
    cur = conn.cursor()
    cur.execute("SELECT id, name, phone FROM phonebook LIMIT %s OFFSET %s;", (limit, offset))
    records = cur.fetchall()
    cur.close()
    if records:
        for record in records:
            print(f"ID: {record[0]}, Name: {record[1]}, Phone: {record[2]}")
    else:
        print("Записи не найдены для данной страницы")

def delete_by_field(conn):
    choice = input("Удалить по:\n1. Name\n2. Phone\nВведите выбор (1/2): ").strip()
    if choice == "1":
        value = input("Введите name: ").strip()
        field = "name"
    elif choice == "2":
        value = input("Введите phone: ").strip()
        field = "phone"
    else:
        print("Неверный выбор")
        return
    cur = conn.cursor()
    cur.execute(f"DELETE FROM phonebook WHERE {field} = %s;", (value,))
    conn.commit()
    cur.close()
    print("Запись удалена успешно")

def main():
    config = load_config()
    conn = connect(config)
    create_table(conn)
    while True:
        print("\n1. Insert data from CSV")
        print("2. Insert data in console")
        print("3. Update")
        print("4. Query")
        print("5. Delete by name")
        print("6. Clear database")
        print("7. Exit")
        print("8. Query by pattern")
        print("9. Upsert")
        print("10. Batch upsert")
        print("11. Paginated query")
        print("12. Delete by name or phone")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            csv_path = input("Enter path to CSV file: ").strip()
            insert_from_csv(conn, csv_path)
        elif choice == "2":
            insert_console(conn)
        elif choice == "3":
            update(conn)
        elif choice == "4":
            query(conn)
        elif choice == "5":
            delete(conn)
        elif choice == "6":
            clear_db(conn)
            create_table(conn)
        elif choice == "7":
            break
        elif choice == "8":
            search_by_pattern(conn)
        elif choice == "9":
            upsert(conn)
        elif choice == "10":
            batch_upsert(conn)
        elif choice == "11":
            paginated_query(conn)
        elif choice == "12":
            delete_by_field(conn)
        else:
            print("ERROR")
    conn.close()

if __name__ == "__main__":
    main()