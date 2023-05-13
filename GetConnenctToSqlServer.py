import pyodbc
import pyttsx3

engine = pyttsx3.init()


def Get_Connect_To_SqlServer(servername, databasename, username=None, password=None):
    conn_string = f"DRIVER={{SQL Server}};SERVER={servername};DATABASE={databasename}"

    if username is not None:
        conn_string += f";UID={username};PWD={password}"
    else:
        conn_string += ";Trusted_Connection=yes"
    
    try:
        conn = pyodbc.connect(conn_string)
        engine.say(f"Successfully connected to {databasename}")
        engine.runAndWait()
        print(f"Successfully connected to {servername}/{databasename}")
        return conn
    except pyodbc.Error as e:
        engine.say(f"Error connecting to {databasename}")
        engine.runAndWait()
        print(f"Error connecting to {servername}/{databasename}: {e}")
        return None


def start():
    engine.say("Hello !,Wellcome to test connection application.")
    engine.runAndWait()
    engine.say("For testing connection to your database please enter database name,server name and table name, if you have a username and password enter in commend input!,else leave theme empty.")
    engine.runAndWait()
    servername = input("Enter Server Name :\n")
    databasename = input("Enter Database Name :\n")
    tableName = input("Enter Table Name :\n")
    username = input("Enter Username :\n")
    password = input("Enter Password :\n")
    if username == None:
        conn = Get_Connect_To_SqlServer(servername,databasename)
    else :
        conn = Get_Connect_To_SqlServer(servername,databasename,username,password)
    if servername==None and username == None:
        conn = Get_Connect_To_SqlServer(".",databasename)
    elif servername==None and username is not None:
        conn = Get_Connect_To_SqlServer(".",databasename,username,password)
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {tableName}')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()
    if conn is None:
        engine.say("No Connetction Founded!")
        engine.runAndWait()
        print("No Connetction Founded!")        

start()