from django.shortcuts import render

# Create your views here.
def index_movie(request):
    return render(request,'index01_old.html')