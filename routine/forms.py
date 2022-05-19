from django.forms import ModelForm
from .models import routine, day

class RoutineForm(ModelForm):
    class Meta:
        model = routine # 사용할 모델
        fields = ['title', 'category', 'goal', 'is_alarm'] # UpdateForm에서 사용할 routine model의 속성

class DayForm(ModelForm):
    class Meta:
        model = day # 사용할 모델
        fields = ['day'] # DayForm에서 사용할 day model의 속성