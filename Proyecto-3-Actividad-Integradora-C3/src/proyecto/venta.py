import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv("ventas_tecnologia.csv")

# Mostrar datos
print("DATOS DEL ARCHIVO CSV")
print(df)

# Crear columna de ingresos
df["ingresos"] = df["cantidad"] * df["precio_unitario"]

# Reportes tabulares
ventas_producto = df.groupby("producto")["cantidad"].sum()
ventas_mes = df.groupby("mes")["cantidad"].sum()
ingresos_producto = df.groupby("producto")["ingresos"].sum()
ingresos_mes = df.groupby("mes")["ingresos"].sum()

print("\nVENTAS TOTALES POR PRODUCTO")
print(ventas_producto)

print("\nVENTAS TOTALES POR MES")
print(ventas_mes)

print("\nINGRESOS POR PRODUCTO")
print(ingresos_producto)

# Datos importantes
print("\nRESULTADOS IMPORTANTES")
print("Producto más vendido:", ventas_producto.idxmax())
print("Producto menos vendido:", ventas_producto.idxmin())
print("Producto con mayores ingresos:", ingresos_producto.idxmax())
print("Mes más rentable:", ingresos_mes.idxmax())

# Gráfica de barras
plt.figure()
ventas_producto.plot(kind="bar")
plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad vendida")
plt.show()

# Gráfica de líneas
plt.figure()
ventas_mes.plot(kind="line", marker="o")
plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Cantidad vendida")
plt.show()

# Gráfica circular
plt.figure()
ventas_producto.plot(kind="pie", autopct="%1.1f%%")
plt.title("Porcentaje de Ventas por Producto")
plt.ylabel("")
plt.show()