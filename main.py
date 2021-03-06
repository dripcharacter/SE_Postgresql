from database_CRUD import CRUD, SCACRUD
from sunburst_chart import sunburst, json_to_list, json_data, json_fake
import matplotlib.pyplot as plt
import json
import uuid
import os

if __name__ == "__main__":
    # db = CRUD()
    # print(db.readDB(schema='public', table='se_table', column='scaproperty, sweettaste, sourtaste', condition='id=2'))
    # db.updateDB(schema='public', table='se_table', column='sweettaste, sourtaste, bittertaste', value='30, 40, 50', condition='id>=1')
    # print(db.readDB(schema='public', table='se_table', column='*'))
    # db.deleteDB(schema='public', table='se_table', condition='id=10')

    # db.insertDB(schema='public', table='se_table',
    #             column='uuid, sweettaste, sourtaste, bittertaste, saltytaste, user_name, bean_name, scaproperty',
    #             data='''\'{uuid}\', \'{sweettaste}\', \'{sourtaste}\', \'{bittertaste}\', \'{saltytaste}\',
    #             \'{user_name}\', \'{bean_name}\', \'{scaproperty}\''''.format(
    #                 uuid=uuid.uuid4(), sweettaste=76, sourtaste=53, bittertaste=46, saltytaste=11, user_name="mashiro",
    #                 bean_name="test_bean", scaproperty=json.dumps(json_data)))
    # db.updateDB(schema='public', table='se_table', column='sweettaste, sourtaste, bittertaste', value='30, 40, 50',
    #             condition='table_pk<=1')
    # result = db.readDB(schema='public', table='se_table', column='scaproperty',
    #                    condition='''table_pk=1 AND user_name=\'mashiro\'''')

    sca_db = SCACRUD()
    tmp_uuid = str(uuid.uuid4())
    print(tmp_uuid)
    sca_db.insertSCA(uuid=tmp_uuid, user_name='mashiro', schema='public', table='se_table',
                     column='uuid, sweettaste, sourtaste, bittertaste, saltytaste, user_name, bean_name, scaproperty',
                     data='''\'{uuid}\', \'{sweettaste}\', \'{sourtaste}\', \'{bittertaste}\', \'{saltytaste}\', 
                \'{user_name}\', \'{bean_name}\', \'{scaproperty}\''''.format(
                         uuid=tmp_uuid, sweettaste=76, sourtaste=53, bittertaste=46, saltytaste=11, user_name="mashiro",
                         bean_name="test_bean", scaproperty=json.dumps(json_data)))
    sca_db.readSCAImage(user_name='mashiro', slug='mashiro-' + tmp_uuid[:8])
    sca_db.updateSCA(column='sweettaste, bittertaste, saltytaste, scaproperty',
                     value='''\'{sweettaste}\', \'{bittertaste}\', \'{saltytaste}\', \'{scaproperty}\''''.format(
                         sweettaste=99, bittertaste=99, saltytaste=99, scaproperty=json.dumps(json_fake)),
                     user_name='mashiro', uuid=tmp_uuid,
                     condition='''uuid=\'{uuid}\' AND user_name=\'{user_name}\''''.format(uuid=tmp_uuid,
                                                                                          user_name='mashiro'))
    sca_db.readSCAImage(user_name='mashiro', slug='mashiro-' + tmp_uuid[:8])
    result=sca_db.readDB(schema='public', table='se_table',
                               column='uuid, table_pk, user_name, bean_name, sweettaste, sourtaste, bittertaste, saltytaste, createat, updatedat',
                               condition='''uuid=\'{uuid}\' AND user_name=\'{user_name}\''''.format(uuid=tmp_uuid,
                                                                                                    user_name='mashiro'))[0]
    print(result)
    print(type(result))
    # sca_db.deleteSCA(condition='''uuid=\'{uuid}\' AND user_name=\'{user_name}\''''.format(uuid=tmp_uuid, user_name='mashiro'))
    print('mashiro-'+tmp_uuid[:8]+'.png')
    print(os.path.exists('mashiro-'+tmp_uuid[:8]+'.png'))
    # sca_db.readSCAImage(user_name='mashiro', slug='mashiro-' + tmp_uuid[:8])

# TODO: updateDB??? ?????? ???????????? last_modified_time??? now()??? ??????????????????????????? ???
# TODO: insertDB, updateDB, deleteDB??? ??? ??? ?????? ?????? scaproperty??? ???????????? ??? sunburst chart??? ?????? ??? ????????? db_table ?????? ??? ?????? 3 ????????? ??? ??? ???????????? ???????????? ????????? ??????
