# Name: Ashutosh Bhati
# Roll No.: 0863CS241045

def print_anything(**data):
    for key, value in data.items():
        print(f'{key} = {value}')


print_anything(name='Ashutosh Bhati')
print_anything(id=1001, e_name='Ashutosh Bhati', company='google', salary=20000000)
