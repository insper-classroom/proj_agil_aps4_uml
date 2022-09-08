# APS 4 - Projeto Ágil e Programação Eficaz

## Equipes e Funcionários

Vamos trabalhar com um sistema de equipes parecido com o que vocês implementaram na PagPedia. Nesta modelagem teremos Funcionários, Gerentes e Equipes seguindo as interfaces e relações definidas abaixo. 

![](diagrama.svg)

Crie implementações destas classes em Python no arquivo `impl.py`. Disponibilizamos um conjunto de testes de unidade `test_impl.py` que verifica se sua implementação  está de acordo com o diagrama acima. Para executá-los rode o comando abaixo.

```
pytest
```

## Questões de discussão

1. Segundo a modelagem acima, é possível uma equipe trocar de gerente? 

**COLOQUE SUA RESPOSTA AQUI**

2. O campo `__equipes_que_gerencia` é privado e só possui acesso de leitura via a função `equipes_que_gerencia`. Liste um problema que poderia ocorrer se o atributo fosse público. 

**COLOQUE SUA RESPOSTA AQUI**