#Maneja las pausas de tiempo
import time as t

#Maneja fechas y horas 
from datetime import *

#Maneja la BDD
from sqlite3 import *

#Limpiar la consola
import os as os

#Maneja las pausas de tiempo
import time as t

#libreria para crear barra de carga (puramente estetico)
import tqdm

#Salida de hiperTexto con arte ASCII code
import pyfiglet


#_____________________________________________________________________Estilo_____________________________________________________________________

#Crear tablas agradables visualmente 
import tabulate 

#Estilos disponibles
# * **simple:** Este es el estilo de tabla por defecto. Las celdas están alineadas a la izquierda y no hay líneas de cuadrícula.
# * **grid:** Este estilo de tabla añade líneas de cuadrícula a la tabla.
# * **fancy_grid:** Este estilo de tabla añade líneas de cuadrícula y un borde a la tabla.
# * **pipe:** Este estilo de tabla utiliza el carácter de tubería (|) para separar las celdas.
# * **orgtbl:** Este estilo de tabla utiliza la sintaxis de Org-mode para crear tablas.
# * **rst:** Este estilo de tabla utiliza la sintaxis de reStructuredText para crear tablas.
# * **mediawiki:** Este estilo de tabla utiliza la sintaxis de MediaWiki para crear tablas.
# * **html:** Este estilo de tabla utiliza la sintaxis HTML para crear tablas.
# * **latex:** Este estilo de tabla utiliza la sintaxis LaTeX para crear tablas.

#Tipo de estilo de los outputs (Se puede cambiar por el estilo deseado)
fontStyle = "fancy_grid"

#_____________________________________________________________________Estilo_____________________________________________________________________



#_____________________________________________________________________BD_____________________________________________________________________

#Coneccion a la BD
conn = connect("BarrioPrivado.db")


c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS LOTES(ID INTEGER PRIMARY KEY AUTOINCREMENT,
		                                      lot NUMBER(2) NOT NULL,
		                                      man NUMBER(2) NOT NULL,
		                                      m_fond NUMBER(3) NOT NULL,
		                                      m_fren NUMBER(3) NOT NULL,
		                                      luz_p BOOLEAN NOT NULL,
		                                      agua_p BOOLEAN NOT NULL,
		                                      asfalto BOOLEAN NOT NULL,
		                                      esquina BOOLEAN NOT NULL)""")

c.execute("""CREATE TABLE IF NOT EXISTS PROPIETARIOS(ID INTEGER PRIMARY KEY AUTOINCREMENT,
		                                             apellido VARCHAR(15) NOT NULL,
		                                             nombre VARCHAR(15) NOT NULL,
		                                             lot_p NUMBER(2) NULL,
		                                             man_p NUMBER(2) NULL,
		                                             fecha_Compra DATE NULL,
		                                             supcubm2 NUMBER(3) NULL,
		                                             hab NUMBER(2) NULL,
		                                             cons_luz NUMBER(5) NULL,
		                                             cons_agua NUMBER(5) NULL,
		                                             cons_gas NUMBER(5) NULL)""")

c.execute("""CREATE TABLE IF NOT EXISTS PRECIOS(ID INTEGER PRIMARY KEY AUTOINCREMENT,
		                                        luz_m NUMBER(5) NOT NULL,
		                                        agua_m NUMBER(5) NOT NULL,
		                                        gas_m NUMBER(5) NOT NULL,
		                                        cochera_m NUMBER(5) NOT NULL,
		                                        seguridad_cp NUMBER(5) NOT NULL,
		                                        luz_cp NUMBER(5) NOT NULL,
		                                        agua_cp NUMBER(5) NOT NULL,
		                                        valor_metro NUMBER(5) NOT NULL)""")

c.close()
#_____________________________________________________________________BD_____________________________________________________________________



#Descargar listas 
LOTES = {"lot": "Number",
    "man": "Number",
    "m_fond": "Number",
    "m_fren": "Number",
    "luz_p": "Boolean",
    "agua_p": "Boolean",
    "asfalto": "Boolean",
    "esquina": "Boolean",}


PROPIETARIOS = {"apellido": "Text",
    "nombre": "Text",
    "lot_p": "Number",
    "man_p": "Number",
    "fecha_Compra": "Date",
    "supcubm2": "Number",
    "hab": "Number",
    "cons_luz": "Number",
    "cons_agua": "Number",
    "cons_gas": "Number",}

PRECIOS = {"luz_m": "Number",
    "agua_m": "Number",
    "gas_m": "Number",
    "cochera_m": "Number",
    "seguridad_cp": "Number",
    "luz_cp": "Number",
    "agua_cp": "Number",
    "valor_metro": "Number"}


DictDiccitionaries = {"LOTES":LOTES,
                       "PROPIETARIOS":PROPIETARIOS,
                       "PRECIOS":PRECIOS}


# #Variables auxiliares

# x = " "
# y = " "

# #----------------------

# M = 4
# LM = 6

# #Variables del Lote

# lot =  [] 
# manz = []
# m_fren = []
# m_fond=  []
# luz_p=     []
# agua_p =   []
# asfalto =  []
# esquina =  []

# #Variables del propietario 

# ap = []
# nom = []
# lot_p = []
# manz_p = []
# fc = []
# supcubm2 = []
# habit = []
# cantvehi = []
# cons_luz = []
# cons_agua = []
# cons_gas = []

# #Variables para el menu 

opc_manz = 0 
opc_lot = 0
opc_ap = ""
opc_c = 0

def ResetMenu():
	global opc_m , opc_m_c, opc_m_c_p,opc_m_c_l,opc_liq
	opc_m = 0  #Opciones Menu 
	opc_m_c = 0 # Opciones Consultas 
	opc_m_c_p = 0 # Opciones Consulta del propietario 
	opc_m_c_l = 0 # Opciones Consultas del local 
	opc_liq = 0 #Opciones de liquidacion
#Variables de precios

# #Common pay(Cost) as cp
# #Pay(Cost) as m

# luz_m = 60
# luz_mls = []
# Agua_m = 30
# Agua_mls = []
# Gas_m = 45
# Gas_mls = []
# Cochera_m = 10000
# Cochera_mls = []

# #Common Pay
# Seg_cp = 30000
# Seg_cpls = []

# Luz_cp = 80000
# Luz_cpls = []

# #X metro de frente 
# Agua_cp = 40 
# Agua_cpls = []
# Asf_cp = 70 
# Asf_cpls = []

# #X metro cuadrado
# metros2 = []
# Valorter_m = 60000
# Valorter_mls = []

def val_range(maxim,minin):
    while True:
        x = str(input(" ▶ "))

        print(x)
        print(x <= str(maxim) and x >= str(minin))

        if int(x) <= int(maxim) and int(x) >= int(minin):
            return str(x)
        else:
            print("Su valor tiene que estar entre",minin ,"y",maxim ,sep = " ")


def string(CadenaTexto):

    while True:
        Bucle = False

        #Navego por cada caracter del texto buscando un numero para validar una cadena pura
        for caracteres in CadenaTexto:
            if caracteres.isdigit():
                Bucle = True
        #Si el bucle es falso significa que nunca encontro un digito en la cadena de texto
        if Bucle == False:
            return CadenaTexto

        #Si el bucle es verdadero (Else ya que solo se pueden tomar 2 valores en un booleano) se vuelve a pedir una cadena de texto
        else:
            CadenaTexto = input('Tiene que ingresar un texto sin numeros  > ')


def ValidacionFecha():
       
    while True:
        # try:
            print("Ingresa una fecha en el formato MM(mes): ")
            #Arreglar val_range 
            fechaM = val_range(12,1)
            time.strptime(str(fechaM),'%m')
            print("Fecha válida")
            break
        # except ValueError:
            # print("Fecha inválida")

    while True:
        try:
            fechaD = input("Ingresa una fecha en el formato DD(dia): ")
            time.strptime(str(fechaD),'%d')
            print("Fecha válida")
            break
        except ValueError:
            print("Fecha inválida")
    while True:
        try:
            #fecha = input("Ingresa una fecha en el formato YYYY-MM-DD: ")
            print("Ingresa una fecha en el formato YYYY(año): ")
            fechaY = val_range(2022,1900)
            #datetime.strptime(fecha, '%Y-%m-%d')
            time.strptime(str(fechaY), '%Y')
            print("Fecha válida")
            break
        except ValueError:
            print("Fecha inválida")

    fecha = str(fechaY) + "-" + str(fechaM) + "-" + str(fechaD)
    # RevfechaY = str(reversed(fechaY))
    # RevfechaM = str(reversed(fechaM))
    # RevfechaD = str(reversed(fechaD))
    # fecha_val = "-".join([RevfechaY,RevfechaM,RevfechaD])
    # fecha_hoy = str(reversed(str(datetime.strptime(fechaY, '%Y'))))+ str(reversed(str(datetime.strptime(fechaM,'%m')))) + str(reversed(str(datetime.strptime(fechaD,'%d'))))
    # print(fecha_val +"\n" + fecha_hoy)

    print(fecha)
    return fecha



def numeric(Numeric_string,Long_of_String,Max_number):
    c = 0
    #El while true se encarga de forzar un valor apto para el codigo
    while True:

        #Esto mantiene la solides del codigo verifica que Numeric_string sea tipo int para que isdigit acepte la condicion
        if Numeric_string.isdigit() and len(Numeric_string) <= 3 and int(Numeric_string) >= 0 and int(Numeric_string) <= int(Max_number):
            print(Numeric_string.isdigit())
            return Numeric_string #El return frena el while True
        else:
            if c == 0:
                Numeric_string = input("Ingrese una opcion valida > ")

            if c == 1 and len(Numeric_string) >= 2:
                Numeric_string = input("Ingrese una opcion valida de {} cifras > ".format(Long_of_String))

            if c == 1:
                Numeric_string = input("Ingrese una opcion valida  entre {} y {} > ".format(1,Max_number))

            if c > 3:
                Numeric_string = input("Ingrese una opcion valida de {} cifras entre {} y {} > ".format(Long_of_String,1,Max_number))


        #Manera de ayudar al usuario , mientras mas se equivoca mas va a ayudarlo para poder cargar los datos necesarios
        c += 1


def numval(x):
	
	it = False 
	while it == False:
		
		try:
			x = int(input( "▶ " ))
			it = True 
			return x 
		except (ValueError):
			print("Este valor solo puede ser numerico")
			it = False

#el val_range funciona unicamente con variables tipo int

def val_range(maxim,minin):
    while True:
        x = str(input(" ▶ "))

        print(x)
        print(x <= str(maxim) and x >= str(minin))

        if 0 <= int(maxim) and int(x) >= int(minin):
            return int(x)
        else:
            print("Su valor tiene que estar entre",minin ,"y",maxim ,sep = " ")


	# a = 19
	# print(a)
	# ranker(a,0,20)

def srtval(x):
	
	while True :
		print(x)
		x = input(" ▶ ")

		if x.isdigit() == False:
			for i in range(len(x)):
				if x[i].isdigit() == True:

					x=x[:i]+" "+x[i+1:]
					print(x) 


			return x
			break
			
		else:

			print("No se pueden ingresar numeros")

		print(x)	

def val_strlist(x):
	
	while True:
		
		x = input(" ▶ ")

		if x.lower() in ap:
			return x
			 
		else:
			print("El apellido que ingreso no esta cargado\n Los nombres cargados son: \n ", ap, "\n Reingrese el apellido")
			

def sn(z):
	
	while True:
		z = str(input( """Opciones:
			-Si
			-No 
			▶ """ ))
		
		if z.upper() == "SI" or z.upper() == "NO" or z.upper() == "S" or z.upper() == "N":
			zup = z.upper()
			return zup[:1]
			break 
		else:
			print("Ingrese por respuesta un si o no")

def nrep(var):

	for i in range(len(var)-1):
		if var[i] == var[-1]:
			print("El valor ",var[-1], ",ya fue cargado")
			var.pop(-1)
			var.append(numval(var))
			print(var)
			nrep(var)

	# a = [2,4,5,6,7,8,2]

	# nrep(a)

def nrep2(var,var2):

	print(var)
	print(var2)
	for i in range(len(var)-1):
		if var[i] == var[-1] and var2[i] == var2[-1]:
			var.pop(-1)
			var2.pop(-1)
			print("Ya fue cargado, en el indice, " ,i)
			var.append(input(numval(var)))
			var2.append(input(numval(var2)))
	return var, var2

	# a = [1,1,12,2,3,4,3]
	# b = [2,2,3,42,3,5,3]


	# nrep2(a,b)
	
def nrep2_lotxprop(var,var2,var_p,var2_p):

	print(var)
	print(var2)
	for i in range(len(var)-1):
		if var_p[i] == var[-1] and var2_p[i] == var2[-1]:
			var.pop(-1)
			var2.pop(-1)
			print("Ya fue cargado, en el indice, " ,i)
			var.append(input(numval(var)))
			var2.append(input(numval(var2)))
	return var, var2

def fdecompra():
	
	while True:
		try:
			print("Ingresa una fecha en el formato MM(mes): ")
			#Arreglar val_range 
			fechaM = val_range(12,1)
			datetime.strptime(fechaM,'%m')
			print("Fecha válida")
			break
		except ValueError:
			print("Fecha inválida")
		else:
			print("Fecha inválida")
	while True:
		try:
			fechaD = input("Ingresa una fecha en el formato DD(dia): ")
			datetime.strptime(fechaD,'%d')
			print("Fecha válida")
			break
		except ValueError:
			print("Fecha inválida")
	while True:
		try:
	    	#fecha = input("Ingresa una fecha en el formato YYYY-MM-DD: ")
			print("Ingresa una fecha en el formato YYYY(año): ")
			fechaY = val_range(2022,1900)
	        #datetime.strptime(fecha, '%Y-%m-%d')
			datetime.strptime(fechaY, '%Y')
			print("Fecha válida")
			break
		except ValueError:
			print("Fecha inválida")

	fecha = fechaY + "-" + fechaM + "-" + fechaD
	fecha_val = reversed(fechaY) + "-" + reversed(fechaM) + "-" + reversed(fechaD)
	fecha_hoy = reversed(datetime.strptime(fechaY, '%Y') )+ reversed(datetime.strptime(fechaM,'%m')) + reversed(datetime.strptime(fechaD,'%d'))
	print(fecha_val +"\n" + fecha_hoy)

	reversed()

	print(fecha)
	return fecha

def randomer_fc(c):

	for i in range(c):
		
		fechaY = random.randint(1900,2022)
		fechaM = random.randint(1,12)		
		fechaD = random.randint(1,31)

		fecha = str(fechaY) + "-" + str(fechaM) + "-" + str(fechaD)
		
		fc.append(fecha)
	
def randomer_nomap(c):
	
	for i in range(c):
		apes  = ["lopez","martinez" ,"abalos" , "ramos", "faustino"]
		nomes = ["Valentina","juan"  ,"Mariano" ,"Lucas" ,"Tadeo" ]
		
		ind_a= random.randint(1,len(apes)-1)
		ind_n= random.randint(1,len(nomes)-1)
		
		ap.append(apes[ind_a])
		nom.append(nomes[ind_n])

def randomer(principal,a,b,c):
	
	for i in range(c):
		x = random.randint(a,b)
		principal.append(x)


def randomer_bol(principal,c):

	for i in range(c):
		x = random.randint(1,2)
		
		if x == 1:
			principal.append("S")
		else:
			principal.append("N")
		

# def reingresar_prop(y):

# 	# La funcion le pregunta al usuario,
# 	# si esta seguro de lo que ingreso.

# 	print("Esta seguro de lo que ingreso?")
# 	tmp = sn(x)
# 	if tmp == "NO" or tmp == "N":
# 		#Advertencia 
# 		print("""Atencion si no esta seguro de los ingresos,
# 		 se borraran todos los datos recien ingresado. 
# 		 Los tendra que ingresar todo de nuevo. 

# 		 ¿Quiere continuar?""") 
# 		tmp_2 = sn(x)
# 		if tmp_2 == "SI" or tmp_2 == "S":
# 			apnom.pop(-1) 
# 			lot_p.pop(-1) 
# 			manz_p.pop(-1) 
# 			fc.pop(-1) 
# 			supcubm2.pop(-1) 
# 			habit.pop(-1) 
# 			cantvehi.pop(-1) 
# 			cons_luz.pop(-1) 
# 			cons_agua.pop(-1) 
# 			cons_gas.pop(-1) 
# 			print("[+] Ultimos datos eliminados\n")

def var_mod(x):

	if x == 1:
		print("Ingrese el valor $$")
		luz_m = int(input()[0:])

	elif x == 2:
		print("Ingrese el valor $$")
		Agua_m = int(input()[0:])


	elif x == 3:
		print("Ingrese el valor $$")
		Gas_m = int(input()[0:])

	elif x == 4:
		print("Ingrese el valor $$")
		Cochera_m = int(input()[0:])

	elif x == 5:
		print("Ingrese el valor $$")
		Seg_cp = int(input()[0:])

	elif x == 6:
		print("Ingrese el valor $$")
		Luz_cp = int(input()[0:])
				
	elif x == 7:
		print("Ingrese el valor $$")
		Agua_cp = int(input()[0:])
				
	elif x == 8:
		print("Ingrese el valor $$")
		Asf_cp = int(input()[0:])
				
	elif x == 9:
		print("Ingrese el valor $$")
		Valorter_m = int(input()[0:])
				
	#Modificador de variables
#La maquina crea datos de propietarios al azar 

#_____________________________________________________________________CLASES_____________________________________________________________________
#_____________________________________________________________________CLASES_____________________________________________________________________
#_____________________________________________________________________CLASES_____________________________________________________________________
class ReadState():

    def __init__(self,table):
        self.table = table

    def ReadAll(self):
        c = conector.cursor()
        c.execute("SELECT * FROM " + self.table + "")
        rows = c.fetchall()

        #Coincidencias en el diccionario para poder identicar los valores
        TemplateVerification = {}

        for i in DictDiccitionaries:
            if i == self.table:
                TemplateVerification = DictDiccitionaries[i]

        #Tabulate formate table 
        tabu = tabulate.tabulate(rows,headers=TemplateVerification.keys(),tablefmt=fontStyle,numalign="center",stralign="center")
        print(tabu)

    def ReadColumn(self,camp):
        self.camp = camp 
        c = conn.cursor()
        c.execute("SELECT * FROM " + self.table + "")
        rows = c.fetchall()

        #Coincidencias en el diccionario para poder identicar los valores
        TemplateVerification = {}

        for i in DictDiccitionaries:
            if i == self.table:
                TemplateVerification = DictDiccitionaries[i]

        print(len(rows))

        IdOption = str(input("Registro ▶️ : "))

        #Arreglar Error del fetchall()
        c = conn.cursor()
        c.execute("SELECT * FROM " + self.table + " WHERE "+ self.camp +" = '"+ IdOption +"'")
        rows = c.fetchall()
        tabu = tabulate.tabulate(rows,headers=TemplateVerification.keys(),tablefmt=fontStyle,numalign="center",stralign="center")
        print(tabu)


class ChargeState():
    def __init__(self,table):
        global nombres
        self.table = table

    def InputData(self):
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM pragma_table_info('"+ self.table +"')")
        nombres = cursor.fetchall()
        datos = []
        #Coincidencias en el diccionario para poder identicar los valores
        TemplateVerification = {}

        for i in DictDiccitionaries:
            if i == self.table:
                TemplateVerification = DictDiccitionaries[i]
        # if self.table in DictDiccitionaries:

        for i in nombres:


            if "ID" == i[0].upper():
                pass
            else:
                if TemplateVerification[i[0]] == "Number":
                    datos.append(numeric(input("Ingrese el campo " + i[0] + ' > '),2,70))
                
                elif TemplateVerification[i[0]] == "Date":
                    print("Ingrese el campo " + i[0])
                    datos.append(ValidacionFecha())
                
                elif TemplateVerification[i[0]] == "Text":
                    datos.append(string(input("Ingrese el campo " + i[0] + ' > ')))

                elif TemplateVerification[i[0]] == "Boolean":
                    datos.append(numeric(input("Ingrese el campo (0_No / 1_Si) " + i[0] + ' > '),2,10))
                else:
                    print("erorr > ",i )
				
        cursor = conn.cursor()

        # Adaptacion para sqlite (?,?,?,?,?)

        # ATENCION: NO EJECUTAR SIN VALIDAR LOS DATOS ANTERIORMENTE

        print(len(datos))

        print(datos)

        ValuesInputs = "?,"*((len(datos)))

        # Sacamos la coma de mas (?,?,?,?,?,) <<<
        ValuesInputs = ValuesInputs[:-1]

        print("Value Inputs :",ValuesInputs)

        cursor.executemany("INSERT INTO "+ self.table +" VALUES (null," + ValuesInputs + ")",[datos,])
        conn.commit()


#_____________________________________________________________________CLASES_____________________________________________________________________
#_____________________________________________________________________CLASES_____________________________________________________________________
#_____________________________________________________________________CLASES_____________________________________________________________________


#_____________________________________________________________________Presentacion_____________________________________________________________________
#_____________________________________________________________________Presentacion_____________________________________________________________________
#_____________________________________________________________________Presentacion_____________________________________________________________________

def carga():
    # Create an instance of the tqdm.tqdm class.
    pbar = tqdm.tqdm(range(0,100,5))

    # Iterate over the list of elements.
    for i in pbar:
        
        #limpiamos la terminal
        os.system('cls')
        
        # Actualizacion de la barra de progreso.
        pbar.update()

        # Escribimos el estado del bucle
        pbar.write(f"{i}")

        t.sleep(0.15)

    os.system('cls')

    # Close the progress bar.
    pbar.close()

    #Nombre del programa con la ayuda de pyfiglet
    text = pyfiglet.print_figlet(text="Barrio Privado",
                                colors="WHITE",
                                font="roman")

    t.sleep(2)

    os.system("cls")

carga()
#_____________________________________________________________________Presentacion_____________________________________________________________________
#_____________________________________________________________________Presentacion_____________________________________________________________________
#_____________________________________________________________________Presentacion_____________________________________________________________________


#_____________________________________________________________________Inicio_Del_Codigo_____________________________________________________________________
#_____________________________________________________________________Inicio_Del_Codigo_____________________________________________________________________
#_____________________________________________________________________Inicio_Del_Codigo_____________________________________________________________________


c = 5


#Banderas
ban = False


print("Fecha de hoy :",date.today())
while True:
	ResetMenu()
	os.system('cls')
	table = [
      ["Altas de lotes","Funcionando 100%"],
      ["Altas de propietarios","Funcionando 100%"],
      ["Consultas","Funcionando 50%"],
      ["Act.tabla de consumos","Funcionando 100%"],
      ["Calculo de consumo","Funcionando 0%"],
      ["Emitir liquidacion","Funcionando 0%"],
      ["Fin de tarea","Funcionando 100%"],]
	print(tabulate.tabulate(table, headers=["Option", "Description","Estado.developInfo"],numalign="center", tablefmt=fontStyle, showindex=True))

	opc_m = numval(opc_m)

	if opc_m <= 6 and opc_m >= 0:		
		os.system('cls')
		if opc_m == 6:
			os.system('cls')
			break
		
		#Lotes
		elif opc_m == 0:
			os.system('cls')
			Instance01 = ChargeState("LOTES")
			Instance01.InputData()

			# reingresar_lot(x)

		#Propietarios
		elif opc_m == 1:
			os.system('cls')
			Instance01 = ChargeState("PROPIETARIOS")
			Instance01.InputData()

			# reingresar_prop(y)

			
		# #Consultas

		elif opc_m == 2:
			ResetMenu()
			os.system('cls')
			while opc_m_c != 2:
				os.system('cls')
				table = [
    				["Lotes"],
    				["Propietarios"],
    				["Volver"],]
                
				print(tabulate.tabulate(table, headers=["Option", "Description"],numalign="center", tablefmt=fontStyle, showindex=True))
						
				opc_m_c = val_range(2,0)

				if int(opc_m_c) == 0:
					os.system('cls')
					ResetMenu()
					while opc_m_c_l != 2:
						os.system('cls')
						table = [
      						["Por Manzana"],
      						["Por Propietario"],
      						["Volver"],]
						print(tabulate.tabulate(table, headers=["Option", "Description"],numalign="center", tablefmt=fontStyle, showindex=True))

						opc_m_c_l = val_range(2,0)

						if int(opc_m_c_l) == 0:
							os.system('cls')
							print("Ingrese la manzana que busca")
							Instance01 = ReadState("LOTES")
							Instance01.ReadColumn("man")
							t.sleep(10)


							
						elif opc_m_c_l == 1:
							os.system('cls')
							print("Ingrese el lote que busca")
							Instance01 = ReadState("LOTES")
							Instance01.ReadColumn("lot")
							t.sleep(10)

				elif int(opc_m_c) == 1:
					ResetMenu()
					os.system('cls')
					while opc_m_c_p != 3:
						os.system('cls')
						table = [
      						["Por Nombre(Apellido)"],
      						["Por Manzana"],
      						["Por Manzana y Lote "],
      						["Volver"],]
						print(tabulate.tabulate(table, headers=["Option", "Description"],numalign="center", tablefmt=fontStyle, showindex=True))

						opc_m_c_p = val_range(3,0)

						if int(opc_m_c_p) == 0:
							os.system('cls')
							print("Ingrese su appelido")
							opc_ap = string(opc_ap)
							
							Instance01 = ReadState("PROPIETARIOS")
							Instance01.ReadColumn("nombre")
							t.sleep(10)							

						elif opc_m_c_p == 1:
							os.system('cls')
							print("Ingrese su manzana")							
							Instance01 = ReadState("PROPIETARIOS")
							Instance01.ReadColumn("man_p")
							t.sleep(10)	

						elif opc_m_c_p == 2:
							os.system('cls')

							
				
		#Act.tableros
		elif opc_m == 3:
			os.system('cls')

			Instance01 = ChargeState("PRECIOS")
			Instance01.InputData()
			

		#Se puede hacer un def
		#Calculo de consumo 
		elif opc_m == 4:
			os.system('cls')
			
			# Nota: Las listas son extensas podrian ser bidimencionales x manzana 
			# Do/Hacer: Hacer contadores para cada consumo, 
			# depende de si esta habitada y en que consuma y no 

			#Seguridad
			for i in range(len(supcubm2)):
				if supcubm2[i] > 0:
					Seg_cpls.append((Seg_cp/(M*LM))*2)

				else:
					Seg_cpls.append(Seg_cp/(M*LM))
			#Los prints verifican el correcto funcionamiento
			print("Seguridad",Seg_cpls)
			#Luz 
			for i in range(len(cons_luz)):
				luz_mls.append(luz_m * cons_luz[i])

			print("Luz",luz_mls)
			#Agua
			for i in range(len(cons_agua)):
				Agua_mls.append(Agua_m * cons_agua[i])
			print("Consumode agua",Agua_mls) 
			#Gas
			for i in range(len(cons_gas)):
				Gas_mls.append(Gas_m * cons_gas[i]) 
			print("Consumode gas",Gas_mls) 
			
			#Luz publica
			cont_luz_p = 0
			for i in range(len(luz_p)):
				
				if luz_p[i] == 'S':
			 
					cont_luz_p += 1 
			for i in range(len(luz_p)):
					if luz_p[i] == "S":
						Luz_cpls.append(Luz_cp / cont_luz_p)
					else:
						Luz_cpls.append(0)
			print("Luz publica",Luz_cpls)
			#con contador s o n 

			#Corregir
			#Agua publica 

			cont_Agua_cp = 0 
			for i in range(len(agua_p)):
				if agua_p[i] == 'S':
					
					cont_Agua_cp += 1 

			for i in range(len(agua_p)):
				if agua_p[i] == "S":
					Agua_cpls.append(cont_Agua_cp / Agua_cp)
				else:
					Agua_cpls.append(0)
			print("Agua publica ",Agua_cpls)
			
			#Asfalto
			cont_Asf_cp = 0 			 
			for i in range(len(asfalto)):
				if asfalto[i] == 'S':
					
					cont_Asf_cp += 1 

			for i in range(len(asfalto)):
				if asfalto[i] == "S":
					Asf_cpls.append(Asf_cp / cont_Asf_cp)
				else:
					Asf_cpls.append(0)
			print("Asfalto ",Asf_cpls)
			#Cochera 
			for i in range(len(cantvehi)):
				if cantvehi[i] != 0:
					Cochera_mls.append(cantvehi[i]*Cochera_m)  
				else:
					Cochera_mls.append(0)
			print("Cochera",Cochera_mls)

			#Terreno 
			for i in range(len(m_fren)):
				metros2.append(m_fren[i]*m_fond[i])
			for i in range(len(metros2)):
				Valorter_mls.append(metros2[i]*Valorter_m)
			print("Valor terreno",Valorter_mls)

			ban = True


		#Emitir liquidacion
		elif opc_m == 5:
			os.system('cls')
		
			#♪(´▽｀) Agregar opcion 2 (Por Manzana y Lote)
			if ban == True:
				table = [
      					["Por Nombre(Apellido)"],
      					["Por Manzana"],
      					["Por Manzana y Lote"],
      					["Volver"],]
				print(tabulate.tabulate(table, headers=["Option", "Description"],numalign="center", tablefmt=fontStyle, showindex=True))
				
				while True:
					opc_liq = val_range(3,0)

					if opc_liq == 0:
						print("Ingrese su appelido")
						opc_ap = val_strlist(opc_ap)
						print("Nombre | Lote | Manzana | Fecha de compra | Superficie cubierta | Precio ")
						for i in range(len(ap)):
							if ap[i] == opc_ap:
								
								print("{}  {}  {}  {}  {} ${}  ".format(opc_ap
																			,lot_p[i]
																			,manz_p[i]
																			,fc[i]
																			,supcubm2[i]
																			,Valorter_mls[i]))
								

					elif opc_liq == 1:

						print("Ingrese la Manzana")
						opc_manz = val_range(1,M)

						print("Nombre | Lote | Manzana | Fecha de compra | Superficie cubierta | Precio ")

						for i in range(len(ap)):
							if manz_p[i] == opc_manz:
								print("{}  {}  {}  {}  {} ${}  ".format(ap[i]
																			,lot_p[i]
																			,manz_p[i]
																			,fc[i]
																			,supcubm2[i]
																			,Valorter_mls[i]))

						print("Ingrese la manzana")
						opc_manz = val_range(1,M)
						print("Ingrese el lote")
						opc_lot = val_range(1,LM)

						print("Nombre | Lote | Manzana | Fecha de compra | Superficie cubierta | Precio ")

						for i in range(len(lot_p)):
							if lot_p[i] == opc_lot and manz_p[i] == opc_manz:
								print("{}  {}  {}  {}  {} ${}  ".format(ap[i]
																			,lot_p[i]
																			,manz_p[i]
																			,fc[i]
																			,supcubm2[i]
																			,Valorter_mls[i]))
					else:
						break
							
			else:
				print('Primero Calcular consumo con  la opcion "5" ')

			
	else:
		print("Solo puede ingresar los valores dentro de menu del 0-6")

