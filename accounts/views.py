from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created you can now log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')