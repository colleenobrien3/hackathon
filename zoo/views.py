from django.shortcuts import render, redirect
from .models import ZooUser
from .forms import ZooUserForm
# Create your views here.

def zoo_home(request):
    return render(request, 'zoo_home.html')

def zoo_user_create(request):
    if request.method == 'POST':
        form = ZooUserForm(request.POST)
        # if form.is_valid and request.POST['first_name'].isalpha():
        if form.is_valid():
            user = form.save()
            return redirect('zoo_home')
        
    else:
        form = ZooUserForm()
        return render(request, 'zoo_user_form.html', {'form': form})
