
# accounts/views.py
from django.shortcuts import render, redirect
from .forms import RegistroAdoptanteForm

def registro_adoptante(request):
    if request.method == 'POST':
        form = RegistroAdoptanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroAdoptanteForm()
    return render(request, 'registration/register.html', {'form': form})