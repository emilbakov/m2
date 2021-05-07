from djangomap.forms import ContactForm
from django.views.generic.edit import FormView
from django.core.mail import send_mail

from django.urls import reverse, reverse_lazy




class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # subject = 'Website Inquiry' 
		# body ={'name': form.cleaned_data['name'],'email': form.cleaned_data['email_address'],'message':form.cleaned_data['message']}
        # message = "\n".join(body.values())

		# try:
		# 	send_mail(subject, message,'eb.bakov@gmail.com', ['eb.bakov@gmail.com']) 
		# except BadHeaderError:
		# 	return HttpResponse('Invalid header found.')
		# return redirect ("main:homepage")      
        print(form)
        subject = 'Website Inquiry'
        body ={'name': form.cleaned_data['name'],'email': form.cleaned_data['email'],'message':form.cleaned_data['message']}
        message = "\n".join(body.values())
        send_mail(subject,message,'eb.bakov@gmail.com', ['eb.bakov@gmail.com'])

               
                
        return super().form_valid(form)

