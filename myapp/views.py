from django.shortcuts import render
from myapp.models import Emp
from .forms import MyForm

# Create your views here.
def index(req):
    emp=Emp.objects.all()
    fm=MyForm()
    return render(req,'index.html',{'emp':emp,'fm':fm})

def grip(req):
    return render(req,'grip.html')

def engine(req):
    return render(req,'engine.html')

