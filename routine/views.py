from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from rest_framework.decorators import api_view
from account.models import MyUser
from routine.forms import UpdateForm, UpdateDayForm
from routine.models import day, routine, routine_result

# Create your views here.

def index(request):
    """
        routine 생성/조회하는 메뉴 페이지 render
    """
    return render(request, 'routine/routineMenu.html')

@api_view(['GET'])
@login_required(login_url='account:login') # 로그인이 필요한 작업
def renderRoutineForm(request):
    """
        routine 입력 폼을 render
    """
    return render(request, 'routine/createRoutine.html')

@api_view(['POST'])
@login_required(login_url='account:login') # 로그인이 필요한 작업
def create(request):
    """
        routine 폼에 입력한 내용을 DB에 저장
    """
    user = MyUser.objects.get(pk=request.user.pk) # 생성된 user의 id 값을 가져옴

    title = request.POST.get('title')
    category = request.POST.get('category')  
    goal = request.POST.get('goal')
    is_alarm = True if request.POST.get('is_alarm') == 'true' else False
    days = request.POST.getlist('days[]')

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
        new_result = routine_result(
            result = 'NOT(안 함)',
            is_deleted = False,
            routine_id = new_routine
        )
        new_day.save()
    
    new_result.save()

    result_response = {
        "data": {
            "routine_id": new_routine.pk
        },
        "message": {
            "msg": "  .",
            "status": "ROUTINE_CREATE_OK"
        }
    }
    user_id = user.pk

    # return JsonResponse(result) 
    return redirect(reverse('routine:readAll', kwargs={'user_id':user_id})) # 전체 routine 보는 페이지

@login_required(login_url='account:login') # 로그인이 필요한 작업
def readAll(request, user_id):

    """
        사용자id로 저장된 모든 routine 조회 
    """
    routine_list = routine.objects.filter(account_id_id=user_id) # 접속한 user의 id값으로 routine 모두 조회
    
    context = {'routine_list': routine_list}

    """
        아래 result_response 다시 작성!! 
        data를 가지고 올 때 -> for문 쓰나?
    """
    result_response = {
        "data": [{
            "goal": "  2",
            "id": 1,
            "result": "NOT",
            "title": " !"
        },
        {
            "goal": "  2",
            "id": 1,
            "result": "DONE",
            "title": " !"
        }],
        "message": {
            "msg": "  .",
            "status": "ROUTINE_LIST_OK"
        }
    }

    return render(request, 'routine/routineList.html', context)

def loadResult(request, routine_day_id):
    """
        result 폼에 입력한 내용을 DB에 저장
        생성될 때 result가 기본적으로 'NOT(안함)'으로 기록되기에 update로 명명
    """

    return render(request, 'routine/updateResult.html')

def readOne(request, routine_id):
    """
        routine id로 선택한 일정 조회
    """
    routine_list = routine.objects.filter(pk=routine_id)
    routine_day_list = day.objects.filter(routine_id_id=routine_id)
    routine_result_list = routine_result.objects.filter(routine_id_id=routine_id)

    context = {
        'routine_list': routine_list,
        'routine_day_list': routine_day_list,
        'routine_result_list': routine_result_list,
    }   

    return render(request, 'routine/routineOne.html', context)

@login_required(login_url='account:login') # 로그인이 필요한 작업
def deleteRoutine(request, routine_id, routine_day_id):
    """
        선택된 routine_day를 삭제
    """
    selected_routine_day = day.objects.get(pk=routine_day_id)
    selected_routine_day.delete()
    return redirect(reverse('routine:readOne', kwargs={'routine_id': routine_id}))


@login_required(login_url='account:login') # 로그인이 필요한 작업
def updateRoutine(request, routine_id):
    if request.method == 'POST':
        selected_routine = routine.objects.get(pk=routine_id)
        selected_day = day.objects.filter(routine_id_id=routine_id)
        form = UpdateForm(request.POST, initial=selected_routine)

        for oneday in list(selected_day):
            dayform = UpdateDayForm(request.POST, initial=oneday)
            dayform.save()

        if form.is_valid():
            form.save()

    else:
        selected_routine = routine.objects.get(pk=routine_id)
        context = {'routine': selected_routine}
    
    return render(request, 'routine/updateRoutine.html', context)