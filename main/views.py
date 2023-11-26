import sqlite3
from datetime import datetime
from BurnOutMarkUps.crunches import count_crunches
from BurnOutMarkUps.messages import count_messages
from BurnOutMarkUps.task import count_tasks
from BurnOutMarkUps.commits import count_commits_for_bad_situations
from BurnOutAlgorithm import algorithm
from UsersPreferedDates.dates import parse_dates_db
from UsersPreferedDates.dates import start_date, end_date

from django.shortcuts import render
from django.http import HttpResponse
from .forms import DateForm
from .models import Persons, BurnedPeople, Date
# Create your views here.
def index(request):
    start_date = None
    end_date = None

    persons = Persons.objects.all()
    burnedPeople = BurnedPeople.objects.all()

    if request.method == 'POST':
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')

        # Преобразование строк в объекты datetime
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
            Date.objects.create(start_date=start_date, end_date=end_date)
            # --- каждый SUPPOSE возвращает словарь, необходимый для нашего решения
            algorithm.count_burnout_chance(suppose_commits=count_commits_for_bad_situations(),
                                           suppose_tasks=count_tasks(start_date),
                                           suppose_crunches=count_crunches(start_date, end_date),
                                           suppose_messages=count_messages())
        except ValueError:
            # Обработка ошибки неверного формата даты
            pass

        # if request.method == 'POST':
        #     start_date = request.POST.get('start_date')
        #     end_date = request.POST.get('end_date')
        #     Date.objects.create(start_date=start_date, end_date=end_date)




    return render(request, 'main/index.html',{'persons': persons, 'burnedPeople': burnedPeople, 'start_date': start_date, 'end_date': end_date})





def about(request):
    return render(request, 'main/index.html')


