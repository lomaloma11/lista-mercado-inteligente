WITH tb_compras AS (
    SELECT 
        dt_compra, 
        produto, 
        AVG(valor_produto) AS valor
    FROM compras
    GROUP BY dt_compra, produto
),

tb_lag AS (
    SELECT
        *,
        LAG(dt_compra) OVER (
            PARTITION BY produto
            ORDER BY dt_compra
        ) AS dt_compra_anterior
    FROM tb_compras
),

tb_avg AS (
    SELECT
        produto,
        AVG(
            JULIANDAY(dt_compra) -
            JULIANDAY(dt_compra_anterior)
        ) AS avg_diffs_dias
    FROM tb_lag
    GROUP BY produto
),

tb_stats_produto AS (
    SELECT
        c.produto,
        MAX(c.dt_compra) AS ultima_compra,
        AVG(c.valor) AS valor_medio,
        a.avg_diffs_dias,
        JULIANDAY('now') - JULIANDAY(MAX(c.dt_compra)) AS dias_ult_compra
    FROM tb_compras c
    JOIN tb_avg a ON c.produto = a.produto
    GROUP BY c.produto
)

SELECT * FROM tb_stats_produto;