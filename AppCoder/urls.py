from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('login/', views.login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name="Logout"),
    path('sign_up/', views.register, name="signup"),
    path('profile/', views.editarPerfil, name="EditarPerfil"),
    path('about/', views.about, name="About"),
    path('route_page/', views.route_page, name="Routepage"),
    

    path('pacientes', views.pacientes, name="Pacientes"),
    path('medicos', views.medicos, name="Medicos"),
    path('practicas', views.practicas, name="Practicas"),
    path('buscar/', views.buscar),

    path('lista_medicos/', views.leer_medicos, name="lista_medicos"),
    path('eliminarMedico/<id_medico>/', views.elimina_medico, name="EliminarMedico"),
    path('editarMedico/<pk>/', views.editar_medico, name="EditarMedico"),
    path('agregarMedico/', views.medicos, name="AgregaMedico"),

    path('lista_pacientes/', views.leer_pacientes, name="lista_pacientes"),
    path('eliminarpaciente/<id_paciente>/', views.elimina_paciente, name="EliminarPaciente"),
    path('editarPaciente/<pk>/', views.editar_paciente, name="EditarPaciente"),
    path('agregarPaciente/', views.pacientes, name="AgregaPaciente"),

    path('lista_practicas/', views.leer_practicas, name="lista_practicas"),
    path('eliminarpractica/<id_practica>/', views.elimina_practica, name="EliminarPractica"),
    path('editarPractica/<pk>/', views.editar_practica, name="EditarPractica"),
    path('agregarPractica/', views.practicas, name="AgregaPractica"),
   
   
]

