from database_CRUD import CRUD
from sunburst_chart import sunburst, json_to_list, json_data
import json
import uuid

if __name__=="__main__":
    db=CRUD()
    # print(db.readDB(schema='public', table='se_table', column='scaproperty, sweettaste, sourtaste', condition='id=2'))
    # db.updateDB(schema='public', table='se_table', column='sweettaste, sourtaste, bittertaste', value='30, 40, 50', condition='id>=1')
    # print(db.readDB(schema='public', table='se_table', column='*'))
    # db.deleteDB(schema='public', table='se_table', condition='id=10')
    # db.insertDB(schema='public', table='se_table', column='uuid, sweettaste, sourtaste, bittertaste, saltytaste, user_name, bean_name, scaproperty', data='''\'{uuid}\', \'{sweettaste}\', \'{sourtaste}\', \'{bittertaste}\', \'{saltytaste}\', \'{user_name}\', \'{bean_name}\', \'{scaproperty}\''''.format(uuid=uuid.uuid4(), sweettaste=76, sourtaste=53, bittertaste=46, saltytaste=11, user_name="mashiro", bean_name="test_bean", scaproperty=json.dumps(json_data)))
    result=db.readDB(schema='public', table='se_table', column='*')
    print(result[0][4])
    print(type(result[0][4]))

#TODO: updateDB를 할때 자동으로 last_modified_time을 now()로 업데이트하도록하는 것
#TODO: insertDB, updateDB, deleteDB를 할 때 그에 따른 scaproperty를 기반으로 한 sunburst chart를 생성 및 저장할 db_table 생성 및 앞의 3 작업을 할 때 자동으로 업데이트 하도록 하기
