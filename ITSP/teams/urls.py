from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teams', views.TeamView)
router.register('members', views.NameTeamMembersView)

urlpatterns = [
    path('', include(router.urls)),
]
