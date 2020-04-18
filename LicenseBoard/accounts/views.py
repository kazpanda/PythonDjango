from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from .forms import SignUpForm, UserInformationUpdateForm


def signup(request):
    import pdb
    pdb.set_trace()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('licenses:home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


'''
def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        gender = request.POST['gender']
        birth_date = request.POST['birth_date']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.profile.gender = gender
        user.profile.birth_date = birth_date
        user.save()
    return render(request, 'registration/sign_up.html')
'''


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    form_class = UserInformationUpdateForm
    template_name = 'my_account.html'
    success_url = reverse_lazy('licenses:my_account')

    def get_object(self):
        return self.request.user
