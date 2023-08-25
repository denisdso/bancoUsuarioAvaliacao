from src.service.service_user import ServiceUser

class TestServiceUser:

    def test_add_user_com_sucesso(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuário Adicionado"

        # Chamada
        resultado = service.add_user("Maria", "Analista")

        # Avaliação
        assert resultado == resultado_esperado

    def test_add_user_com_mesmo_nome(self):
        # Setup
        service = ServiceUser()
        service.add_user("maria", "Analista")
        resultado_esperado = "Usuário com mesmo nome já existe"

        # Chamada
        resultado = service.add_user("maria", "smith")

        # Avaliação
        assert resultado == resultado_esperado

    def test_add_user_com_nome_invalido(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.add_user(1236, "Analista")

        # Avaliação
        assert resultado == resultado_esperado

    def test_add_user_com_job_invalido(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.add_user("Maria", 123)

        # Avaliação
        assert resultado == resultado_esperado

    def test_add_user_sem_informar_nome(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.add_user(None, "Analista")

        # Avaliação
        assert resultado == resultado_esperado

    def test_add_user_sem_informar_job(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.add_user("Maria", None)

        # Avaliação
        assert resultado == resultado_esperado

    def test_remove_user(self):
        # Setup
        service = ServiceUser()
        service.add_user("maria", "ene")
        resultado_esperado = "Usuário Removido"

        # Chamada
        resultado = service.remove_user("maria", "ene")

        # Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_nao_encontrado(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuário não encontrado"

        # Chamada
        resultado = service.remove_user("joao", "engenheiro")

        # Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_com_nome_invalido(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.remove_user(123, "engenheiro")

        # Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_com_job_invalido(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.remove_user("Maria", 123)

        # Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_sem_informar_nome(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.remove_user(None, "Analista")

        # Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_sem_informar_job(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.remove_user("Maria", None)

        # Avaliação
        assert resultado == resultado_esperado

    def test_update_user(self):
        # Setup
        service = ServiceUser()
        service.add_user("maria", "ene")
        resultado_esperado = "Usuário Atualizado"

        # Chamada
        resultado = service.update_user("maria", "ene", "maria", "engenheira")

        # Avaliação
        assert resultado == resultado_esperado

    def test_update_user_nao_encontrado(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuário não encontrado"

        # Chamada
        resultado = service.update_user("joao", "engenheiro", "joana", "cientista")

        # Avaliação
        assert resultado == resultado_esperado

    def test_update_user_com_nome_invalido(self):
        # Setup
        service = ServiceUser()
        service.add_user("maria", "ene")
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.update_user("maria", "ene", 1236, "engenheira")

        # Avaliação
        assert resultado == resultado_esperado

    def test_update_user_com_job_invalido(self):
        # Setup
        service = ServiceUser()
        service.add_user("maria", "ene")
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.update_user("maria", "ene", "maria", 123)

        # Avaliação
        assert resultado == resultado_esperado

    def test_update_user_sem_informar_nome(self):
        # Setup
        service = ServiceUser()
        service.add_user("maria", "ene")
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.update_user("maria", "ene", None, 123)

        # Avaliação
        assert resultado == resultado_esperado

    def test_update_user_sem_informar_job(self):
        # Setup
        service = ServiceUser()
        service.add_user("maria", "ene")
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.update_user("maria", "ene", "Maria", None)

        # Avaliação
        assert resultado == resultado_esperado

    def test_get_user_by_name(self):
        # Setup
        service = ServiceUser()
        service.add_user("maria", "ene")
        resultado_esperado = "Nome: maria, Cargo: ene"

        # Chamada
        resultado = service.get_user_by_name("maria", "ene")

        # Avaliação
        assert resultado == resultado_esperado

    def test_get_user_by_name_nao_encontrado(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuário não encontrado"

        # Chamada
        resultado = service.get_user_by_name("joao", "engenheiro")

        # Avaliação
        assert resultado == resultado_esperado

    def test_get_user_com_nome_invalido(self):
        # Setup
        service = ServiceUser()
        service.add_user("maria", "ene")
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.get_user_by_name(123, "ene")

        # Avaliação
        assert resultado == resultado_esperado

    def test_get_user_com_job_invalido(self):
        # Setup
        service = ServiceUser()
        service.add_user("maria", "ene")
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.get_user_by_name("maria", 123)

        # Avaliação
        assert resultado == resultado_esperado

    def test_get_user_sem_informar_nome(self):
        # Setup
        service = ServiceUser()
        service.add_user("maria", "Analista")
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.get_user_by_name(None, "Analista")

        # Avaliação
        assert resultado == resultado_esperado

    def test_get_user_sem_informar_job(self):
        # Setup
        service = ServiceUser()
        service.add_user("maria", "Analista")
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = service.get_user_by_name("maria", None)

        # Avaliação
        assert resultado == resultado_esperado

