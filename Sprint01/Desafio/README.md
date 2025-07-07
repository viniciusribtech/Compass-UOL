# Desafio da Sprint 1
## Caso de Estudo "Concessionária"
### O que fazer?
#### Normalizar o Banco de Dados de estudo
Primeiramente, notei que todas as colunas estavam concentradas em uma só tabela, o que dificulta a visualização e compreensão do objetivo do banco.

<img src="./primeiropassodesafio.png" alt="Primeiro Passo" width="700"/>

---
O **primeiro passo**, então, foi dividir essas colunas amontoadas em tabelas separadas e mais organizadas, onde "nomeCliente, estadoCliente" passaram a ser contidas na nova tabela "tb_cliente" e assim por diante.

<br>
A criação das chaves primárias vão servir mais tarde para serem utilizadas nas chaves estrangeiras e conectar essas colunas novas com a chave primária, e visualizar essas conexões quando criar as modelagens. 
 
---
O **segundo passo** foi mudar o nome da tabela antiga para tb_locacao_antiga, para evitar qualquer bug no momento de criar uma nova tb_locacao para migrar os antigos dados.

<img src="./segundopassodesafio.png" alt="Segundo Passo" width="500"/>

---
O **terceiro passo** foi usar os comandos INSERT para migrar os dados da antiga tabela para as tabelas novas. Assim, as colunas passariam a ter um mesmo conteúdo. E eu poderia apagar a tb_locacao_antiga.

<img src="./terceiropassodesafio.png" alt="Terceiro Passo" width="900"/>

Ao usar o IGNORE, as tabelas já existentes não teriam seu valor mudado.
E, agora, usei o próprio recurso do DBeaver para criar a Modelagem Relacional.

#### Criar o desenho da Modelagem Relacional

<img src="./modelo_relacional_desafio.png" alt="Modelagem Relacional" width="500"/>

---
#### Criar o desenho da Modelagem Dimensional
O **quarto** e último passo, seria criar as tabelas dimensionais e a tabela fato, para poder simular a Modelagem Dimensional no DBeaver, usando o mesmo recurso usado para a Modelagem Relacional anterior.
<img src="./quartopassodesafio.png" alt="Quarto Passo" width="400"/>

---
Assim, pude simular a Modelagem Dimensional
<img src="./modelo_dimensional_desafio.png" alt="Modelagem Dimensional" width="600"/>