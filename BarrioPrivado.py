from datetime import date
from datetime import datetime
import random
from sqlite3 import *

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



#Cargar listas 



#Descargar listas 



#Variables auxiliares

x = " "
y = " "

#----------------------

M = 4
LM = 6

#Variables del Lote

lot =  [] 
manz = []
m_fren = []
m_fond=  []
luz_p=     []
agua_p =   []
asfalto =  []
esquina =  []

#Variables del propietario 

ap = []
nom = []
lot_p = []
manz_p = []
fc = []
supcubm2 = []
habit = []
cantvehi = []
cons_luz = []
cons_agua = []
cons_gas = []

#Variables para el menu 

opc_manz = 0 
opc_lot = 0
opc_ap = ""
opc_c = 0

opc_m = 0  #Opciones Menu 
opc_m_c = 0 # Opciones Consultas 
opc_m_c_p = 0 # Opciones Consulta del propietario 
opc_m_c_l = 0 # Opciones Consultas del local 
opc_liq = 0 #Opciones de liquidacion
#Variables de precios

#Common pay(Cost) as cp
#Pay(Cost) as m

luz_m = 60
luz_mls = []
Agua_m = 30
Agua_mls = []
Gas_m = 45
Gas_mls = []
Cochera_m = 10000
Cochera_mls = []

#Common Pay
Seg_cp = 30000
Seg_cpls = []

Luz_cp = 80000
Luz_cpls = []

#X metro de frente 
Agua_cp = 40 
Agua_cpls = []
Asf_cp = 70 
Asf_cpls = []

#X metro cuadrado
metros2 = []
Valorter_m = 60000
Valorter_mls = []


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
		x = int(input(" ▶ "))

		if x >= maxim and x <= minin:
		
			return x
			break

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
			break
			 
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
		apes  = ["lopez","martines" ,"abalos" , "ramos", "faustino"]
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
		

def reingresar_lot(x):
	
	# La funcion le pregunta al usuario,
	# si esta seguro de lo que ingreso.
	
	print("Esta seguro de lo que ingreso?")
	tmp = sn(x)
	if tmp == "NO" or tmp == "N":
		#Advertencia 
		print("""Atencion si no esta seguro de los ingresos,
		 se borraran todos los datos recien ingresado. 
		 Los tendra que ingresar todo de nuevo. 

		 ¿Quiere continuar?""") 
		tmp_2 = sn(x)
		if tmp_2 == "SI" or tmp_2 == "S":
			lot.pop(-1) 
			manz.pop(-1) 
			m_fren.pop(-1) 
			m_fond.pop(-1) 
			luz_p.pop(-1) 
			agua_p.pop(-1) 
			asfalto.pop(-1) 
			esquina.pop(-1) 
			print("[+] Ultimos datos eliminados\n")

	else:
				print("Ingrese el valor $$")

def reingresar_prop(y):

	# La funcion le pregunta al usuario,
	# si esta seguro de lo que ingreso.

	print("Esta seguro de lo que ingreso?")
	tmp = sn(x)
	if tmp == "NO" or tmp == "N":
		#Advertencia 
		print("""Atencion si no esta seguro de los ingresos,
		 se borraran todos los datos recien ingresado. 
		 Los tendra que ingresar todo de nuevo. 

		 ¿Quiere continuar?""") 
		tmp_2 = sn(x)
		if tmp_2 == "SI" or tmp_2 == "S":
			apnom.pop(-1) 
			lot_p.pop(-1) 
			manz_p.pop(-1) 
			fc.pop(-1) 
			supcubm2.pop(-1) 
			habit.pop(-1) 
			cantvehi.pop(-1) 
			cons_luz.pop(-1) 
			cons_agua.pop(-1) 
			cons_gas.pop(-1) 
			print("[+] Ultimos datos eliminados\n")

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

c = 5

randomer(lot,1,4,c)
randomer(manz,1,4,c)
randomer(m_fren,30,70,c)
randomer(m_fond,30,50,c)
randomer(supcubm2,0,90,c)
randomer(habit,0,10,c)
randomer(cantvehi,0,3,c)
randomer(cons_luz,0,500,c)
randomer(cons_agua,0,500,c)
randomer(cons_gas,0,500,c)
randomer_bol(agua_p,c)
randomer_bol(luz_p,c)
randomer_bol(asfalto,c)
randomer_bol(esquina,c)
#Arreglar
randomer_fc(c)
randomer_nomap(c)
randomer(lot_p,1,4,c)
randomer(manz_p,1,4,c)

#Banderas
ban = False


print("Fecha de hoy :",date.today())
while True:
	
	print("-"*60,"""Menu principal:
		1_Altas de lotes 
		2_Altas de propietarios
		3_Consultas
		4_Act.tabla de consumos
		5_Calculo de consumo 
		6_Emitir liquidacion 
		0_Fin de tarea""","-"*60,sep = "\n")

	opc_m = numval(opc_m)

	if opc_m <= 6 and opc_m >= 0:		

		if opc_m == 0:
			break
		
		#Lotes
		elif opc_m == 1:
			
			#Validar que no se repita
			print("Ingrese lote al que pertenece")
			lot.append(numval(lot))
			print(lot)
			print("Ingrese la manzana a la que pertenece")
			manz.append(numval(manz))
			print(manz)
			nrep2(lot,manz)


			print("Ingrese los metros de frente que posee")
			m_fren.append(numval(m_fren))
			print(m_fren)
			print("Ingrese los metros de fondo que posee")
			m_fond.append(numval(m_fond))
			print("Ingrese metros cubiertos")
			supcubm2.append(numval(supcubm2))
			print(m_fond)
			print("Ingrese si posee luz publica ")
			luz_p.append(sn(luz_p))
			print(luz_p)
			print("Ingrese si posee agua publica ")
			agua_p.append(sn(agua_p))
			print(agua_p)
			print("Ingrese si posee asfalto ")
			asfalto.append(sn(asfalto))
			print(asfalto)
			print("Ingrese si posee una esquina")
			esquina.append(sn(esquina))
			print(esquina)

			reingresar_lot(x)

		#Propietarios
		elif opc_m == 2:
			#Arreglar
			print("Ingrese nombre del propietario ")
			nom.append(srtval(nom))
			print(nom)
			print("Ingrese apellido del propietario ")
			ap.append(srtval(ap))
			print(ap)
			
			#Validar que no se repita 
			print("Ingrese lote al que pertenece")
			lot_p.append(numval(lot_p))
			print(lot_p)
			print("Ingrese la manzana a la que pertenece")
			manz.append(numval(manz_p))
			print(manz_p)

			print("Ingrese la fech de compra")
			fc.append(fdecompra())
			print(fc)
			print("Ingrese la superficie cubierta total ")
			supcubm2.append(numval(supcubm2))
			print(supcubm2)
			print("Ingrese los habitante del hogar ")
			habit.append(numval(habit))
			print(habit)
			print("Ingrese los vehiculos que posee")
			cantvehi.append(numval(cantvehi))
			print(cantvehi)
			print("Ingrese el consumo de luz")
			cons_luz.append(numval(cons_luz))
			print(cons_luz)
			print("Ingrese el consumo de agua")
			cons_agua.append(numval(cons_agua))
			print(cons_agua)
			print("Ingrese el consumo de gas")
			cons_gas.append(numval(cons_gas))
			print(cons_gas)

			reingresar_prop(y)

			
		# #Consultas

		#Arreglar no vuelve a entrar
		elif opc_m == 3:
			while opc_m_c != 3:
				print("-"*60,"""Menu de consultas:
					1_Lotes
					2_Propietarios
					3_Volver""","-"*60,sep = "\n")
				
				opc_m_c = val_range(1,3)

				if opc_m_c == 1:
					while opc_m_c_l != 3:
						print("-"*60,"""Menu de consultas de lotes:
					1_Por manzana
					2_Por manzana y lote
					3_Volver""","-"*60,sep = "\n")

						opc_m_c_l = val_range(1,3)

						print("{} {} {} {} {} {} {} {}".format(manz
																		,lot
																		,m_fond
																		,m_fren
																		,agua_p
																		,luz_p
																		,asfalto
																		,esquina))
						if opc_m_c_l == 1:
							print("Ingrese la manzana que busca")
							print("{} {} {} {} {} {} {} {}".format(manz
																			,lot
																			,m_fond
																			,m_fren
																			,agua_p
																			,luz_p
																			,asfalto
																			,esquina))
							opc_manz = val_range(1,LM)

							print("""Manzana | lote | Mts_fondo | Mts_Frente | Agua | Luz | Asfalto | Esquina """)
							for i in range(len(lot)):
								if manz[i] == opc_manz:
									print("{}  {}  {}  {}  {}  {}  {}  {} ".format(opc_manz
																								,lot[i]
																								,m_fond[i]
																								,m_fren[i]
																								,agua_p[i]
																								,luz_p[i]
																								,asfalto[i]
																								,esquina[i]))

						elif opc_m_c_l == 2:
							
							print("Ingrese la manzana")
							opc_manz = val_range(1,M)
							print("Ingrese el lote")
							opc_lot = val_range(1,LM)
								
							print("""Manzana | lote | Mts_fondo | Mts_Frente | Agua | Luz | Asfalto | Esquina """)

							for i in range(len(lot)):
								if lot[i] == opc_lot and lot[i] == opc_lot:

									print("{}  {}  {}  {}  {}  {}  {}  {} ".format(opc_manz
																			,lot[i]
																			,m_fond[i]
																			,m_fren[i]
																			,agua_p[i]
																			,luz_p[i]
																			,asfalto[i]
																			,esquina[i]))

				elif opc_m_c == 2:

					while opc_m_c_p != 4:
						print("-"*60,"""Menu de consultas de propietario:
					1_Por Nombre(Apellido)
					2_Por Manzana
					3_Por Manzana y Lote 
					4_Volver""","-"*60,sep = "\n")

						opc_m_c_p = val_range(1,3)

						if opc_m_c_p == 1:
							print("Ingrese su appelido")
							opc_ap = val_strlist(opc_ap)
							print("Nombre | Lote | Fecha de compra | Superficie cubierta | Habitantes | Vehiculos | Consumo Luz | Consumo Agua | Consumo gas")
							for i in range(len(ap)):
								if ap[i] == opc_ap:
									
									print("{}  {}  {}  {}  {}  {}  {}  {}".format(opc_ap
																				,lot_p
																				,fc
																				,supcubm2
																				,habit
																				,cantvehi
																				,cons_luz
																				,cons_agua
																				,cons_gas))
									print(ap, nom)
									print("{}  {}  {}  {}  {}  {}  {}  {}".format(opc_ap+" "+nom[i]
																				,lot_p[i]
																				,fc[i]
																				,supcubm2[i]
																				,habit[i]
																				,cantvehi[i]
																				,cons_luz[i]
																				,cons_agua[i]
																				,cons_gas[i]))


						elif opc_m_c_p == 2:

							print("Ingrese la Manzana")
							opc_manz = val_range(1,M)

							print("Lote | Fecha de compra | Superficie cubierta | Habitantes | Vehiculos | Consumo Luz | Consumo Agua | Consumo gas")

							for i in range(len(ap)):
								if manz_p[i] == opc_manz:
									print("{}  {}  {}  {}  {}  {}  {}  {}".format(lot_p[i]
																				,fc[i]
																				,supcubm2[i]
																				,habit[i]
																				,cantvehi[i]
																				,cons_luz[i]
																				,cons_agua[i]
																				,cons_gas[i]))
						elif opc_m_c_p == 3:

							print("Ingrese la manzana")
							opc_manz = val_range(1,M)
							print("Ingrese el lote")
							opc_lot = val_range(1,LM)

							print("Lote | Fecha de compra | Superficie cubierta | Habitantes | Vehiculos | Consumo Luz | Consumo Agua | Consumo gas")

							for i in range(len(lot_p)):
								if lot_p[i] == opc_lot and manz_p[i] == opc_manz:
									print("{}  {}  {}  {}  {}  {}  {}  {}".format(lot_p[i]
																				,fc[i]
																				,supcubm2[i]
																				,habit[i]
																				,cantvehi[i]
																				,cons_luz[i]
																				,cons_agua[i]
																				,cons_gas[i]))

				
		#Act.tableros
		elif opc_m == 4:

			print("""¿Quiere modificar algunos de los costos?
				
				Opciones:

				1 ▶Luz de hogar		${}
				2 ▶Agua de hogar	${}
				3 ▶Gas				${}
				4 ▶Cochera			${}
				5 ▶Seguridad		${}
				6 ▶Luz				${}
				7 ▶Agua publica		${}
				8 ▶Asfalto 			${}
				9 ▶Valor x m2		${}\n"""
								.format(luz_m
								,Agua_m
								,Gas_m
								,Cochera_m
								,Seg_cp
								,Luz_cp
								,Agua_cp
								,Asf_cp
								,Valorter_m
								))

			var_mod(val_range(1,9))

		#Se puede hacer un def
		#Calculo de consumo 
		elif opc_m == 5:
			
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
		elif opc_m == 6:
			


			if ban == True:
				print("-"*60,"""Menu de liquidacion:
					1_Por Nombre(Apellido)
					2_Por Manzana
					3_Por Manzana y Lote 
					4_Volver""","-"*60,sep = "\n")
				while True:
					opc_liq = val_range(1,4)

					if opc_liq == 1:
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
								

					elif opc_liq == 2:

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

# from tkinter import * 
# from tkinter import messagebox

# #Ventana Raiz 
# a = Tk()

# #Configuracion 
                          
# a.iconbitmap('logo.ico')
# a.title("Barrio Privado")
# a.geometry("400x500+500+100")
# a.config(bg = "#349BA8")

# # b =  " "
# # w = Spinbox(a, from_=0, to=10000,textvariable= b)
# # w.pack()			
# # print(b)


# #Defs
# #Hacer boton de guardar datos

# #Validar solo letras, si encuentra numeros lo elimina
# # def Validar_num_true(cuadro):
# # 	cuadraso_num=cuadro.get()
# # 	for i in cuadraso:
# # 		if i not in '0123456789':
# # 		cuadraso.delete(cuadraso.index(i), cuadraso.index(i)+1)

# # 	validate_entry = lambda text: text.isdecimal()

# # #----------------------
# # #Validar solo numeros, si encuentra una letra la elimina
# # def Validar_letra_true():
# # 	cuadraso_str=cuadro.get()
# # 	for i in cuadraso_str:
# # 		if i not in 'abcdefghijklmnñopqrstuvwxz.-_}[]{?¿¡!#$%&/()+*:;|°':
# # 		cuadraso_str.delete(cuadraso_str.index(i), cuadraso_str.index(i)+1)

# def button1():
# 	a1 = Tk()

# 	#1Configuracion
# 	a1.iconbitmap('logo.ico')
# 	a1.title("Barrio Privado ")
# 	a1.geometry("400x500+0+0")
# 	a1.config(bg= "#246C75")
# 	l1 = Label(a1, text = "Ingreso de datos" , bg ="#67A1A8").pack(pady = 15)
# 	b = Button(a1,text = "Salir", bg ="#67A1A8", command = lambda:exit(a1) ).pack(side = "bottom", pady = 10)	
# 	e1 = Entry(a1, bg = "#349BA8",  )
# 	e1.insert(0,"Manzana")

# 	e1.pack(pady  = 10)
# 	e1 = Entry(a1, bg = "#349BA8", )
# 	e1.insert(0,"Lote")

# 	e1.pack(pady  = 10)
# 	e1 = Entry(a1, bg = "#349BA8",)
# 	e1.insert(0,"Metros de frente")

# 	e1.pack(pady  = 10)
# 	e1 = Entry(a1, bg = "#349BA8", )
# 	e1.insert(0,"Metros de fondo")

# 	e1.pack(pady  = 10)
	
# 	#Hacer booleanas
# 	e1 = Entry(a1, bg = "#349BA8", )
# 	e1.insert(0,"Luz publica")

# 	e1.pack(pady  = 10)
# 	e1 = Entry(a1, bg = "#349BA8", )
# 	e1.insert(0,"Agua publica")

# 	e1.pack(pady  = 10)
# 	e1 = Entry(a1, bg = "#349BA8", )
# 	e1.insert(0,"Asfalto")

# 	e1.pack(pady  = 10)
# 	e1 = Entry(a1, bg = "#349BA8", )
# 	e1.insert(0,"Esquina")

# 	e1.pack(pady  = 10)

# #Hacer boton de guardar datos
# def button2():
# 	a2 = Tk()

# 	#Configuracion
# 	a2.iconbitmap('logo.ico')
# 	a2.title("Barrio Privado ")
# 	a2.geometry("400x500+950+0")
# 	a2.config(bg= "#246C75")
# 	b = Button(a2,text = "Salir", bg ="#67A1A8", command = lambda:exit(a2) ).pack(side = "bottom", pady = 10)	
# 	l1 = Label(a2, text = "Ingreso de datos" , bg ="#67A1A8").pack(pady = 15)
# 	e2 = Entry(a2, bg = "#349BA8")
# 	e2.insert(0,"Nombre")
# 	e2.pack(pady  = 10)
# 	e2 = Entry(a2, bg = "#349BA8")
# 	e2.insert(0,"Apellido")
# 	e2.pack(pady  = 10)
# 	e2 = Entry(a2, bg = "#349BA8")
# 	e2.insert(0,"Lote")
# 	e2.pack(pady  = 10)
# 	e2 = Entry(a2, bg = "#349BA8")
# 	e2.insert(0,"Manzana")
# 	e2.pack(pady  = 10)
# 	#Hacerlo bien ⬇
# 	e2 = Entry(a2, bg = "#349BA8")
# 	e2.insert(0,"Fecha de compra")
# 	e2.pack(pady  = 10)
# 	e2 = Entry(a2, bg = "#349BA8")
# 	e2.insert(0,"Habitantes")
# 	e2.pack(pady  = 10)
# 	e2 = Entry(a2, bg = "#349BA8")
# 	e2.insert(0,"Vehiculos")
# 	e2.pack(pady  = 10)
# 	e2 = Entry(a2, bg = "#349BA8")
# 	e2.insert(0,"Consumo de luz")
# 	e2.pack(pady  = 10)
# 	e2 = Entry(a2, bg = "#349BA8")
# 	e2.insert(0,"Consumo de Agua")
# 	e2.pack(pady  = 10)
# 	e2 = Entry(a2, bg = "#349BA8")
# 	e2.insert(0,"Consumo de Gas")
# 	e2.pack(pady  = 10)

# def button3():
# 	messagebox.showinfo(title= "Barrio Privado", message = "Datos Calculados")

# def button4():
# 	a4 = Tk()

# 	#Configuracion
# 	a4.iconbitmap('logo.ico')
# 	a4.title("Barrio Privado ")
# 	a4.geometry("400x350+800+200")
# 	a4.config(bg= "#246C75")
# 	l4 = Label(a4, text = " Tabla de consumo ", bg = "#67A1A8", font = "Unispace").pack(fill = "x")

# 	l4 = Label(a4, text = "  Propietario ", bg = "#349BA8").pack(fill = "x", pady = 10 )
# 	b = Button(a4, text = " Nombre ", bg = "#67A1A8").pack(pady = 5, ipadx = 50)
# 	b = Button(a4, text = " Manzana ", bg = "#67A1A8").pack(pady = 5, ipadx = 50)
# 	b = Button(a4, text = " Manzana y lote ", bg = "#67A1A8").pack(pady = 5, ipadx = 35)
# 	l4 = Label(a4, text = " Lote ", bg = "#349BA8").pack(fill = "x", pady = 10 )
# 	b = Button(a4, text = " Manzana ", bg = "#67A1A8").pack(pady = 5, ipadx = 50)
# 	b = Button(a4, text = " Manzana y lote ", bg = "#67A1A8").pack(pady = 5, ipadx = 35)
# 	b = Button(a4,text = "Salir", bg ="#67A1A8", command = lambda:exit(a4) ).pack(side = "bottom", pady = 10)	

# def button5():
# 	a5 = Tk()

# 	#Configuracion
# 	a5.iconbitmap('logo.ico')
# 	a5.title("Barrio Privado ")
# 	a5.geometry("400x350+200+200")
# 	a5.config(bg= "#246C75")
# 	l5 = Label(a5, text = " Consultas ", bg = "#67A1A8").pack(fill = "x" )

# 	l4 = Label(a5, text = "  Propietario ", bg = "#349BA8").pack(fill = "x", pady = 10 )
# 	b = Button(a5, text = " Nombre ", bg = "#67A1A8").pack(pady = 5, ipadx = 50)
# 	b = Button(a5, text = " Manzana ", bg = "#67A1A8").pack(pady = 5, ipadx = 50)
# 	b = Button(a5, text = " Manzana y lote ", bg = "#67A1A8").pack(pady = 5, ipadx = 35)
# 	l4 = Label(a5, text = " Lote ", bg = "#349BA8").pack(fill = "x", pady = 10 )
# 	b = Button(a5, text = " Manzana ", bg = "#67A1A8").pack(pady = 5, ipadx = 50)
# 	b = Button(a5, text = " Manzana y lote ", bg = "#67A1A8").pack(pady = 5, ipadx = 35)
# 	b = Button(a5,text = "Salir", bg ="#67A1A8", command = lambda:exit(a5) ).pack(side = "bottom", pady = 10)	
# def button6():
# 	a6 = Tk()

# 	#Configuracion
# 	a6.iconbitmap('logo.ico')
# 	a6.title("")
# 	a6.geometry("400x450+500+500")
# 	a6.config(bg= "#246C75")
# 	b = Button(a6,text = "Salir", bg ="#67A1A8", command = lambda:exit(a6) ).pack(side = "bottom", pady = 10)
# 	lab = Label(a6, text = "Liquidacion " , bg = "#38585C", font = " Unispace" , pady = 10 , fg  = "White" )
# 	lab.pack(fill = X)
# 	#Entry o label ??!?
# 	et = Entry(a6,bg = "#349BA8")
# 	et.insert(0, "Manzana")
# 	et.pack(pady = 5)
# 	et = Entry(a6,bg = "#349BA8")
# 	et.insert(0, "Lote")
# 	et.pack(pady = 5)
# 	et = Entry(a6,bg = "#349BA8")
# 	et.insert(0, "Propietario")
# 	et.pack(pady = 5)
# 	et = Entry(a6,bg = "#349BA8")
# 	et.insert(0, "Ultima fecha de compra")
# 	et.pack(pady = 5)
# 	et = Entry(a6,bg = "#349BA8")
# 	et.insert(0, "Precio del terreno")
# 	et.pack(pady = 5)
# 	et = Entry(a6,bg = "#349BA8")
# 	et.insert(0, " Metros cubiertos")
# 	et.pack(pady = 5)
# 	et = Entry(a6,bg = "#349BA8",justify = "center")
# 	et.insert(0, " 🔽Reseña del propietario🔽 ")
# 	et.config(state = "disable")
# 	et.pack(fill = "x", pady = 10)
# 	etT = Text(a6,bg = "#349BA8",height=7,width=40)
# 	etT.pack()
# def exit(a):
# 	a.destroy()

# #Labels

# l = Label(a,text = "Menu principal",justify = "center",bg= "#38585C",font = "Unispace", fg = "white").pack(fill = "x",ipady =10)
# l2 = Label(a, text = "Altas ",bg = "#246C75" ).pack(fill = "x", pady = 5)
# l3 = Label(a, text = "Consumo ",bg = "#246C75" )
# l4 = Label(a, text = "Liquidacion ",bg = "#246C75" )
# l5 = Label(a, text = "			 ",bg = "#246C75" )

# #Butons

# b = Button(a,text = "Alta de lotes", bg ="#67A1A8", command = button1).pack(pady =5, ipadx = 51)
# b = Button(a,text = "Alta de propietarios", bg ="#67A1A8", command = button2).pack(pady =5, ipadx = 32)
# l3.pack(fill = "x", pady = 15)
# b = Button(a,text = "Calculo de consumo", bg ="#67A1A8", command = button3).pack(pady =5, ipadx = 29)
# b = Button(a,text = "Tabla de consumo", bg ="#67A1A8", command = button4).pack(pady =5, ipadx = 35)
# b = Button(a,text = "Consultas", bg ="#67A1A8", command = button5).pack(pady =5, ipadx = 57)
# l4.pack(fill = "x", pady = 15)
# b = Button(a,text = "Liquidacion", bg ="#67A1A8", command = button6).pack(pady =5, ipadx = 22)
# l5.pack(fill = "x", pady = 15)
# b = Button(a,text = "Salir", bg ="#67A1A8", command = lambda:exit(a) ).pack()

# a.mainloop()


