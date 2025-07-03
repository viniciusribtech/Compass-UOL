-- Seção 4 | Caso de Estudo "Loja"
-- E08 - Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.
select 
	tbvendas.cdvdd,
	vend.nmvdd
from tbvendas
join tbvendedor as vend on tbvendas.cdvdd = vend.cdvdd
where tbvendas.status = 'Concluído'
group by tbvendas.cdvdd, vend.nmvdd
order by count (*) desc
limit 1

-- E09 - Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.
select 
	cdpro,
	nmpro
from tbvendas
where dtven between '2014-02-02' and '2018-02-02'
	and status = 'Concluído'
group by cdpro, nmpro
order by sum(qtd) desc
limit 1


-- E10 - A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

-- Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.

-- As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

select 
	v.nmvdd as vendedor,
	round(sum(ven.qtd * ven.vrunt), 2) as valor_total_vendas,
	round(sum(ven.qtd * ven.vrunt) * v.perccomissao / 100, 2) as comissao
from tbvendas as ven
join tbvendedor as v on ven.cdvdd = v.cdvdd
where ven.status = 'Concluído'
group by v.nmvdd
order by comissao desc

-- E11 - Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente

select
	cdcli,
	nmcli,
	sum (qtd * vrunt) as gasto
from tbvendas
where status = 'Concluído'
group by cdcli, nmcli 
order by gasto desc
limit 1

-- E12 - Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
-- Observação: Apenas vendas com status concluído.

select
	dep.cddep,
	dep.nmdep,
	dep.dtnasc,
	sum((ven.qtd * ven.vrunt) > 0) as valor_total_vendas
from tbdependente as dep
join tbvendedor as v on dep.cdvdd = v.cdvdd
join tbvendas as ven on v.cdvdd = ven.cdvdd
where status = 'Concluído'
group by cddep, nmdep, dtnasc
order by valor_total_vendas
limit 1

-- E13 - Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

select
	cdpro,
	nmcanalvendas,
	nmpro,
	sum(qtd) as quantidade_vendas
from tbvendas
where status = 'Concluído'
	and nmcanalvendas in ('Ecommerce', 'Matriz')
group by cdpro, nmcanalvendas, nmpro
order by quantidade_vendas 
limit 10

-- E14 - Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

select
	estado,
	round(avg(qtd * vrunt), 2) as gastomedio
from tbvendas
where status = 'Concluído'
group by estado
order by gastomedio desc

-- E15 - Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.

select cdven
from tbvendas 
where deletado = '1'
order by cdven 

-- E16 - Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).

select
	estado,
	nmpro,
	round(avg(qtd), 4) as quantidade_media
from tbvendas
where status = 'Concluído'
group by estado, nmpro
order by estado, nmpro
