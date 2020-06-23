from rest_framework import viewsets
from .models import Team, NameTeamMembers
from .serializers import TeamSerializer, NameTeamMembersSerializer


class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = ('teamID')


class NameTeamMembersView(viewsets.ModelViewSet):
    queryset = NameTeamMembers.objects.all()
    serializer_class = NameTeamMembersSerializer
