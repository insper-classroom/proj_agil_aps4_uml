from unittest.mock import Mock
import inspect


def test_classes_foram_definidas():
    import impl
    all_classes = inspect.getmembers(impl, inspect.isclass)
    class_names = [c[0] for c in all_classes]
    assert all([
        'Equipe' in class_names,
        'Funcionario' in class_names,
        'Gerente' in class_names,
    ])

def test_Gerente_Herda_de_Funcionario():
    import impl
    assert issubclass(impl.Gerente, impl.Funcionario)


def test_cria_Funcionario():
    import impl
    st =  inspect.signature(impl.Funcionario.__init__) 
    assert len(st.parameters) == 2


    params = list(st.parameters.values())
    assert params[0].name == 'self'
    assert params[1].name == 'nome'

    funcionario = impl.Funcionario('nome 1')
    assert funcionario.nome == 'nome 1'

    funcionario = impl.Funcionario('nome 2')
    assert funcionario.nome == 'nome 2'


def test_Funcionario_Gerente_sem_equipes():
    import impl
    funcionario = impl.Funcionario('nome 1')
    assert funcionario.equipes_que_participa() == []

    gerente = impl.Gerente('nome g')
    assert gerente.equipes_que_participa() == []

def test_cria_Gerente():
    import impl
    st =  inspect.signature(impl.Gerente.__init__) 
    assert len(st.parameters) == 2


    params = list(st.parameters.values())
    assert params[0].name == 'self'
    assert params[1].name == 'nome'

    gerente = impl.Gerente('nome g')
    assert gerente.nome == 'nome g'


def test_Gerente_nao_gerencia_nenhuma_equipe():
    import impl
    gerente = impl.Gerente('nome g')
    assert gerente.equipes_que_gerencia() == []

def test_cria_Equipe():
    import impl
    st =  inspect.signature(impl.Equipe.__init__) 
    assert len(st.parameters) == 3


    params = list(st.parameters.values())
    assert params[0].name == 'self'
    assert params[1].name == 'nome'
    assert params[2].name == 'gerente'

    gerente = impl.Gerente('nome g')
    equipe = impl.Equipe('nome 1', gerente)

    assert equipe.nome == 'nome 1'
    assert equipe.gerente() == gerente
    assert equipe.componentes() == [gerente]


def test_adiciona_Funcionario_a_Equipe():
    import impl
    gerente = impl.Gerente('nome g')
    funcionario = impl.Funcionario('nome 1')
    equipe = impl.Equipe('nome 1', gerente)
    equipe.add_componente(funcionario)

    assert funcionario in equipe.componentes()
    assert gerente in equipe.componentes()

    assert equipe in funcionario.equipes_que_participa()
    assert funcionario in equipe.componentes()

    funcionario2 = impl.Funcionario('nome 2')
    funcionario2.add_equipe(equipe)
    assert equipe in funcionario2.equipes_que_participa()
    assert funcionario2 in equipe.componentes()



def test_Gerente_com_tres_equipes():
    import impl
    gerente = impl.Gerente('nome g')
    
    equipe1 = impl.Equipe('nome 1', gerente)
    equipe2 = impl.Equipe('nome 2', gerente)
    equipe3 = impl.Equipe('nome 3', gerente)

    assert equipe1 in gerente.equipes_que_gerencia()
    assert equipe2 in gerente.equipes_que_gerencia()
    assert equipe3 in gerente.equipes_que_gerencia()


def test_lista_subordinados_tres_Equipes_mesmo_Gerente():
    import impl
    funcionarios = [impl.Funcionario(f'nome {i}') for i in range(6)]
    gerente = impl.Gerente('g')

    equipes = [impl.Equipe(f'e {i}', gerente) for i in range(3)]
    for i in range(6):
        equipes[i % 3].add_componente(funcionarios[i])
    
    subordinados = gerente.lista_subordinados()
    assert all([func in subordinados for func in funcionarios])


def test_lista_subordinados_tres_Equipes_dois_Gerente():
    import impl
    funcionarios = [impl.Funcionario(f'nome {i}') for i in range(7)]
    gerentes = [impl.Gerente('g'), impl.Gerente('g2')]

    equipes = [impl.Equipe(f'e {i}', gerentes[i % 2]) for i in range(3)]
    
    for i in range(7):
        equipes[i % 3].add_componente(funcionarios[i])
    
    equipes[0].add_componente(funcionarios[6])
    equipes[1].add_componente(funcionarios[6])
    equipes[2].add_componente(funcionarios[6])
    
    subordinados1 = set(gerentes[0].lista_subordinados())
    subordinados1_correto = set(equipes[0].componentes() + equipes[2].componentes())
    assert subordinados1 == subordinados1_correto

    subordinados2 = set(gerentes[1].lista_subordinados())
    subordinados2_correto = set(equipes[1].componentes())
    assert subordinados2 == subordinados2_correto
