import datetime
from django.shortcuts import render
from .models import CourseMaster, Reserver
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .forms import ReserverForm
from django.contrib.messages.views import SuccessMessageMixin
from .mixins import MonthWithScheduleMixin

def success(request, **kwargs):
    return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

class CourseListView(ListView):
    template_name = 'list.html'
    model = CourseMaster

class ReservationView(SuccessMessageMixin, CreateView):
    template_name = 'reservation.html'
    form_class = ReserverForm
    model = Reserver
    success_url = reverse_lazy('salon:success')
    success_message = '予約完了しました。'
    def form_valid(self, form):
        # commit=Falseで一時保存
        reserver_instance = form.save(commit=False)
        # ここでcourse_idを設定
        reserver_instance.course_id = form.cleaned_data['course_id']
        # 最終的な保存
        reserver_instance.save()
        return super().form_valid(form)

class MonthWithScheduleCalendar(MonthWithScheduleMixin, TemplateView):
    """スケジュール付きの月間カレンダーを表示するビュー"""
    template_name = 'month.html'
    model = Reserver
    date_field = 'reservation_date'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        # ReserverモデルとCourseMasterモデルのデータを取得
        reservers_with_courses = Reserver.objects.select_related('course').all()
        combined_data = []
        for reserver in reservers_with_courses:
            combined_item = {
                'id': reserver.course.id,
                'course_name': reserver.course.course_name,
            }
            combined_data.append(combined_item)
        context.update({
            'calendar_context': calendar_context,
            'combined_data': combined_data
        })
        return context