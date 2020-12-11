from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from common.BootstrapFormMixin import BootstrapFormMixin

User = get_user_model()
#
# def get_redirect_url(params):
#     redirect_url = params.get('return_url')
#     return redirect_url if redirect_url else 'index'
#
from radionator.profiles.forms import LoginForm


class LogIn(LoginView, BootstrapFormMixin, SuccessMessageMixin):
    template_name = 'profiles/login.html'
    form_class = LoginForm
    success_message = f'Welcome! '




# class LogIn(View):
#     def get(self, request):
#         context = {
#             'login_form': LoginForm()
#         }
#         return render(request, 'profiles/log3in.html', context)
#
#     def post(self, request):
#         login_form = LoginForm(request.POST)
#
#         if login_form.is_valid():
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#
#             return_url = get_redirect_url(request.POST)
#
#             if user:
#                 login(request, user)
#                 return redirect(return_url)
#         return render(request, 'profiles/log3in.html')

