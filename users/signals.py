from django.db.models.signals import post_save
from .models import Profile
from django.conf import settings
from django.dispatch import receiver
from django.contrib.gis.geoip2 import GeoIP2

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def build_profile_on_user_creation(sender, instance, created, **kwargs):
  if created:
    profile = Profile(user=instance)
    
    profile.save()

def getCountry(request):
	g = GeoIP2()
	ip = request.META.get('REMOTE_ADDR', None)
	if ip:
		city = g.city(ip)['city']
	else:
		city = 'Rome' # default city	
