from django.urls import path
from . import views as staff_views

app_name = 'staff_module'
urlpatterns = [
    path('', staff_views.staff_home_page, name='home'),

    # departments
    path('departments/', staff_views.StaffDepartmentList.as_view(), name='department_list'),
    path('departments/<int:pk>', staff_views.StaffDepartmentDetail.as_view(), name='department_detail'),

    # projects
    path('projects/', staff_views.StaffProjectList.as_view(), name='project_list'),
    path('projects/<int:pk>', staff_views.StaffProjectDetail.as_view(), name='project_detail'),
]