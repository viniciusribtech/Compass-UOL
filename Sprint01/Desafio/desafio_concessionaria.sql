-- primeiro, dividi a unica tabela tb_locacao em varias outras tabelas, dividindo assim suas colunas de forma mais compreensível
create table tb_cliente (
idCliente int primary key,
nomeCliente varchar,
cidadeCliente varchar,
estadoCliente varchar,
paisCliente varchar
);

create table tb_carro (
idCarro int primary key,
chassiCarro varchar,
marcaCarro varchar,
modeloCarro varchar,
anoCarro int,
kmCarro int,
idcombustivel int,
foreign key (idcombustivel) references tb_combustivel(idcombustivel)
);
-- as chaves estrangeiras servem para relacionar a coluna da tabela nova com a chave primária da primeira tabela (o que possibilita a ligação das colunas na visualização da modelagem)
create table tb_combustivel(
idcombustivel int primary key,
tipocombustivel varchar
);

create table tb_vendedor(
idVendedor int primary key,
nomeVendedor varchar,
sexoVendedor smallint,
estadoVendedor varchar
);

alter table tb_locacao rename to tb_locacao_antiga;
-- mas, antes de criar uma nova tb_locacao, o cliente não saberia diferenciar as duas tabelas de mesmo nome. Por isso, mudei o nome da primeira tb_locacao, para tb_locacao_antiga
create table tb_locacao(
idLocacao int primary key,
idCliente int,
idCarro int,
idVendedor int,
dataLocacao datetime,
horaLocacao time,
qtdDiaria int,
vlrDiaria decimal,
dataEntrega date,
horaEntrega time,
foreign key (idCliente) references tb_cliente(idCliente),
foreign key (idCarro) references tb_carro(idCarro),
foreign key (idVendedor) references tb_vendedor(idVendedor)
);
-- desse modo, pude migrar os valores dos dados para as novas tabelas criadas e dividir suas colunas
insert or ignore into tb_locacao (idlocacao, idcliente, idcarro, idvendedor, datalocacao, horalocacao, qtddiaria, vlrdiaria, dataentrega, horaentrega)
select idlocacao, idcliente, idcarro, idvendedor, datalocacao, horalocacao, qtddiaria, vlrdiaria, dataentrega, horaentrega
from tb_locacao_antiga;
-- usando o 'insert or ignore' migrei os valores dos dados e evitei o problema de colunas repetidas que já existiam na tb_locacao_antiga
insert into tb_cliente (idcliente, nomecliente, cidadecliente, estadocliente, paiscliente)
select distinct idcliente, nomecliente, cidadecliente, estadocliente, paiscliente
from tb_locacao_antiga;

insert into tb_combustivel (idcombustivel, tipocombustivel)
select distinct idcombustivel, tipocombustivel
from tb_locacao_antiga;

insert into tb_carro (idcarro, chassicarro, marcacarro, modelocarro, anocarro, kmcarro, idcombustivel)
select distinct idcarro, chassicarro, marcacarro, modelocarro, anocarro, kmcarro, idcombustivel
from tb_locacao_antiga;

insert into tb_vendedor (idvendedor, nomevendedor, sexovendedor, estadovendedor)
select distinct idvendedor, nomevendedor, sexovendedor, estadovendedor
from tb_locacao_antiga;
-- depois de criada a Modelagem Relacional, comecei a criar novas tabelas para simular e visualizar a Modelagem Dimensional
create table dim_cliente(
idCliente integer primary key,
nomeCliente text,
cidadeCliente text,
estadoCliente text,
paisCliente text
)

create table dim_carro(
idCarro integer primary key,
chassiCarro text,
marcaCarro text,
modeloCarro text,
anoCarro integer,
kmCarro integer,
idcombustivel integer
)

create table dim_vendedor(
idVendedor integer primary key,
nomeVendedor text,
sexoVendedor integer,
estadoVendedor text
)

create table dim_combustivel(
idcombustivel integer primary key,
tipocombustivel text
)

create table fato_locacao(
idLocacao integer primary key,
idCliente integer,
idCarro integer,
idVendedor integer,
idcombustivel integer,
dataLocacao date,
horaLocacao time,
qtdDiaria integer,
vlrDiaria decimal,
dataEntrega date,
horaEntrega time,
foreign key (idCliente) references dim_cliente(idCliente),
foreign key (idCarro) references dim_carro(idCarro),
foreign key (idVendedor) references dim_vendedor(idVendedor),
foreign key (idcombustivel) references dim_combustivel(idcombustivel)
)
-- com as novas tabelas pra Modelagem Dimensional feitas, agora pude gerar uma nova Modelagem Relacional, dessa vez sem as tabelas "tb_cliente, tb_vendedor, etc...",
-- para simular a Modelagem Dimensional