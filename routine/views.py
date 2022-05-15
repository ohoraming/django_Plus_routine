from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from account.models import MyUser
from routine.models import day, routine
# Create your views here.

def index(request):
    return render(request, 'routine/routineMenu.html')

@api_view(['POST'])
def create(request):
    user = MyUser.objects.get(pk=request.user.pk) # 생성된 user의 id 값을 가져옴

    title = request.POST.get('title')
    category = request.POST.get('category')  
    goal = request.POST.get('goal')
    is_alarm = True if request.POST.get('is_alarm') == 'true' else False
    days = request.POST.getlist('days[]')

    print(user)

    new_routine = routine(
        account_id=user,
        title=title,
        category = category,
        goal = goal,
        is_alarm = is_alarm,
        is_deleted = False
    )

    new_day = day(
        day = days,
        routine_id = new_routine
    )

    new_routine.save()
    new_day.save()

    print(new_routine)

    result = {
        "data": {
            "routine_id": new_routine.pk
        },
        "message": {
            "msg": "  .",
            "status": "ROUTINE_CREATE_OK"
        }
    }

    return JsonResponse(result)

@api_view(['GET'])
def load_page(request):
    return render(request, 'routine/createRoutine.html')