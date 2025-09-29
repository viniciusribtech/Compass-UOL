CREATE OR REPLACE VIEW view_fato_completo AS
SELECT 
    f.id_filme,
    f.id_artista,
    f.id_profissao,
    f.id_tempo,
    f.notamedia,
    f.numerovotos,
    d.titulopincipal,
    d.titulooriginal,
    d.anolancamento_filme,
    d.tempominutos,
    d.genero,
    a.nomeartista_dim,
    a.generoartista,
    a.anonascimento,
    a.anofalecimento,
    p.profissao_dim,
    t.anolancamento_tempo
FROM fato_filmeartista f
LEFT JOIN dim_filme d 
    ON f.id_filme = d.id_filme
LEFT JOIN dim_artista a 
    ON f.id_artista = a.id_artista
LEFT JOIN dim_profissao p 
    ON f.id_profissao = p.id_profissao
LEFT JOIN dim_tempo t 
    ON f.id_tempo = t.id_tempo;
