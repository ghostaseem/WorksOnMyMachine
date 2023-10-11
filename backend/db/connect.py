import psycopg2


def connect_to_db():
    host = "wommcodefest.postgres.database.azure.com"
    dbname = "listening_ear"
    user = "server_admin"
    password = "GRC@CodeFest2023@"

    # Construct connection string

    conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
    conn = psycopg2.connect(conn_string)
    print("Connection established")

    return conn
