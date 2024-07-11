from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    count = cache.get('count', 0, version=user.pk)
    count += 1
    ip = request.META.get('REMOTE_ADDR')
    request.session['ip'] = ip
    cache.set('count', count, 60 * 60 * 24, version=user.pk)



