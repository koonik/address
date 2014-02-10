from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from forms.models import Address, AddressForm


def index(request):
    address_list = Address.objects.all()[:50]
    template = loader.get_template('forms/index.html')
    context = RequestContext(request, {
        'address_list': address_list,
    })
    return HttpResponse(template.render(context))


def address(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = AddressForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            form.save()
            return HttpResponseRedirect('/forms/')    # Redirect after POST
    else:
        form = AddressForm() # An unbound form

    return render(request, 'forms/address.html', {'form': form, })