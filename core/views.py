from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse
from django.views import generic
from django.shortcuts import render
import os

from .forms import ContactForm


class HomeView(generic.TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plotly_html_file_path = os.path.join(settings.STATIC_ROOT, 'notebooks/charts/PCA3dplot.html')

        with open(plotly_html_file_path, 'r') as file:
            plot_div = file.read()
        context['plot_div'] = plot_div
    
        return context

class ContactView(generic.FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        messages.info(self.request, 'Dziękujemy za kontakt. Otrzymaliśmy wiadomość')
        name = form.cleaned_data.get('imię')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('wiadomość')
        full_message = f'''
            Otrzymano wiadomość od {name}, {email}
            ------------------------------------------------------
            {message}
            '''
        send_mail(
            subject='Otrzymano wiadomość',
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_valid(form)


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        return context

def data_science_view(request):
    plotly_html_file_path = os.path.join('STATIC', 'notebooks/charts/PCA3dplot.html')

    with open(plotly_html_file_path, 'r') as file:
        plot_div = file.read()

    context = {'plot_div': plot_div}
    return render(request, 'index.html', context)