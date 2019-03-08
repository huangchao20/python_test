from django.shortcuts import render

# Create your views here.

def showinfo(request):
    return render(request, 'showinfo.html')