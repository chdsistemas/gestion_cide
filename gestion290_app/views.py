from django.shortcuts import render, redirect, get_object_or_404
from gestion290_app.models import *
from gestion290_app.forms import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash



def home(request):
    return render(request, 'home.html')


def insertar_usuario(request):
    if request.method == 'POST':
        formulario = FormularioUsuario(request.POST)
        if formulario.is_valid():
            usuario = formulario.save(commit=False)  # No guarda aún en la BD: debe se cifra la contraseña antes de
            usuario.set_password(formulario.cleaned_data['password'])  # Cifra la contraseña
            usuario.save()  # Ahora sí se guarda
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('insertar_usuario')
        else:
            messages.error(request, 'Hay algunos errores en el registro. Vuelva a intentar...')
    else:
        formulario = FormularioUsuario()
    return render(request, 'usuario/insertar.html', {'formulario': formulario})



def listar_usuarios(request):
    usuarios = Usuario.objects.all() # Seleccionar todos los usuarios
    return render(request, 'usuario/listar.html', {'usuarios':usuarios}) # Dibujar el template



@login_required
def actualizar_usuario(request):
    usuario = request.user  # Usuario logueado
    if request.method == 'POST':
        formulario = FormularioUsuario(request.POST, instance=usuario)
        if formulario.is_valid():
            usuario = formulario.save(commit=False)  # Aún no guardar en la BD
            nueva_password = formulario.cleaned_data.get('password')
            if nueva_password:
                usuario.set_password(nueva_password)
            usuario.save()  # Ahora sí guardamos todo en la BD
            update_session_auth_hash(request, usuario)  # Mantiene la sesión activa después de actualizar la contraseña            
            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('perfil_usuario')
        else:
            messages.error(request, 'Hay errores en el formulario. Verifica los datos.')
    else:
        formulario = FormularioUsuario(instance=usuario)
    return render(request, 'usuario/actualizar.html', {'formulario': formulario})



def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('listar_usuarios')



def login_usuario(request):
    if request.method == 'POST':
        # Si los input no están vacíos:
        if ((request.POST.get('username') != None) and (request.POST.get('password')) != None):
            username_recibido = request.POST.get('username')
            password_recibido = request.POST.get('password') 
            autenticar = authenticate(
                username = username_recibido, 
                password = password_recibido
                )
            if autenticar is not None: # Si variable autenticar no es vacía
                login(request, autenticar) # Guarda datos de la sesión en el navegador
                return redirect('home')
            else:
                mensaje_error = 'Credenciales incorrectas, intente de nuevo'
                return render(request, 'usuario/login.html', {'mensaje_error': mensaje_error})
    else:
        return render(request, 'usuario/login.html')
    


def logout_usuario(request):
    logout(request)
    return redirect('home')
# endregion


# region rol

def insertar_rol(request):
    if request.method == "POST":
        form = FormularioRol(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_roles')
    else:
        formulario = FormularioRol()
    return render(request, 'rol/insertar.html', {'formulario': formulario})



def actualizar_rol(request, id):
    rol = get_object_or_404(Rol, id=id)
    if request.method == 'POST':
        rol.nombre = request.POST.get('nombre')
        rol.descripcion = request.POST.get('descripcion')
        rol.save()
    else:
        return render(request, 'rol/actualizar', {'rol':rol})



def eliminar_rol(request, id):
    rol = get_object_or_404(Rol, id=id)
    rol.delete()
    return redirect('listar_roles')



def listar_roles(request):
    roles = Rol.objects.all()
    return render(request, ['rol/listar.html', 'usuario/insertar.html'], {'roles':roles})



def ver_mi_perfil(request):
    usuario_registrado = request.user
    usuario = Usuario.objects.get(id=usuario_registrado.id)
    return render(request, 'usuario/detallar.html', {'usuario': usuario})


