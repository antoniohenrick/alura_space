from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

# Função responsável pela página principal
def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {'cards': fotografias})

# Função responsável pelas imagens das outras páginas
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})




