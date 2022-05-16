from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from rest_framework.decorators import api_view
from account.models import MyUser
from routine.models import day, routine

# Create your views here.

@login_required(login_url='account:login') # 로그인이 필요한 작업시 추가
def index(request):
    return render(request, 'routine/routineMenu.html')

@api_view(['POST'])
# @login_required(login_url='account:login') # 로그인이 필요한 작업시 추가
def create(request):
    user = MyUser.objects.get(pk=request.user.pk) # 생성된 user의 id 값을 가져옴

    title = request.POST.get('title')
    category = request.POST.get('category')  
    goal = request.POST.get('goal')
    is_alarm = True if request.POST.get('is_alarm') == 'true' else False
    days = request.POST.getlist('days[]')

    print(request.POST.get('is_alarm'))

    new_routine = routine(
        account_id = user,
        title = title,
        category = category,
        goal = goal,
        is_alarm = is_alarm,
        is_deleted = False
    )
    new_routine.save()
    for dd in days:
        new_day = day(
            day = dd,
            routine_id = new_routine
        )
        new_day.save()

    print(user)
    print(new_routine.category)

    result = {
        "data": {
            "routine_id": new_routine.pk
        },
        "message": {
            "msg": "  .",
            "status": "ROUTINE_CREATE_OK"
        }
    }
    user_id = user.pk

    # return JsonResponse(result) # 여기서 바로 render할 수는 없나???
    return redirect(reverse('routine:readAll', kwargs={'user_id':user_id})) # 전체 routine 보는 페이지

@api_view(['GET'])
def load_page(request):
    return render(request, 'routine/createRoutine.html')

@login_required(login_url='account:login') # 로그인이 필요한 작업시 추가
def readAll(request, user_id):
    """
        사용자id로 저장된 모든 routine 조회 
    """
    routine_list = routine.objects.filter(account_id_id=user_id) # 접속한 user의 id값으로 routine 모두 조회
    context = {'routine_list': routine_list}
    return render(request, 'routine/routineList.html', context)

