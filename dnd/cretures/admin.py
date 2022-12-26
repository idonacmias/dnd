from django.contrib import admin

from .models import Creture, Adventurer, Player, Skills_proficiency
# Register your models here.


admin.site.register(Creture)
admin.site.register(Adventurer)
admin.site.register(Player)
admin.site.register(Skills_proficiency)
