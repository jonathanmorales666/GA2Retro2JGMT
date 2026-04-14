# Jonathan Gabriel Morales Torres "10"
# Retroalimentación GA2
# Analisis de sistemas

precio = input("Introduce el precio del producto con dos decimales: ")
print(precio[:precio.find('.')], 'quetzales y', precio[precio.find('.')+1:], 'centimos. ')