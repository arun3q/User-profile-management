from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.gis.geoip2 import GeoIP2


def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)	
		if form.is_valid():
			location = getLocation(request)
			
			user = form.save(commit=False)
			user.location = location
			email = form.cleaned_data.get('email')
			user.save()
			messages.success(request, "Account created for {}! You can now login.".format(email))
			return redirect('login')
	else:
		form = UserRegisterForm()
	
	return render(request, 'users/register.html', {'form': form})

def getLocation(request):
	g = GeoIP2()
	
	ip = request.META.get('HTTP_X_FORWARDED_FOR', None)
	if not ip:
		ip = request.META.get('REMOTE_ADDR', None)
	country = ip
	if ip:
		try:
			country = g.country(ip)['country_code'].lower()
		except:
			country = 'au'
	return country
	#http://api.hostip.info/flag.php?ip=1.186.178.45

@login_required
def profile(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST,
									request.FILES, 
									instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, "Your account is updated!.")
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
		
	if request.user.location:
		user_location = request.user.location.lower()
	else:
		user_location = "au"
	country_flag = "http://assets.ipstack.com/flags/"+user_location+".svg"
	
	context = {
		'u_form': u_form,
		'p_form': p_form,
		'country_flag':country_flag
	}
	return render(request, 'users/profile.html', context)