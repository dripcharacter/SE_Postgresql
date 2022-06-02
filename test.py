test_str = 'I am minseok'
print(test_str)
test_str = test_str + ', sorry I am mashiro.'
print(test_str)
test_str = 'sweettaste, sourtaste, bittertaste, scaproperty'
print(test_str.split(', '))
for entry in test_str.split(', '):
    if entry=='scaproperty':
        print(entry)
test_str='scproperty, saproperty, SCAPROPERTY, seaproperty'
for entry in test_str.split(', '):
    if entry=='scaproperty':
        print(entry)

uuid='b1d813b6-ff69-44d6-8f95-927ffcc070b9'
username='mashiro'
print(username+'-'+uuid[:8])