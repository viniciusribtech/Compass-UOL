# Resumo da Sprint 03
## O que aprendi?
Essa sprint num modo geral foi um pouco menos exaustiva que as duas primeiras, os exercícios e desafio não apresentaram grande dificuldade, mas em particular, tive muitos problemas em compreender como funciona o Docker, e principalmente com diretórios na hora de montar o código.

## Primeira semana:
A sprint se iniciou com a apresentação do Docker, ferramenta que nunca tinha sequer ouvido falar. Mas, mesmo assim, a instalação dela na minha máquina não apresentou problemas. Comecei a seguir a trilha, vendo as videoaulas e anotando no bloco de notas as informações fundamentais, resolvi disponibilizar uma das anotações na pasta Evidências.

Além disso, o tempo todo eu intercalei o estudo com as aulas no AWS Skillbuilder, de Cloud Practitioner:

--- 
    AWS Cloud Practicioner Essentials:
	Introdução ao AWS:
    ponto chave: pagar pelo que usar

    - Modelo cliente-servidor:
        cliente: navegador ou aplicação com o qual uma pessoa interage para fazer solicitações aos servidores.

        servidor: serviço

	Computação em Nuvem:
        Entrega de recursos de TI sob demanda pela internet.

    3 Modelos de Implantação da Computação em Nuvem:

	Baseada na Nuvem:
	- execute todas as partes da aplicação na nuvem
	- migre aplicações para a nuvem
	- projete e crie novas aplicações na nuvem

	On-Premises:
	- implante recursos usando ferramentas de virtualização e gerenciamento de recursos
	- aumente a utilização de recursos usando tecnologias de virtualização e gerenciamento de aplicações

	On-Premises também é conhecida como implantação de nuvem privada, utilizando ferramentas de virtualização.
	Pode executar aplicações em tecnologia totalmente mantida no seu data center on-premises. 
	Tecnologias de virtualização e gerenciamento de aplicativos ajudam a aumentar a utilização de recursos.
	
	Implantação Híbrida:
	- conecte recursos baseados na nuvem à infraestrutura on-premises
	- integre recursos baseados na nuvem com aplicações de TI legadas.
	Recursos baseados na nuvem ficam conectados à infraestrutura on-premises.
---

Acima uma das minhas anotações sobre a Introdução do curso (no momento, ainda não concluí o curso do Skillbuilder)

## Segunda semana:
    Comecei a estudar o desafio e a realizar o exercício proposto. No exercício, baixei um script de python "carguru.py", criar Dockerfiles, e usar hashlib em um novo script.
---
    Sobre o desafio, não tive dificuldades em gerar o "etl.py" e o "job.py", tampouco os Dockerfiles. Mas ao criar o "docker-compose.yml" para unir os containers, tive bastante trabalho com problemas de diretório nos volumes, não conseguia fazer o "etl.py" ler o arquivo "concert_tour_by_women.csv" através do docker compose up --build, por exemplo. Depois de uma manhã inteira, consegui fazer o docker-compose rodar normalmente todas as aplicações, e o problema anterior foi resolvido quando passei o arquivo .csv para dentro da pasta /volume/, onde o docker-compose.yml rodaria.

- [Pasta Evidências](./Evidências/)
- [Pasta Exercícios](./Exercícios/)
- [Pasta Desafio](./Desafio/)
- [Readme Desafio](./Desafio/README.md)