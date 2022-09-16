from multiprocessing import context
from django.shortcuts import render
from .models import *

# call your data from models
projectsData = Myprojects.objects.all()

context = {
    'projects': projectsData
}

# Create your views here.
def index(request):
    return render(request, 'index.html', context)