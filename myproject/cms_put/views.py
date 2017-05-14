from django.shortcuts import render
from django.http import HttpResponse
from cms_put.models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def home(request):

	if request.method == 'GET':

		lista_paginas = Pages.objects.all()
		respuesta = "<h1>Bienvenidos</h1>"
		respuesta += """
					<form action="" method='post'> 
						<br>Escribe un nombre:
						<input type="text" name="nombre" value="" /></br>
						<br>Escribe el contenido:
						<input type="text" name="pagina" value="" /></br>
						<input type="submit" value="Enviar" />
					</form>
					"""
		respuesta += "<h3>Lista con las paginas</h3>"
		for pagina in lista_paginas:
			respuesta += "<br><a href='" +pagina.nombre + "'>" + pagina.nombre + "</a></br>"
		return HttpResponse(respuesta)

	elif request.method == 'POST':
		nombre = request.POST['nombre']	
		pagina = request.POST['pagina']
		pag = Pages(nombre = nombre, pagina = pagina)
		pag.save()
		return HttpResponse("Name added correctly")
	elif request.method == 'PUT':
		body = request.body.decode('utf-8')
		nombre,pagina = body.split(",")
		pag = Pages(nombre = nombre, pagina = pagina)
		pag.save()
		return HttpResponse("Name added correctly")
	else:
		respuesta = "Method not valid"
		return HttpResponse(respuesta)

def nombre_pagina(request,nombre):
	try:
		pagina = Pages.objects.get(nombre = nombre)
		respuesta = pagina.pagina
	except Pages.DoesNotExist:
		respuesta = "pagina no encontrada"
	return HttpResponse(respuesta)
