def get_personal_data(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['surname'])
    print(kwargs['phone'])

get_personal_data(name="Алена", surname="Возмищева", phone="+7(953)1234567")
get_personal_data(surname="Возмищева", name="Алена", phone="+7(953)1234567")

print()

def planet_space_address(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
planet_space_address(planet="Земля", star="Солнце", galaxy="Млечный Путь", age=round(4.543e9))

print()

