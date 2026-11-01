from django.contrib import admin
from django.urls import path, include

from studentorg import views
from studentorg.views import (
    HomePageView,
    OrganizationList,
    OrganizationCreateView,
    OrganizationUpdateView,
    OrganizationDeleteView,
    ProgramList,
    ProgramCreateView,
    ProgramUpdateView,
    ProgramDeleteView,
    StudentList,    
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    CollegeList,
    CollegeCreateView,
    CollegeUpdateView,
    CollegeDeleteView,
    OrgMemberList,
    OrgMemberCreateView,
    OrgMemberUpdateView,
    OrgMemberDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")), # allauth routes
    path('', HomePageView.as_view(), name='home'),

    # Organization
    path(
        'organization_list',
        OrganizationList.as_view(),
        name='organization-list'
    ),

    path(
        'organization_list/add',
        OrganizationCreateView.as_view(),
        name='organization-add'
    ),

    path(
        'organization_list/<pk>',
        OrganizationUpdateView.as_view(),
        name='organization-update'
    ),

    path(
        'organization_list/<pk>/delete',
        OrganizationDeleteView.as_view(),
        name='organization-delete'
    ),

    # Program
    path(
        'program_list',
        ProgramList.as_view(),
        name='program-list'
    ),

    path(
        'program_list/add',
        ProgramCreateView.as_view(),
        name='program-add'
    ),

    path(
        'program_list/<pk>',
        ProgramUpdateView.as_view(),
        name='program-update'
    ),

    path(
        'program_list/<pk>/delete',
        ProgramDeleteView.as_view(),
        name='program-delete'
    ),

    # Students
    path(
        'student_list',
        StudentList.as_view(),
        name='student-list'
    ),

    path(
        'student_list/add',
        StudentCreateView.as_view(),
        name='student-add'
    ),

    path(
        'student_list/<pk>',
        StudentUpdateView.as_view(),
        name='student-update'
    ),

    path(
        'student_list/<pk>/delete',
        StudentDeleteView.as_view(),
        name='student-delete'
    ),

    path(
        'college_list',
        views.CollegeList.as_view(),
        name='college-list'
    ),

    path(
        'college_list/add',
        views.CollegeCreateView.as_view(),
        name='college-add'
    ),

    path(
        'college_list/<pk>',
        views.CollegeUpdateView.as_view(),
        name='college-update'
    ),

    path(
        'college_list/<pk>/delete',
        views.CollegeDeleteView.as_view(),
        name='college-delete'
    ),

    path(
        'orgmem_list',
        views.OrgMemberList.as_view(),
        name='orgmem-list'
    ),

    path(
        'orgmem_list/add',
        views.OrgMemberCreateView.as_view(),
        name='orgmem-add'
    ),

    path(
        'orgmem_list/<pk>',
        views.OrgMemberUpdateView.as_view(),
        name='orgmem-update'
    ),

    path(
        'orgmem_list/<pk>/delete',
        views.OrgMemberDeleteView.as_view(),
        name='orgmem-delete'
    ),

]