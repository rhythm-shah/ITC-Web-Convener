from rest_framework import serializers
from .models import Team, NameTeamMembers


class NameTeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameTeamMembers
        fields = ('nameTeamMembers', 'team')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('url', 'teamName', 'teamID')
        lookup_field = 'teamID'
        extra_kwargs = {
            'url': {'lookup_field': 'teamID'}
        }


'''
class TeamSerializer(serializers.HyperlinkedModelSerializer):
    nameTeamMembers = NameTeamMembersSerializer.Meta.fields

    class Meta:
        model = Team
        fields = ('url', 'teamName', 'teamID', 'nameTeamMembers')
        lookup_field = 'teamID'
        extra_kwargs = {
            'url': {'lookup_field': 'teamID'}
        }
'''
