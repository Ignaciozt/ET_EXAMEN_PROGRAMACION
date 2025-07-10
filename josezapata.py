#programa de logistaca de stock

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}
#funcion para stock por marca
def stock_marca(marca):
    total =0;
    for codigo,datos in productos.items():
        if(datos[1].lower()==marca.lower()):
            total += stock[codigo][1];
    print(f"El stock total para {marca} es: {total}");

#funcion para busqueda por precio
def buscar_por_precio(p_min,p_max):
    resultados = [];
    for codigo,datos in productos.items():
        precio = datos[4]
        if (precio >= p_min and precio <= p_max) and (stock[codigo][1] > 0):
            resultados.append(codigo + "--" + datos[2]);
    if resultados:
        resultados.sort();
        print("Productos encontrados",resultados);
    else:
        print("No hay productos en ese rango de precio");

#funcion para ordenar productos
def ordenar_productos(codigo,ordenar_productos):
    if(codigo in stock):
        stock[codigo][1] = ordenar_productos;
        return True;
    return False;

#programa principal
def main():

    while True:
        print("*** MENU PRINCIPAL ***");
        print("1. Stock marca.");
        print("2. Búsqueda por precio.");
        print("3. Listado de productos.");
        print("4. Salir.");
        
        opc = int(input("Ingrese una opción del 1-4: "));
        if (opc==1):
            marca = input("ingrese la marca: ");
            stock_marca(marca);
        elif(opc==2):
            try:
                p_min = float(input("Ingrese el precio mínimo: "));
                p_max = float(input("Ingrese el precio máximo: "));
                buscar_por_precio(p_min,p_max);
            except ValueError:
                print("Debe ingresar valores numericos válidos!!");
        elif(opc==3):
            while True:
                codigo = input("Ingrese el codigo del producto:");
                try:
                    ordenar_productos = int(input("Ingrese el nuevo stock: "));
                    if ordenar_productos(codigo,ordenar_productos);
                        print("Stock actualizado!");
                    else:
                        print("Elcodigo no existe!");
                except ValueError:
                    print("Debe ingresar un numero entero para el stock!");
                repetir = input("Desea actualizar otro producto (s/n)?: ").lower();
                if(repetir !="s"):
                    break;
        elif(opc==4):
            print("Programa finalizado.");
            break;
        else:
            print("Debe ingresar una opción válida!!");

    #ejecutar programa
if_name_=="_main_":
    main();

       
        

