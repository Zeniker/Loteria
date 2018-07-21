from django.shortcuts import redirect


def index(request):
    # Redireciona para os jogos
    return redirect('dia_sorte')

