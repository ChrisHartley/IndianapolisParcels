from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from applicants.forms import NewApplicantSignupForm

def showUserSignup(request):
	form = NewApplicantSignupForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		else:
			print form.errors
	return render_to_response('signup.html', {
		'form': form,
		'title': "new user"
	}, context_instance=RequestContext(request))
