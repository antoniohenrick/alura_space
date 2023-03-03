from django.shortcuts import render

# Função responsável pela página principal
def index(request):
    return render(request, 'galeria/index.html')

# Função responsável pelas imagens das outras páginas
def imagem(request):
    return render(request, 'galeria/imagem.html')




