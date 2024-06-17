from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from schedule.models import Schedule
from django.utils.formats import number_format
from django.db.models import Count


def count_today_schedules():
        today = timezone.now().date()
        return Schedule.objects.filter(day_schedule__date=today).count()


def total_price_today():
        today = timezone.now().date()
        total_price =  Schedule.objects.filter(day_schedule__date=today).aggregate(
                total=Sum('total_price'))['total'] or 0.00
        total_price = number_format(total_price, decimal_pos=2, force_grouping=True)

        return total_price


def total_price_current_month():
        today = timezone.now().date()
        first_day_of_month = today.replace(day=1)
        first_day_of_next_month = today.replace(day=1, month=today.month + 1)
        last_day_of_current_month = first_day_of_next_month - timezone.timedelta(days=1)

        total_price =Schedule.objects.filter(day_schedule__date__gte=first_day_of_month, 
        day_schedule__date__lte=last_day_of_current_month).aggregate(total=Sum('total_price'))['total'] or 0.00
        total_price = number_format(total_price, decimal_pos=2, force_grouping=True)

        return total_price


def get_last_7_days_totals():
    today = timezone.now().date()
    dates = [today - timedelta(days=i) for i in range(7)]
    totals = []

    for date in dates:
        total = Schedule.objects.filter(day_schedule__date=date).aggregate(total=Sum('total_price'))['total']
        totals.append({'date': date.strftime("%d/%m/%Y"), 'total': total if total else 0})

    return totals[::-1]


def get_last_7_days_service_counts():
    today = timezone.now().date()
    dates = [today - timedelta(days=i) for i in range(7)]
    counts = []

    for date in dates:
        count = Schedule.objects.filter(day_schedule__date=date).aggregate(total=Count('id'))['total']
        counts.append({'date': date.strftime("%d/%m/%Y"), 'count': count if count else 0})

    return counts[::-1]  