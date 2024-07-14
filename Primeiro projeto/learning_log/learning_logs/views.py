from django.shortcuts import render

# Create your views here.

def index(request):
    """Pagina principal do learning_log"""
    return render(request, 'learning_logs/index.html')
