import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender='movies.Person')
def congratulatory(sender, instance, created, **kwargs):
    if created and instance.birth_date == datetime.date.today():
        print(f"У {instance.full_name} сегодня день рождения! 🥳")