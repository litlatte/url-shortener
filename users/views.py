from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import CreateView
from .forms import SignUpForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.



def profile_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('/account/login')
    else:
        ctx = {
            'slugs': request.user.slugs.all()
        }
        return render(request, 'registration/profile.html', context=ctx)

class SignUpView(SuccessMessageMixin, UserPassesTestMixin, CreateView):
    form_class = SignUpForm
    success_url = '/account'
    template_name = 'registration/signup.html'
    success_message = '%(username)s account was created successfully. Login to continue'
    permission_denied_message = _("You are already registered!")

    def form_save(self, form):
        form.save()
        return HttpResponseRedirect('/account', request=self.request)


    def test_func(self):
        return self.request.user.is_anonymous

    
    def handle_no_permission(self):
        return HttpResponseRedirect('/account')