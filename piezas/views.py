from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from .forms import LoginForm, buyForm
from .models import coleccionista, pieza
from django.contrib import messages
from .forms import piezaForm, verColeccion, eliminarForm, piezaFormUpdate,editPiece
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError

input_id = None

def home(request):
    return render(request, 'home.html')

def editar(request):
    if request.method == 'POST':
        input_id = request.POST['id_input']
        return render(request, 'pages/piece/editarform.html')



def editarForm(request):
    if request.method == 'POST':
        form = editPiece(request.POST)
        input_id  = request.POST.get('id_pieza')
        instance = pieza.objects.get(id_pieza=input_id)
        print("enter")
        if form.is_valid():
            print("forms")
            instance.nombre = form.cleaned_data['nombre']
            instance.valor_facial = form.cleaned_data['valor_facial']
            instance.precio_avaluado = form.cleaned_data['precio_avaluado']
            instance.ceca = form.cleaned_data['ceca']
            instance.material = form.cleaned_data['material']
            instance.diametro = form.cleaned_data['diametro']
            instance.año = form.cleaned_data['año']
            instance.tipo_articulo = form.cleaned_data['tipo_articulo']
            instance.save()
            return redirect('mi_coleccion')
    else:
        form = editPiece()
    return render(request, 'editar.html', {'form':form})


"""
def editarForm(request):
    if request.method == "POST": 
        input_id = request.POST.get('id_input')
        formulario = piezaForm(request.POST)
        print("h")
        if formulario.is_valid():
            try:
                update_piece(formulario)
                print("Formulario valido")
                redirect('mi_coleccion')  # Guarda los datos en la base de datos
                    # Redirigir a una página de éxito o realizar otras acciones
            except Exception as e:
                    # Manejar el error
                print(f"Error al guardar los datos: {str(e)}")
                 
    else:
        print("g")
        formulario = piezaForm()
    
    return render(request, 'pages/piece/create.html', {'formulario': formulario})
"""
def help_editing(request):
    return render(request, 'pages/piece/editarform.html')


def eliminar(request):
    return render(request, 'eliminar.html', {'eliminar':eliminar})

def eliminar_form(request):
    if request.method == 'POST':
        id_input = request.POST['id_input']
        try:
            registro = pieza.objects.get(id_pieza=id_input)
            registro.delete()
            return redirect('mi_coleccion')  # Redirige a la página de inicio después de eliminar el registro
        except pieza.DoesNotExist:
            error_message = 'El ID ingresado no existe'
            return render(request, 'eliminar.html', {'error_message': error_message})
    else:
        return render(request, 'eliminar.html')

def buy(request):
    return render(request, 'buy.html')

def mi_coleccion(request):
    form = verColeccion(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            try:
                identificacion = request.POST.get('identificacion')
                Coleccionista = coleccionista.objects.get(identificacion = identificacion)
                resultados = pieza.objects.filter(coleccionista=Coleccionista)                
                return render(request, 'pages/piece/mostrarUpdate.html', {'piezas': resultados})
                for resultado in resultados:
                    render(request, 'pages/piece/update.html', {'form':form})
            except Exception as e:
                print(e)
    else:
        form = verColeccion()
    return render(request, 'pages/piece/update.html', {'form':form})

def signup(request):
    if request.method == "POST": 
        formulario = SignupForm(request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                print("Formulario valido")
                redirect('home')  # Guarda los datos en la base de datos
                # Redirigir a una página de éxito o realizar otras acciones
            except Exception as e:
                # Manejar el error
                print(f"Error al guardar los datos: {str(e)}")
                 
    else:
        formulario = SignupForm()
    
    return render(request, 'register.html', {'formulario': formulario})



##preguntar
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            identificacion = form.cleaned_data['Identificacion']
            password = form.cleaned_data['Password']
            print(identificacion, password)
            user = coleccionista.objects.get(Identificacion=identificacion, Password=password)
            
            if user:
                # Inicio de sesión exitoso
                # Puedes agregar tu lógica adicional aquí
                return redirect('home')  # Redirecciona a la página de inicio después del inicio de sesión exitoso
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = LoginForm()
    
    return render(request, 'registration/login.html', {'form': form})

    
def nueva_pieza(request):
    if request.method == "POST": 
        
        formulario = piezaForm(request.POST)
        print("h")
        if formulario.is_valid():
            try:
                formulario.save()
                print("Formulario valido")
                redirect('mi_coleccion')  # Guarda los datos en la base de datos
                # Redirigir a una página de éxito o realizar otras acciones
            except Exception as e:
                # Manejar el error
                print(f"Error al guardar los datos: {str(e)}")
                 
    else:
        print("g")
        formulario = piezaForm()
    
    return render(request, 'pages/piece/create.html', {'formulario': formulario})

def mostrar(request):
    piezas = pieza.objects.all()
    return render(request, 'mostrar.html', {'piezas': piezas})


def compra(request):
    if request.method == "POST": 
        
        formulario = buyForm(request.POST)
        id_comprador = request.POST.get('id_coleccionista')
        print(id_comprador)
        id_pieza = request.POST.get('id_pieza')
        print(id_pieza)
        if formulario.is_valid():
            try:
                formulario.save()
                update_buy(id_comprador, id_pieza)
                redirect('mostrar')
                # Guarda los datos en la base de datos
                # Redirigir a una página de éxito o realizar otras acciones
            except Exception as e:
                # Manejar el error
                print(f"Error al guardar los datos: {str(e)}")
    else:
        formulario = buyForm()
    
    return render(request, 'buy.html', {'formulario': formulario})

def update_buy(id_comprador, id_pieza):
    Coleccionista = coleccionista.objects.get(identificacion = id_comprador)
    instancia = pieza.objects.get(id_pieza = id_pieza)
    instancia.coleccionista = Coleccionista
    instancia.save()

def update_piece(form):
    print("entro")
    Coleccionista = coleccionista.objects.get(identificacion = form.cleaned_data["coleccionista"])
    print("hola",Coleccionista)
    instancia = pieza.objects.get(id_pieza = input_id)
    instancia.coleccionista = Coleccionista
    instancia.nombre = form.cleaned_data["nombre"]
    instancia.valor_facial = form.cleaned_data["valor_facial"]
    instancia.precio_avaluado = form.cleaned_data["precio_avaluado"]
    instancia.ceca = form.cleaned_data["ceca"]
    instancia.material = form.cleaned_data["material"]
    instancia.peso = form.cleaned_data["peso"]
    instancia.diametro = form.cleaned_data["diametro"]
    instancia.año = form.cleaned_data["año"]
    instancia.id_coleccion = form.cleaned_data["id_coleccion"]
    instancia.tipo_articulo = form.cleaned_data["tipo_articulo"]
    instancia.save()
