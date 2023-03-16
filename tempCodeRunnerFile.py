contact_name = 'hom'
from main import *
with open('contact_name.txt','r') as f:
    names_str = f.read()
    contact_name_list= names_str.split('\n')
        
with open('contact_no.txt','r') as f:
    no_str = f.read()
    contact_no_list= no_str.split('\n')
print(contact_name_list)
print(contact_no_list)
for i in range(len(contact_name_list)):
    if contact_name_list[i] in contact_name:
        print(contact_name_list[i])
        print(contact_no_list[i])
print(dir(send_message))