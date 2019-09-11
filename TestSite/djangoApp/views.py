from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Sith, Recruit, Planet, Question
from django.core.mail import send_mail
from django.db.models import Count, F

def index(request):
    return render(request, 'djangoApp/home.html')

def sith(request):
    siths = Sith.objects.order_by('name')
    return render(request, 'djangoApp/sith.html', {'siths':siths})

def submit_sith(request):
    current_id = request.POST['chosen_sith_id']
    return HttpResponseRedirect(reverse('current_sith', args=(current_id)))

def recruit(request):
    questions = Question.objects.order_by('number')
    planets = Planet.objects.all()
    return render(request, 'djangoApp/recruit.html', {'planets':planets, 'questions':questions})

def current_sith(request, sith_id):
    sith = Sith.objects.get(id = sith_id)
    siths = Sith.objects.order_by('name')
    planet = sith.planet
    planet_name = planet.name
    allowed_recruits = Recruit.objects.filter(mentor = None, planet_id = planet.id)
    recruit_count = sith.recruit_set.all().count()
    answers = []
    for r in allowed_recruits:
        answers.append(r.get_answers())
    args = {'siths':siths, 'sith':sith, 'planet_name':planet_name, 'recruit_count':recruit_count,
            'allowed_recruits':allowed_recruits, 'answers':answers}
    return render(request, 'djangoApp/sithPage.html', args)

def save_recruit(request):
    r = Recruit(name = request.POST['name'], planet_id = request.POST['planet'], 
                age = request.POST['age'], email = request.POST['email'])
    r.save()
    answers = request.POST.getlist('answers[]')
    answers = list(map(int,answers))
    all_questions = Question.objects.all().values_list('id', flat = True)
    for i in all_questions:
        if i in answers:
            r.answer_set.create(question_id = i, choice = 1)
        else:
            r.answer_set.create(question_id = i, choice = 0)
    return HttpResponseRedirect(reverse('home'))

def accept_recruit(request, sith_id, recruit_id):
    recruit = Recruit.objects.get(id = recruit_id)
    recruit.mentor = Sith.objects.get(id = sith_id)
    recruit.save()
    #send_mail('Congratulations', 'some msg', "admin", recruit.email)
    return HttpResponseRedirect(reverse('current_sith', args = (sith_id,)))
    
def sith_info(request):
    siths_with_hands = Sith.objects.annotate(rec_count = Count('recruit')).filter(rec_count__gt = 1)
    siths = Sith.objects.order_by('id')
    recruits_count = []
    for s in siths:
        recruits_count.append(s.recruit_set.count())
    args = {'siths_with_hands':siths_with_hands, 'recruits_count':recruits_count,'siths':siths}
    return render(request, 'djangoApp/sithInfo.html', args)


