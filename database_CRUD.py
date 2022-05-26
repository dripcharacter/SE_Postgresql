from database import PostgreSQL_Database as Postgres_DB


class CRUD(Postgres_DB):
    def insertDB(self, schema, table, column, data):
        sql = "INSERT INTO {schema}.{table}({column}) VALUES ({data})".format(schema=schema, table=table, column=column,
                                                                              data=data)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print("insert DB err", e)

    def readDB(self, schema, table, column, condition=None):
        if condition == None:
            sql = "SELECT {column} FROM {schema}.{table}".format(column=column, schema=schema, table=table)
        else:
            sql = "SELECT {column} FROM {schema}.{table} WHERE {condition}".format(column=column, schema=schema,
                                                                                   table=table, condition=condition)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e:
            result = ("read DB err", e)

        return result

    def updateDB(self, schema, table, column, value, condition):
        sql = "UPDATE {schema}.{table} SET ({column})=ROW({value}) WHERE {condition}".format(schema=schema, table=table,
                                                                                             column=column, value=value,
                                                                                             condition=condition)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print("update DB err", e)

    def deleteDB(self, schema, table, condition):
        sql = "DELETE FROM {schema}.{table} WHERE {condition}".format(schema=schema, table=table, condition=condition)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print("delete DB err", e)
