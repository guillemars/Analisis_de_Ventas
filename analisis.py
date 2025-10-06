import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

def calcular_total(cantidad, precio_unitario):
    return cantidad * precio_unitario

def main():
    # Leer archivo CSV
    df = pd.read_csv("ventas.csv")

    # Limpiar datos: eliminar nulos y cantidades negativas
    df = df.dropna()
    df = df[df['cantidad'] >= 0]

    # Crear columna total
    df['total'] = df.apply(lambda row: calcular_total(row['cantidad'], row['precio_unitario']), axis=1)

    # a) Producto mas vendido por cantidad
    producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()
    print("Producto mas vendido:", producto_mas_vendido)

    # b) Producto con mayor facturacion total
    producto_mayor_facturacion = df.groupby('producto')['total'].sum().idxmax()
    print("Producto con mayor facturacion:", producto_mayor_facturacion)

    # c) Facturacion total por mes
    df['fecha'] = pd.to_datetime(df['fecha'])
    facturacion_mes = df.groupby(df['fecha'].dt.to_period('M'))['total'].sum()
    print("Facturacion por mes:")
    print(facturacion_mes)

    # Guardar en SQLite
    conn = sqlite3.connect("ventas.db")
    df.to_sql("ventas", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()

    # Grafico de facturacion por mes
    facturacion_mes.plot(kind="bar")
    plt.ylabel("Facturacion total")
    plt.title("Facturacion total por mes")
    plt.tight_layout()
    plt.savefig("grafico.png")
    plt.close()

if __name__ == "__main__":
    main()
