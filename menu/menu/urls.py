from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('about/team/', TemplateView.as_view(template_name='about_team.html'), name='about_team'),
    path('about/history/', TemplateView.as_view(template_name='about_history.html'), name='about_history'),
    path('contacts/', TemplateView.as_view(template_name='contacts.html'), name='contacts'),
    path('policy/', TemplateView.as_view(template_name='policy.html'), name='policy'),
    path('terms/', TemplateView.as_view(template_name='terms.html'), name='terms'),
    path('jobs/', TemplateView.as_view(template_name='jobs.html'), name='jobs'),
    path('jobs/it/', TemplateView.as_view(template_name='jobs_it.html'), name='jobs_it'),
    path('jobs/office/', TemplateView.as_view(template_name='jobs_office.html'), name='jobs_office'),
]