from ast import Pass
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Paciente, Practica, Medico
from AppCoder.forms import  PracticaFormulario, PacienteFormulario, MedicoFormulario, UserEditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.mixins import 
from django.contrib.auth.decorators import login_required




# Create your views here.


def inicio(request):

      return render(request, "AppCoder/inicio.html")

def buscar(request):
      
      if(len(request.GET["documento_pac"]))<=8:
            documento_pac = request.GET['documento_pac'] 
            paciente = Paciente.objects.filter(documento_pac__icontains=documento_pac)
            if not paciente:
                  return render(request, "AppCoder/inicio.html", {"error":"El documento ingresado no se encuentra en la base de datos"})
            return render(request, "AppCoder/inicio.html", {"pacientes":paciente, "documento_pac":documento_pac})
      else: 
            respuesta = "Paciente con documento mal ingresado. Supera 8 dígitos."
            return render(request, "AppCoder/inicio.html", {"error":respuesta})
      #No olvidar from django.http import HttpResponse

#ALTA PACIENTE
def pacientes(request):

      if request.method == 'POST':

            miFormulario = PacienteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid():   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  paciente = Paciente (nombre=informacion['nombre'], Apellido=informacion['Apellido'], documento_pac=informacion['documento_pac']) 
                  
                  paciente.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PacienteFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/pacientes.html", {"miFormulario":miFormulario})

#LISTAR PACIENTES
@login_required
def leer_pacientes (request):
     
      pacientes = Paciente.objects.all()

      return render (request, "AppCoder/lista_pacientes.html", {"pacientes":pacientes})

#ELIMINA PACIENTE
def elimina_paciente (request, id_paciente):

      paciente = Paciente.objects.get(id=id_paciente)

      paciente.delete()

      paciente = Paciente.objects.all()

      return render(request, "AppCoder/lista_pacientes.html", {"pacientes":paciente})

#UPDATE PACIENTE
def editar_paciente(request, pk):

      #Recibe el nombre del profesor que vamos a modificar
      paciente = Paciente.objects.get(pk=pk)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = PacienteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid():   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
                  
                  paciente.nombre = informacion['nombre']
                  paciente.Apellido = informacion['Apellido']
                  paciente.documento_pac = informacion['documento_pac']

                  paciente.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= PacienteFormulario(initial={'nombre': paciente.nombre, 'Apellido':paciente.Apellido , 'documento_pac':paciente.documento_pac}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarPaciente.html", {"miFormulario":miFormulario, "paciente_nombre":pk})





#LISTA DE MEDICOS
@login_required
def leer_medicos(request):
     
      medicos = Medico.objects.all()

      return render (request, "AppCoder/lista_medicos.html", {"medicos":medicos})

#ALTA MEDICO
def medicos(request):

      if request.method == 'POST':

            miFormulario = MedicoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid():   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  medico = Medico (nombre=informacion['nombre'], Apellido=informacion['Apellido'], Profesion=informacion['Profesion']) 

                  medico.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= MedicoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/medicos.html", {"miFormulario":miFormulario})

#ELIMINAR MEDICO
def elimina_medico(request, pk):

      medico = Medico.objects.get(pk=pk)

      medico.delete()

      medicos = Medico.objects.all()

      return render(request, "AppCoder/lista_medicos.html",{"medicos":medicos})

#UPDATE MEDICO
def editar_medico(request, pk):

      #Recibe el nombre del profesor que vamos a modificar
      medico = Medico.objects.get(pk=pk)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = MedicoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid():   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  medico.nombre = informacion['nombre']
                  medico.Apellido = informacion['Apellido']
                  medico.Profesion = informacion['Profesion']

                  medico.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= MedicoFormulario(initial={'nombre': medico.nombre, 'Apellido':medico.Apellido , 'Profesion':medico.Profesion}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarMedico.html", {"miFormulario":miFormulario, "medico_nombre":pk})

#ALTA PRACTICA

def practicas(request):


      if request.method == 'POST':

            miFormulario = PracticaFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid():   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  practica = Practica (practica_nombre=informacion['practica_nombre'], documento_pac=informacion['documento_pac'], fecha_practica=informacion['fecha_practica']) 

                  practica.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PracticaFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/practicas.html", {"miFormulario":miFormulario})


#LISTAR PRACTICAS
@login_required
def leer_practicas(request):
     
      practicas = Practica.objects.all()

      return render (request, "AppCoder/lista_practicas.html", {"practicas":practicas})

#ELIMINA PRACTICA
def elimina_practica(request, id_practica):

      practica = Practica.objects.get(id=id_practica)

      practica.delete()

      practica = Practica.objects.all()

      return render(request, "AppCoder/lista_practicas.html", {"practicas":practica})

#UPDATE PRACTICA
def editar_practica(request,pk):

      #Recibe el nombre del profesor que vamos a modificar
      practica = Practica.objects.get(pk=pk) 

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = PracticaFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid():   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
                  
                  practica.practica_nombre = informacion['practica_nombre']
                  practica.fecha_practica = informacion['fecha_practica']
                  practica.documento_pac = informacion['documento_pac']
                  practica.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= PracticaFormulario(initial={'practica_nombre': practica.practica_nombre, 'fecha_practica':practica.fecha_practica , 'documento_pac':practica.documento_pac}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarPractica.html", {"miFormulario":miFormulario, "practica_nombre":pk})

#LOGIN

def login_request(request):
      
      if(request.method =='POST'):

            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():

                  data = form.cleaned_data

                  user = authenticate(username=data['username'], password = data['password'])

                  if user is not None:
                        
                        login(request, user)

                        return render(request, 'Appcoder/inicio.html', {'mensaje': f'Bienvenido {user.get_username()}'})
                       # return render(request, 'Appcoder/', {'mensaje': f'Bienvenido {user.get_username()}'})
                  else:

                         return render(request, 'Appcoder/inicio.html', {'mensaje': f'Error de autenticación. Por Favor pruebe nuevamente'})

            else:

                   return render(request, 'Appcoder/inicio.html', {'mensaje': f'No se realizaron cambios. Verifique'})  

      else:

            form =AuthenticationForm()
            return render(request, 'AppCoder/login.html', {'form': form})

def register(request):

      if (request.method =='POST'):

            form=UserCreationForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request, 'AppCoder/inicio.html', {"mensaje":"El usuario se ha creado correctamente!"})

            else:

                  return render(request, 'AppCoder/inicio.html', {"mensaje":"El usuario NO se ha creado correctamente. verifique"})

      else:

            form=UserCreationForm()
            return render(request, 'AppCoder/registro.html',{"form": form})

          
def editarPerfil(request):

      usuario = request.user

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = UserEditForm(request.POST) #aquí mellega toda la información del html

            if miFormulario.is_valid():   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.first_name = informacion['first_name']
                  usuario.last_name = informacion['last_name']

                  usuario.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UserEditForm(initial={'email': usuario.email,'password1': usuario.password,'first_name': usuario.first_name,'last_name': usuario.last_name}) 
           

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

def about(request):
     
     return render (request, 'AppCoder/about.html')

def route_page(request):
     
     return render (request, 'AppCoder/route_page.html')