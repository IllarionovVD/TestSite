from django.contrib import admin

# Register your models here.
from .models import Planet, Sith, Recruit, Question, Answer

admin.site.register(Planet)
admin.site.register(Sith)
admin.site.register(Recruit)
admin.site.register(Question)
admin.site.register(Answer)
