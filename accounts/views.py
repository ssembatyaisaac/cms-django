from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def signup_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      #log the user in
      login(request, user)
      return redirect('articles:list')
  else:
    form = UserCreationForm()
  return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      #login the user
      user = form.get_user()
      login(request, user)
      return redirect('articles:list')
  else:
    form = AuthenticationForm()
  return render(request, 'accounts/login.html', {'form': form})