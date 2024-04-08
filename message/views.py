from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def index(request):
    messages = createMessage.objects.all()

    return render(request, 'index.html',{'messages':messages})


def messages(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            name_surname = form.cleaned_data['username']
            description = form.cleaned_data['description']
            # Veritabanına yeni bir mesaj oluştur
            createMessage.objects.create(username=name_surname, description=description)
        return redirect('home')
    else:
        form = MessageForm() 
    return render(request, 'message.html', {'form':form})

def nasılÇalışır(request):
    return render(request, 'nasılÇalışır.html') 