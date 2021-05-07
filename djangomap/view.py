from djangomap.forms import ContactForm
from django.views.generic.edit import FormView

from django.urls import reverse, reverse_lazy


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)