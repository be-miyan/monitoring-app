from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Avg

from datetime import datetime as dt, timezone, timedelta
from django.utils.timezone import make_aware

from .models import Environment, Period, Photo


def date_range(start, stop, step=timedelta(hours=1)):
    """時間ごとのイテレータを生成"""
    current = start
    while current < stop:
        yield current
        current += step

def IndexView(request):
    return HttpResponseRedirect('/dashboard/login')

# TODO classベースからdefベースに変更する
class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request_period = context['period'] if 'period' in context.keys() else '' 
        all_periods = Period.objects.order_by('sort')

        # プルダウン設定
        selected_period = all_periods.filter(name__exact=request_period).first()
        if not selected_period:
               selected_period = all_periods.first()   

        context['selected_period'] = selected_period 
        context['nonselected_periods'] = all_periods.exclude(name__exact=request_period)
      

        # 集計期間設定
        step = selected_period.step 
        duration_from_start = selected_period.duration_from_start
        hour_setting = 0 if selected_period.isDailyData else dt.now().hour
        minute_setting = 0 if selected_period.isDailyData else dt.now().minute - dt.now().minute%10
        minute_setting = 0

        start_dt = dt.now().replace(hour=hour_setting, minute=minute_setting, second=0, microsecond=0) - duration_from_start
        end_dt = dt.now().replace(hour=hour_setting, minute=minute_setting, second=0, microsecond=0) + step

        # 集計情報取得 
        hour_avg = []
        for d in date_range(start_dt, end_dt, step):
            start = make_aware(d)
            end = make_aware(d + step)
            hour_avg.append(
                (d,
                 "All",
                 (Environment.objects.filter(
                     postdate__range=(start, end))).aggregate(Avg("temperature"))['temperature__avg'],
                 (Environment.objects.filter(
                     postdate__range=(start, end))).aggregate(Avg("pressure"))['pressure__avg'],
                 (Environment.objects.filter(
                     postdate__range=(start, end))).aggregate(Avg("humidity"))['humidity__avg'],
                 (Environment.objects.filter(
                     postdate__range=(start, end))).aggregate(Avg("lux"))['lux__avg'],
                 )
            )
        context['hour_avg'] = hour_avg

        # 画像取得
        context['photos'] = Photo.objects.order_by('-postdate')[:5]

        # 最新データ取得
        context['latest_environment_list'] = Environment.objects.order_by(
            '-postdate')[:10]

        return context
