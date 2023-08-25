from src import service
from src.service.service_user import ServiceUser
from src.models.store import Store
from src.models.user import User



# user_1 = User("Maria", "Engenheiro")
# print(user_1.name)
# print(user_1.job)
#
# print("######")
#
# user_2 = User("Maria2", "Engenheiro2")
# print(user_2.name)
# print(user_2.job)
#
# store = Store()
# store.bd.append(user_1)
# store.bd.append(user_2)
# print(store.bd)
# print(store.bd[0].name)
#
# service = ServiceUser()
# resultado = service.add_user("eduarda", "engenharia")
# print(resultado)
# resultado = service.add_user("maria", "TI")
# print(resultado)
# print(service.store.bd[0].name)
# print(service.store.bd[1].job)

service = ServiceUser()
print("////////********////////")

resultado = service.add_user("Maria", "engenharia")
#resultado = service.remove_user("eduarda", "engenharia")
print(resultado)

resultado2 = service.get_user_by_name("Maria", "engenharia")
#resultado = service.remove_user("eduarda", "engenharia")
print(resultado2)

resultado2 = service.update_user("Maria", "engenharia", "eduarda", "teste")
#resultado = service.remove_user("eduarda", "engenharia")
print(resultado2)
