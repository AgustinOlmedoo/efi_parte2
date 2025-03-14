from django.contrib.auth import (
    authenticate,
    login, 
    logout,
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View

from usuarios.forms import UserRegisterForm
from django.contrib import messages 
from usuarios.models import Profile

class LoginView(View):
    def get(self, request):
        return render(request, 'home/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                messages.warning(request, 'Nombre de usuario o contraseña incorrectos.')

        return render(request, 'home/login.html')
    



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'home/register.html'

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            dict(
                form=form
            )
        )
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

        return render(
            request,
            self.template_name,
            dict(
                form=form
            )
        )


def about_us(request):
    return render(request, 'home/sobre_nosotros.html')

class UpdateLang(View):
    def get(self, request):
        profile= Profile.objects.get(user=request.user)
        lang= profile.language
        if lang =='es':
            profile.language= 'en'
        if lang=='en':
            profile.language = 'es'
        profile.save()
        return redirect(request.META.get('HTTP_REFERER', 'index'))

def index_view(request):
    return render(
        request,
        'home/index.html'
    )
