from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

from .models import UserProfile

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username)|Q(email = username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# Create your views here.
@csrf_exempt
def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get("logname", "")
        pass_word = request.POST.get("password", "")
        print user_name, pass_word
        # send to db to authenticate if the value correct, if not, set user None
        user = authenticate(username = user_name, password = pass_word)
        # use method login, write into request
        print user
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login.html", {})
    elif request.method == "GET":
        return render(request, "login.html", {})

