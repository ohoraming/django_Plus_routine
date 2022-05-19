from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from rest_framework.decorators import api_view
from routine.forms import RoutineForm
from account.models import MyUser
from routine.models import day, routine, routine_result

# Create your views here.

@api_view(['GET'])
@login_required(login_url='account:login') # 로그인이 필요한 작업
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
    print(request)
    print(request.GET)
    print(request.POST)
    """
        routine 폼에 입력한 내용을 DB에 저장
    """
    user = MyUser.objects.get(pk=request.user.pk) 

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
        new_day.save()

    new_result = routine_result(
        result = 'NOT',
        is_deleted = False,
        routine_id = new_routine
    )
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

    return JsonResponse(result_response) 
    # return redirect(reverse('routine:readAll')) # 전체 routine 보는 페이지

@login_required(login_url='account:login') # 로그인이 필요한 작업
@api_view(['GET'])
def readAll(request):
    """
        사용자id로 저장된 모든 routine과 result 조회 
    """
    routine_list = routine.objects.filter(account_id_id=request.user.pk).order_by('routine_id') # 접속한 user의 id값으로 routine 모두 조회
    routine_result_list = routine_result.objects.all()

    
    context = {
        'routine_list': routine_list,
        'routine_result_list': routine_result_list
        }

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

@api_view(['GET'])
def readOne(request, routine_id):
    """
        routine id로 선택한 일정 조회
    """
    routine_list = routine.objects.get(pk=routine_id)
    routine_result_list = routine_result.objects.get(routine_id_id=routine_id)
    routine_day_list = day.objects.filter(routine_id_id=routine_id)

    context = {
        'routine_list': routine_list,
        'routine_result_list': routine_result_list,
        'routine_day_list': routine_day_list,
    }   

    result_response = {
        "data": {
            "goal": "  2",
            "id": 1,
            "result": "NOT",
            "title": " !",
            "days": ["MON", "TUE", "FRI"],
        },
        "message": {
            "msg": "  .",
            "status": "ROUTINE_DETAIL_OK"
        }
    }

    return render(request, 'routine/routineOne.html', context)

@api_view(['POST'])
def updateResult(request, routine_id):
    """
        선택한 routine의 result 수정
    """
    if request.method == 'POST':
        routine_list = routine.objects.filter(routine_id=routine_id).order_by('routine_id') # 접속한 user의 id값으로 routine 모두 조회
        selected_result = routine_result.objects.filter(routine_id_id=routine_id)

        selected_result.delete()
        new_result = request.POST.get('result')
        
        changed_result = routine_result(
            result = new_result,
            routine_id_id = routine_id
        )
        changed_result.save()
    else:
        routine_list = routine.objects.filter(account_id_id=request.user.pk).order_by('routine_id') # 접속한 user의 id값으로 routine 모두 조회
        selected_result = routine_result.object.get(routine_id_id=routine_id)

    context = {
        'routine_list': routine_list,
        'routine_result_list': selected_result
        }
    
    return render(request, 'routine/routineList.html', context)

@api_view(['GET'])
@login_required(login_url='account:login') # 로그인이 필요한 작업
def deleteDay(request, routine_id, routine_day_id):
    """
        선택한 routine_day 삭제
    """
    selected_routine_day = day.objects.get(pk=routine_day_id)
    selected_routine_day.delete()
    
    return redirect(reverse('routine:readOne', kwargs={'routine_id': routine_id}))

@api_view(['GET'])
@login_required(login_url='account:login') # 로그인이 필요한 작업
def deleteRoutine(request, routine_id, user_id):
    """
        선택한 routine 삭제
    """
    selected_routine = routine.objects.get(pk=routine_id)
    selected_routine.delete()

    result_response = {
        "data": {
            "account_id": user_id,
            "routine_id": routine_id,
        },
        "message": {
            "msg": "  .",
            "status": "ROUTINE_DELETE_OK"
        }
    }

    return redirect(reverse('routine:readAll'))

@api_view(['GET','POST'])
@login_required(login_url='account:login') # 로그인이 필요한 작업
def updateRoutine(request, routine_id):
    """
        선택한 routine 수정
    """
    if request.method == 'POST':
        selected_routine = routine.objects.get(pk=routine_id)
        selected_day = day.objects.filter(routine_id_id=routine_id)
        
        form = RoutineForm(request.POST, instance=selected_routine)

        days = request.POST.getlist('days[]')

        selected_day.delete()

        for new_day in days:
            df = day(
                day = new_day,
                routine_id_id=routine_id
            )
            df.save()

        if form.is_valid():
            form.save()
        return redirect(reverse('routine:readAll'))
    else:
        selected_routine = routine.objects.get(pk=routine_id)

    context = {'routine': selected_routine}
    
    return render(request, 'routine/updateRoutine.html', context)