from django.urls import path
from . import views

urlpatterns = [
    path('schedule/', views.ScheduleListView.as_view(), name='schedule_list'),
    path('schedule/create/', views.ScheduleListCreate.as_view(), name='schedule_create'),
    path('schedule/<int:pk>/detail/', views.ScheduleListDetail.as_view(), name='schedule_detail'),
    path('schedule/<int:pk>/update/', views.ScheduleListUpdate.as_view(), name='schedule_update'),
    path('schedule/<int:pk>/delete/', views.ScheduleListDelete.as_view(), name='schedule_delete'),
]