import sqlite3


class Database:
    def __init__(self,baza_manzili):
        self.path_to_db = baza_manzili

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self,sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql,parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data


    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language:str = 'uz'):
        #SQL_EXAMPLE = "INSERT INTO users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO users(id, Name, email, lamguage) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):

        #SQL_EXAMPLE = "SELECT * FROM users where  id=1 AND Name='John'"
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return sql.execute(sql, parameters=parameters, fetchone=True)

    def select_type(self, **kwargs):

        #SQL_EXAMPLE = "SELECT * FROM users where  id=1 AND Name='John'"
        sql = "SELECT * FROM myfiles_menu WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM users WHERE TRUE", commit=True)

    def user_sanash(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)

    def user_qoshish(self,ism: str,tg_id:int, fam: str = None, username:str = None,):
        #SQL_EXAMPLE = "INSERT INTO users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO users(ism,tg_id,fam,username) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(ism,tg_id,fam,username), commit=True)

    def select_all_menu(self):
        sql = """
        SELECT * FROM menu
        """
        return self.execute(sql, fetchall=True)

    def select_maxsulotlar(self, **kwargs):

        #SQL_EXAMPLE = "SELECT * FROM users where  id=1 AND Name='John'"
        sql = "SELECT * FROM maxsulotlar WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def select_all_maxsulotlar(self):
        sql = """
           SELECT * FROM maxsulotlar
           """
        return self.execute(sql, fetchall=True)
def logger(statement):
    print(f"""
    --------------------------------------------------------
    Executing:
    {statement}
    --------------------------------------------------------
""")
