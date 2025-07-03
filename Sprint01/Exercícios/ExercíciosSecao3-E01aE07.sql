-- Seção 3 | Caso de Estudo "Biblioteca"
-- E01 - Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma
select cod, titulo, autor, editora, valor, publicacao, edicao, idioma
from livro
where publicacao > '2014-12-31' 
order by cod

-- E02 - Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  Atenção às colunas esperadas no resultado final:  titulo, valor.
select titulo, valor
from livro 
order by valor desc
limit 10

-- E03 - Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.
select
  count(l.editora) as quantidade,
  e.nome,
  en.estado,
  en.cidade
from livro as l
join editora as e on l.editora = e.codeditora
join endereco as en on e.endereco = en.codendereco 
group by e.nome, en.estado, en.cidade
order by quantidade desc
limit 5

-- E04 - Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).
select 
	autor.nome,
	autor.codautor,
	autor.nascimento,
	count(livro.autor) as quantidade
from autor
left join livro on autor.codautor = livro.autor
group by autor.codautor, autor.nome, autor.nascimento
order by replace(autor.nome, 'Á', 'A')

-- E05 - Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.
select distinct
	au.nome
from autor as au
join livro as l on au.codautor = l.autor
join editora as e on l.editora = e.codeditora
join endereco as en on e.endereco = en.codendereco
where en.estado not in ('RIO GRANDE DO SUL', 'PARANÁ')
order by au.nome

-- E06 - Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.
select 
	autor.codautor,
	autor.nome,
	count (l.autor) as quantidade_publicacoes
from autor
left join livro as l on autor.codautor = l.autor
group by autor.codautor, autor.nome
order by quantidade_publicacoes desc
limit 1

-- E07 - Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.
select 
	autor.nome
from autor
left join livro as l on autor.codautor = l.autor
group by autor.nome
having count(l.autor) = 0
order by autor.nome