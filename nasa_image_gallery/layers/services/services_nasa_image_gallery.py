# capa de servicio/lógica de negocio

from ..transport import transport
from ..dao import repositories
from ..generic import mapper
from django.contrib.auth import get_user

def getAllImages(input=None):#El parámetro 'input' indica si se debe buscar por un valor introducido en el buscador.
    #Creamos dos listas vacías:
    coleccion_json = []
    imagenes = [] 
    #Llama a la función desde transport.py y obtiene el listado de imágenes y las guarda en una de las listas.
    coleccion_json = transport.getAllImages(input=None)
    #Recorre el listado anterior.
    for imagen in coleccion_json:
        #Transforma cada imagen en una NASA Card con la función de mapper.py y lo agrega en el listado vacío de imágenes.
        NASA_card = mapper.fromRequestIntoNASACard(imagen)  
        imagenes.append(NASA_card) #Agrega cada imagen a la lista.
    return imagenes


def getImagesBySearchInputLike(input):
    return getAllImages(input)


# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request del template en una NASACard.
    fav.user = '' # le seteamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.


# usados en el template 'favourites.html'
def getAllFavouritesByUser(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositorio TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            nasa_card = '' # transformamos cada favorito en una NASACard, y lo almacenamos en nasa_card.
            mapped_favourites.append(nasa_card)

        return mapped_favourites


def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.
