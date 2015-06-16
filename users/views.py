from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

def user_profile(request):

	return render_to_response('users/profile.html', {
		'title': "profile"
	}, context_instance=RequestContext(request))

