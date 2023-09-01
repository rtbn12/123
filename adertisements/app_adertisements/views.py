from django.shortcuts import render,redirect,reverse
from .models import Advertisment
from.forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy






def index(request):
    advertisements = Advertisment.objects.all()
    context={'advertisements': advertisements }
    return render(request,'app_adertisements/index.html',context)



def top_sellers(request):return render(request,'app_adertisements/top-sellers.html')




@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
   if request.method =='POST':
       form= AdvertisementForm(request.POST,request.FILES)
       if form.is_valid():
           # advertisement= Advertisment(**form.cleaned_data)
           advertisement = form.save(commit=False)
           advertisement.user= request.user
           advertisement.save()
           return redirect(reverse("main-page"))
   form = AdvertisementForm()
   context = {'form': form}
   return render(request, 'app_adertisements/advertisement-post.html', context)












