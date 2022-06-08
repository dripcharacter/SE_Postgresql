from flask import Flask, request, send_file
from flask_restx import Resource, Api
from database_CRUD import SCACRUD
import os
import json

app = Flask(__name__)
api = Api(app)


@api.route('/se_data/post/')
class SeDataPost(Resource):
    def post(self):
        sca_db = SCACRUD()
        body_json = request.get_json()
        uuid = body_json.get('uuid')
        user_name = body_json.get('user_name')
        bean_name = body_json.get('bean_name')
        sweettaste = body_json.get('sweettaste')
        sourtaste = body_json.get('sourtaste')
        bittertaste = body_json.get('bittertaste')
        saltytaste = body_json.get('saltytaste')
        scaproperty = body_json.get('scaproperty')
        print(scaproperty)
        print(type(scaproperty))
        sca_db.insertSCA(uuid=uuid, user_name=user_name,
                         column='uuid, user_name, bean_name, sweettaste, sourtaste, bittertaste, saltytaste, scaproperty',
                         data='''\'{uuid}\', \'{user_name}\', \'{bean_name}\', \'{sweettaste}\', \'{sourtaste}\', \'{bittertaste}\', \'{saltytaste}\', \'{scaproperty}\''''.format(
                             uuid=uuid, user_name=user_name, bean_name=bean_name, sweettaste=sweettaste,
                             sourtaste=sourtaste, bittertaste=bittertaste, saltytaste=saltytaste,
                             scaproperty=json.dumps(scaproperty)))

        result = sca_db.readDB(schema='public', table='se_table',
                               column='uuid, table_pk, user_name, bean_name, sweettaste, sourtaste, bittertaste, saltytaste, createat, updatedat',
                               condition='''uuid=\'{uuid}\' AND user_name=\'{user_name}\''''.format(uuid=uuid,
                                                                                                    user_name=user_name))[
            0]
        return {
            'uuid': result[0],
            'table_pk': result[1],
            'user_name': result[2],
            'bean_name': result[3],
            'sweettaste': result[4],
            'sourtaste': result[5],
            'bittertaste': result[6],
            'saltytaste': result[7],
            'createat': result[8].strftime("%m/%d/%Y, %H:%M:%S"),
            'updatedat': result[9].strftime("%m/%d/%Y, %H:%M:%S")
        }


@api.route('/se_data/<uuid:data_uuid>/<string:user_name>/')
class SeDataCRUD(Resource):
    def get(self, data_uuid, user_name):
        data_uuid = str(data_uuid)
        sca_db = SCACRUD()
        result = sca_db.readDB(schema='public', table='se_table',
                               column='uuid, table_pk, user_name, bean_name, sweettaste, sourtaste, bittertaste, saltytaste, createat, updatedat',
                               condition='''uuid=\'{uuid}\' AND user_name=\'{user_name}\''''.format(uuid=data_uuid,
                                                                                                    user_name=user_name))[
            0]
        return {
            'uuid': result[0],
            'table_pk': result[1],
            'user_name': result[2],
            'bean_name': result[3],
            'sweettaste': result[4],
            'sourtaste': result[5],
            'bittertaste': result[6],
            'saltytaste': result[7],
            'createat': result[8].strftime("%m/%d/%Y, %H:%M:%S"),
            'updatedat': result[9].strftime("%m/%d/%Y, %H:%M:%S")
        }

    def put(self, data_uuid, user_name):
        data_uuid = str(data_uuid)
        sca_db = SCACRUD()
        True

    def delete(self, data_uuid, user_name):
        data_uuid = str(data_uuid)
        sca_db = SCACRUD()
        True


@api.route('/se_image/<uuid:data_uuid>/<string:user_name>/')
class SeImageCRUD(Resource):
    def get(self, data_uuid, user_name):
        data_uuid = str(data_uuid)
        sca_db = SCACRUD()
        slug = user_name + '-' + data_uuid[:8]
        sca_db.readSCAImage(user_name=user_name, slug=slug)
        file_name = slug + '.png'
        if os.path.exists(file_name):
            return send_file(file_name, mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
