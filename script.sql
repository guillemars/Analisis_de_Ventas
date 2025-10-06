CREATE TABLE IF NOT EXISTS ventas (
    fecha TEXT,
    producto TEXT,
    cantidad INTEGER,
    precio_unitario REAL,
    total REAL
);

-- Consulta para obtener los 3 productos más vendidos por cantidad
SELECT producto, SUM(cantidad) AS total_vendido
FROM ventas
GROUP BY producto
ORDER BY total_vendido DESC
LIMIT 3;
