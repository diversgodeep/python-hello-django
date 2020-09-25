import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from hello.forms import logMessageForm
from hello.forms import logMessage
from django.views.generic import ListView

def home(request):
  return render(request, "hello/home.html")

def about(request):
  return render(request, "hello/about.html")

def contact(request):
  return render(request, "hello/contact.html")

def hello_there(request, name):
  return render (
    request,
    'hello/hello_there.html',
    {
      'name': name,
      'date': datetime.now()
    }
  )

def log_message(request):
  form = logMessageForm(request.POST or None)

  if request.method == "POST":
    if form.is_valid():
      message = form.save(commit=False)
      message.log_date = datetime.now()
      message.save()
      return redirect("home")
  else:
    return render(request, "hello/log_message.html", {"form": form})
