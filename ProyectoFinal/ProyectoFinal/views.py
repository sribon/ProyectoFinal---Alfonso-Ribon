from django.shortcuts import render
from accounts.models import Avatar


def home(request):
    if request.user.is_authenticated:
        avatares= Avatar.objects.filter(user=request.user)
        if avatares.count() != 0:
            return render(request,'page/home.html',{'url':avatares[0].imagen.url})
    return render(request,'page/home.html')


