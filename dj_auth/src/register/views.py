from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# test user cred- username: pc2810 password: $learndj$
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect ("/login")
    return render(request, 'index.html')

def loginUser(request):
    msg= None
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            msg="No account with these creadentials exist"
            # return render(request, 'login.html')
    context = {
        'msg':msg,
    }
    return render(request, 'login.html', context )

def logoutUser(request):
    logout(request)
    return redirect("/login")

class signupUser(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
