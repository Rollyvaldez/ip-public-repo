# capa de vista/presentación
# si se necesita algún dato (lista, valor, etc), esta capa SIEMPRE se comunica con services_nasa_image_gallery.py

from django.shortcuts import redirect, render
from .layers.services import services_nasa_image_gallery
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# función que invoca al template del índice de la aplicación.
def index_page(request):
    return render(request, 'index.html')

# auxiliar: retorna 2 listados -> uno de las imágenes de la API y otro de los favoritos del usuario.
def getAllImagesAndFavouriteList(request):
    images = []
    favourite_list = []
    images = services_nasa_image_gallery.getAllImages(request)
    favourite_list = services_nasa_image_gallery.getAllFavouritesByUser

    return images, favourite_list

# función principal de la galería.
def home(request):
    # llama a la función auxiliar getAllImagesAndFavouriteList() y obtiene 2 listados: uno de las imágenes de la API y otro de favoritos por usuario*.
    # (*) este último, solo si se desarrolló el opcional de favoritos; caso contrario, será un listado vacío [].
    images = []
    favourite_list = []
    images,favourite_list = GetAllImagesAndFavouriteList(request) # 2 variables separadas por una coma a las que se le asigna la funcion anterior,
                                                                  # ya que esta retorna ambas listas en una misma linea de codigo
    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list} ) # La funcion render toma 3 parametros y retorna una respuesta http
    # primero el objeto(request) a peticion del usuario, segundo la plantilla que se va a renderizar 'home.html' y
    # por ultimo un contexto(diccionario) delimitado por unas llaves '{'images': images, 'favourite_list': favourite_list}' que marca las
    # variables que estaran dentro de la plantilla en este caso las listas 'images' y 'favourite_list' con sus valores correspondientes


# función utilizada en el buscador.
def search(request):
    images, favourite_list = getAllImagesAndFavouriteList(request)
    search_msg = request.POST.get('query', '')

    # si el usuario no ingresó texto alguno, debe refrescar la página; caso contrario, debe filtrar aquellas imágenes que posean el texto de búsqueda.
    pass


# las siguientes funciones se utilizan para implementar la sección de favoritos: traer los favoritos de un usuario, guardarlos, eliminarlos y desloguearse de la app.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', {'favourite_list': favourite_list})


@login_required
def saveFavourite(request):
    pass


@login_required
def deleteFavourite(request):
    pass


@login_required
def exit(request):
    pass
