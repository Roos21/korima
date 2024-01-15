from django.views.generic import TemplateView
from .forms import NewsletterSubscriberForm, ContactUsForm
from django.shortcuts import render
from django.contrib import messages

class HomePage(TemplateView):
    template_name = 'sites_kine/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsletter_form'] = NewsletterSubscriberForm()
        context['contact_form'] = ContactUsForm()
        return context

    def post(self, request, *args, **kwargs):
        newsletter_form = NewsletterSubscriberForm(request.POST)
        contact_form = ContactUsForm(request.POST)

        newsletter_saved = False
        contact_saved = False

        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request, "Vous êtes abonné à la newsletter !")
            newsletter_saved = True
            newsletter_form = NewsletterSubscriberForm()  # Réinitialisation du formulaire

        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Votre message a été envoyé !")
            contact_saved = True
            contact_form = ContactUsForm()  # Réinitialisation du formulaire

        context = self.get_context_data()
        context['newsletter_form'] = newsletter_form
        context['contact_form'] = contact_form

        if not (newsletter_saved or contact_saved):
            messages.warning(request, "Aucun formulaire valide n'a été soumis.")

        return self.render_to_response(context)
