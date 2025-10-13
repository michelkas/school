from django.shortcuts import render

def custom_404_view(request,exception=None):
    return render(request, "404.html",
                {
                    "code": 404,
                    "titre":"Page Non Trouver",
                      "messages":"la page que vous recherhcez a peut-etre été supprimée, son nom a changer ou elle est temporairement indisponible"},
                status=404)

def custom_500_view(request, exception=None):
    return render(request, '404.html',
                  {"code": 500,
                   "titre":"Erreur Serveur",
                   "messages":"les données sont temporairement indisponible"},
                  status=500)
