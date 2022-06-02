import psycopg2

from database import PostgreSQL_Database as Postgres_DB
from sunburst_chart import sunburst, json_to_list
import matplotlib.pyplot as plt
import os
import sys


class CRUD(Postgres_DB):
    def __init__(self, host='localhost', dbname='se_db', user='se_project', password='se_project', port=5432):
        super().__init__(host, dbname, user, password, port)

    def insertDB(self, schema, table, column, data):
        sql = "INSERT INTO {schema}.{table}({column}) VALUES ({data})".format(schema=schema, table=table, column=column,
                                                                              data=data)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print("insert DB err", e)

    def readDB(self, schema, table, column, condition=None):
        if condition is None:
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
        if table != 'se_image_table':
            column = column + ', updatedat'
            value = value + ', now()'
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


class SCACRUD(CRUD):
    def __init__(self, host='localhost', dbname='se_db', user='se_project', password='se_project', port=5432):
        super().__init__(host, dbname, user, password, port)

    def insertSCA(self, column, data, user_name, uuid, schema='public', table='se_table'):
        self.insertDB(schema=schema, table=table, column=column, data=data)
        property_bool = False
        for entry in column.split(', '):
            if entry == 'scaproperty':
                property_bool = True
                break

        if property_bool:
            uuid_first = uuid[:8]
            slug = user_name + '-' + uuid_first
            scaproperty = self.readDB(schema=schema, table=table, column='scaproperty',
                                      condition='''uuid=\'{uuid}\' AND user_name=\'{user_name}\''''.format(uuid=uuid,
                                                                                                           user_name=user_name))[
                0][0]
            scaproperty = json_to_list(scaproperty)
            sunburst(scaproperty)
            plt.savefig(slug + '.png')
            filename = './' + slug + '.png'
            pngfile = open(filename, 'rb')
            pngfiledata = psycopg2.Binary(pngfile.read())
            self.insertDB(schema=schema, table='se_image_table', column='user_name, slug, image',
                          data='''\'{user_name}\', \'{slug}\', {image}'''.format(user_name=user_name, slug=slug,
                                                                                 image=pngfiledata))
            pngfile.close()
            if os.path.isfile(filename):
                os.remove(filename)
            plt.clf()
            print('insertSCA finished')

    def readSCAImage(self, user_name, slug, column='image', condition=None, schema='public', table='se_image_table'):
        image_data=bytes(self.readDB(schema=schema, table=table, column=column, condition='''slug=\'{slug}\' AND user_name=\'{user_name}\''''.format(slug=slug, user_name=user_name))[0][0])
        fout=None
        filename='./' + slug + '.png'
        fout=open(filename, 'wb')
        fout.write(image_data)
        fout.close()
        print('readSCAImage finished')

    def updateSCA(self, column, value, user_name, uuid, condition, schema='public', table='se_table'):
        self.updateDB(schema=schema, table=table, column=column, value=value, condition=condition)
        property_bool = False
        for entry in column.split(', '):
            if entry == 'scaproperty':
                property_bool = True
                break

        if property_bool:
            uuid_first = uuid[:8]
            slug = user_name + '-' + uuid_first
            scaproperty = self.readDB(schema=schema, table=table, column='scaproperty',
                                      condition='''uuid=\'{uuid}\' AND user_name=\'{user_name}\''''.format(uuid=uuid,
                                                                                                           user_name=user_name))[
                0][0]
            scaproperty = json_to_list(scaproperty)
            sunburst(scaproperty)
            plt.savefig(slug + '.png')
            filename = './' + slug + '.png'
            pngfile = open(filename, 'rb')
            pngfiledata = psycopg2.Binary(pngfile.read())
            self.updateDB(schema=schema, table='se_image_table', column='image', value='''{image}'''.format(image=pngfiledata), condition='''slug=\'{slug}\' AND user_name=\'{user_name}\''''.format(slug=slug, user_name=user_name))
            pngfile.close()
            if os.path.isfile(filename):
                os.remove(filename)
            plt.clf()
            print('updateSCA finished')

    def deleteSCA(self, condition, schema='public', table='se_table'):
        tmp=self.readDB(schema=schema, table=table, column='uuid, user_name', condition=condition)
        wanted_uuid=tmp[0][0]
        wanted_user_name=tmp[0][1]
        self.deleteDB(schema=schema, table=table, condition=condition)
        self.deleteDB(schema=schema, table=table, condition='''slug=\'{slug}\' AND user_name=\'{user_name}\''''.format(slug=wanted_user_name+'-'+wanted_uuid[:8], user_name=wanted_user_name))
        print('deleteSCA finished')
