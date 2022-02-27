from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'index.html')

def emergency(request):
  return render(request, 'emergency.html')

def preparation(request):
  return render(request, 'preparation.html')

def faq(request):
  return render(request, 'faq.html')

def groups(request):
  return render(request, 'groups.html')

def info(request):
  return render(request, 'info.html')

def signs(request):
  return render(request, 'signs.html')