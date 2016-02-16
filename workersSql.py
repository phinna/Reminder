import sqlite3

# DATABASE = "ptt.db"
class DBManager(object):

    @classmethod
    def create_table(cls, database, table):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE {tb}
                (firstName TEXT, lastName TEXT, email TEXT)""".format(tb=table))
        conn.close()

    @classmethod
    def insert_data_to_table(cls, database, table, contacts):
        with sqlite3.connect(database) as connection:
            c = connection.cursor()
            c.executemany('INSERT INTO %s(firstName, lastName, email) \
                    values (?, ?, ?)' % table, contacts)

    @classmethod
    def get_email(cls, database, table, names):
        emails = []
        with sqlite3.connect(database) as connection:
            c = connection.cursor()
            for name in names:
                name = name.split()[0].capitalize()
                c.execute("SELECT email from %s WHERE firstName='%s'" \
                                                            % (table, name))

                emails.append(c.fetchone())
            return emails


