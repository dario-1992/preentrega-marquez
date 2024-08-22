from django.shortcuts import render, HttpResponse
from .models import Cliente, Producto, Entrega 
from Registro.models import Cliente

# Create your views here.

def Inicio(req):
    return render(req, "Registro/index.html")

def Cliente(req):
     return render(req, "Registro/clientes.html")
def Producto(req):
     return render(req, "Registro/productos.html")

def Entrega(req):
     return render(req, "Registro/entregas.html")

def cliente_formulario(req):

     if req.method == "POST":

          cliente = Cliente(nombre=req.POST["nombre"],telefono=req.POST["telefono"],email=req.POST["email"])

          cliente.save()

          return render(req,"Registro/index.html")

     return render(req,"Registro/clienteFormulario.html")