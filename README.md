# Sistema de Práctica de Pacientes CODER HOUSE

# INTEGRANTE: 
++ Sebastián Di Pierro

# PROYECTO: 
++ El proyecto “Sistema de Practica de Pacientes CODER” pretende cumplir con las instancias finales de la entrega del curso Phyton en CODERHOUSE. El mismo se utilizó como lenguaje de programación backend del sistema, por ser un lenguaje interpretado, no compilado, fuertemente tipado dinámico y multiplataforma. Además, se utilizó como frontend el framework Django de desarrollo web y de código abierto escrito en Python. Por último, como sistema de base de datos se utilizó SQLite.

El proyecto fue diseñado, programado y terminado de acuerdo a los lineamientos de CODER HOUSE.

# LINK DEL VIDEO EXPLICATIVO: 
https://bit.ly/Entrega_Final_Python



# CASOS DE PRUEBA

# CASO DE PRUEBA 1 // Nombre del Use Case: Búsqueda del paciente en el sistema por documento.  

Actor Principal: Usuario del sistema	Actor Secundario: S/D
Objetivo: Realizar el registro de los pacientes en el sistema propuesto.

Precondiciones:  Que el paciente se encuentre registrado previamente en el sistema.
Éxito: Se muestre por pantalla el paciente consultado por número de documento.
Fracaso 1: que el paciente no se encuentre registrado en el sistema.
Fracaso 2: que el paciente tenga mal ingresado su número de documento.

Curso Normal

1.  El CU comienza cuando el usuario (PA) selecciona en la opción de búsqueda del paciente en el sistema a través del botón * Buscar paciente por documento	
++ Alternativas
Si el usuario se encuentra logueado en el sistema puede acceder a través del botón * Listar pacientes registrados

Curso Normal

2. El sistema muestra en la pantalla de inicio del sistema el resultado de la búsqueda.	
++ Alternativas
Si el paciente no existe indicará “El documento ingresado no se encuentra en la base de datos”.
Si el dato fue mal ingresado en el sistema indicará “Paciente con documento mal ingresado. Supera 8 dígitos”.

Curso Normal

3. Se muestra el resultado de la búsqueda satisfactoria del paciente en la pantalla de inicio con los datos de Nombre, Apellido y Número de documento.	 
4. Fin de CU.
************************************************************************************************

# CASO DE PRUEBA 2 // Nombre del Use Case: Gestión de médicos registrados - CRUD	Nro. de Orden: 2

Actor Principal: Médico del sistema.	Actor Secundario: S/D
Objetivo: Realizar el registro de los médicos en el sistema propuesto. Procede al ALTA, BAJA o MODIFICACÓN de los datos en el sistema.
Precondiciones:  Que el médico se encuentre registrado previamente en el sistema.

Éxito: Se pueda realizar el CRUUD de manera satisfactoria.
Fracaso 1: no se considera dato que se muestran sólo los médicos registrados.

Curso Normal

1.  El CU comienza cuando el usuario selecciona en la opción Listas médicos registrados desde la pantalla de incio del sistema.	
++ Alternativas
Si el usuario se encuentra logueado en el sistema puede acceder a través del botón Listar médicos registrados
El usuario logueado puede acceder desde el link route_page/ y listar el listado de médicos registrados.

Curso Normal

2. El sistema muestra en pantalla el Listado de Médicos registrados con Nombre, Apellido y Profesión. Además, permite la gestión de ABM a través de la opción Agregar nuevo médico, Eliminar y Editar.	
++ Alternativas
Si el usuario no se encuentra logueado en el sistema no puede acceder al Listado de médicos ni desde la pantalla de inicio ni desde el link route_page/

3. Se procede a la Edición del médico y luego se confirman los cambios.	 
4. Se procede a la eliminación del médico desde pantalla.	
5. Fin de CU.

************************************************************************************************

# CASO DE PRUEBA 3 // Nombre del Use Case: Registro de alta de usuarios en el sistema.  	Nro. de Orden: 3

Actor Principal: Usuario del sistema.	Actor Secundario: S/D
Objetivo: Realizar el registro de los médicos en el sistema propuesto. Procede al ALTA, BAJA o MODIFICACÓN de los datos en el sistema.
Precondiciones:  Que el usuario no se encuentre registrado previamente en el sistema.
 
Éxito: Se pueda registrar el usuario de manera satisfactoria.
Fracaso 1: No coincida la clase de acceso. 
Fracaso 2: El usuario ya existe en el sistema.

Curso Normal

1.  El CU comienza cuando el nuevo usuario selecciona en la opción Registrarse - Login desde la pantalla de incio del sistema.	
++ Alternativas
El nuevo usuario puede acceder desde el link route_page/ y Pagina de registro de usuario.

2. El sistema muestra en pantalla el formulario de registro de usuario con datos de NOMBRE DE USUARIO y PASSWORD con su confirmación.	
++ Alternativas
Si el usuario ya existe en el sistema mostrara un mensaje en la pantalla de inicio “El usuario NO se ha creado correctamente. Verifique”
Si los datos ingresados en el password y su confirmación no coinciden el sistema mostrara un mensaje en la pantalla de inicio “El usuario NO se ha creado correctamente. Verifique”

3. Se procede a la creación del nuevo usuario y mensaje de confirmación en la pantalla de inicio “El usuario se ha creado correctamente!. 
Se muestra mensaje de bienvenida en la barra superior del sistema.	 
4. Fin de CU.


Fecha Creación: 08/02/2022

