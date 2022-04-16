from django.shortcuts import render,redirect
from .models import details
from .forms import detailform
from django.contrib import messages
# Create your views here.
def home(request):

    if request.method == 'POST':
        form = detailform(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = details.objects.all()
            return render(request,'index.html',{'all_items':all_items})

    else:
        all_items = details.objects.all()
        return render(request,'index.html',{'all_items':all_items})

def delete(request,list_id):
    item = details.objects.get(pk=list_id)
    item.delete()
    return redirect('home')
