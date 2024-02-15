from django.urls import path
from .views import IndexView, CourseListView, ReservationView, MonthWithScheduleCalendar
from . import views

app_name = 'salon'

urlpatterns = [
    path('', IndexView.as_view(), name='top'),
    path('list/', CourseListView.as_view(), name='course'),
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('reservation/<int:id>', ReservationView.as_view(), name='reservation'),
    path('success/', views.success, name='success'),
    path('', MonthWithScheduleCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>/', MonthWithScheduleCalendar.as_view(), name='month'),
]
