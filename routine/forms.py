from django.forms import ModelForm
from .models import routine, day

class UpdateForm(ModelForm):
    class Meta:
        model = routine
        fields = ['title', 'category', 'goal', 'is_alarm']

class UpdateDayForm(ModelForm):
    class Meta:
        model = day
        fields = ['day']