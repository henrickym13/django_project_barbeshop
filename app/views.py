from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import metrics


def login_user(request):
    if request.user.is_authenticated:
        return render('index')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else: 
            return redirect('login')
    else:
        return render(request, 'login.html')
        

def logout_user(request):
    logout(request)
    return redirect('login')


def index(request):
        quantity = metrics.count_today_schedules()
        total_price_day = metrics.total_price_today()
        total_price_month = metrics.total_price_current_month()
        totals = metrics.get_last_7_days_totals()
        counts = metrics.get_last_7_days_service_counts()

        context  = {
            'quantity': quantity,
            'total_price_day':total_price_day,
            'total_price_month': total_price_month,
            'totals': totals,
            'counts': counts,
            'username': request.user.username,
        }

        return render(request, 'index.html', {'context': context})
