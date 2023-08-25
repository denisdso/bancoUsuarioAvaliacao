from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    # Achar usuário
    def user_exists(self, name):
        return any(user.name == name for user in self.store.bd)

    # metodo novo
    def add_user(self, name, job):
        if isinstance(name, str) and isinstance(job, str) and name is not None and job is not None:
            if self.user_exists(name):
                return "Usuário com mesmo nome já existe"

            user = User(name, job)
            self.store.bd.append(user)
            return "Usuário Adicionado"
        else:
            return "Parâmetros inválidos"

    def remove_user(self, name, job):
        if isinstance(name, str) and isinstance(job, str) and name is not None and job is not None:
            if self.user_exists(name):
                user_to_remove = next((user for user in self.store.bd if user.name == name and user.job == job), None)
                if user_to_remove:
                    self.store.bd.remove(user_to_remove)
                    return "Usuário Removido"
                else:
                    return "Usuário não encontrado"
            else:
                return "Usuário não encontrado"
        else:
            return "Parâmetros inválidos"

    def update_user(self, name, job, new_name, new_job):
        if isinstance(name, str) and isinstance(job, str) and \
                isinstance(new_name, str) and isinstance(new_job, str) \
                and name is not None and job is not None and \
                new_name is not None and new_job is not None:
            if self.user_exists(name):
                user_to_update = next((user for user in self.store.bd if user.name == name and user.job == job), None)
                if user_to_update:
                    user_to_update.name = new_name
                    user_to_update.job = new_job
                    return "Usuário Atualizado"
                else:
                    return "Usuário não encontrado"
            else:
                return "Usuário não encontrado"
        else:
            return "Parâmetros inválidos"

    def get_user_by_name(self, name, job):
        if isinstance(name, str) and isinstance(job, str) and name is not None and job is not None:
            user = next((user for user in self.store.bd if user.name == name), None)
            if user:
                return f"Nome: {user.name}, Cargo: {user.job}"
            else:
                return "Usuário não encontrado"
        else:
            return "Parâmetros inválidos"
