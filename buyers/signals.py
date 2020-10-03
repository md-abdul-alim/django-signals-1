from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Buyer

#user will tell the buyer that i create a user. please create a buyer instance to this user
@receiver(post_save, sender = User)
def post_save_create_buyer(sender, instance, created, **kwargs):
	print('sender:', sender) #sender means which function or library sending request
	print('instance:', instance) #instanc means the create user
	print('created:', created) #boolian signal. if the user create newly. it will send true signal
								# if the user update profile it will send false signal.

	if created:
		Buyer.objects.create(user=instance)