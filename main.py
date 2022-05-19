from database_CRUD import CRUD

if __name__=="__main__":
    db=CRUD()
    db.insertDB(schema='public', table='se_table', column='scaproperty, sweettaste, sourtaste, bittertaste, user_name', data='\'{{"An space exists",StrawBerry,"space exists?"},{"Caramel yes","Caramelized No",SoTasty}}\', \'10\', \'20\', \'30\', \'mashiro\'')
    print(db.readDB(schema='public', table='se_table', column='scaproperty, sweettaste, sourtaste'))
    print(db.readDB(schema='public', table='se_table', column='scaproperty, sweettaste, sourtaste', condition='id=2'))
    db.updateDB(schema='public', table='se_table', column='sweettaste, sourtaste, bittertaste', value='30, 40, 50', condition='id>=1')
    print(db.readDB(schema='public', table='se_table', column='*'))
    db.deleteDB(schema='public', table='se_table', condition='id=10')