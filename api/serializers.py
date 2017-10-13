from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from gecoa.models import Experience
from gecoa.models import Province

from rest_framework import serializers


class ProvinceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(lookup_field='slug', view_name='province-detail')

    class Meta:
        model = Province
        fields = ('url', 'name')


class ExperienceListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(lookup_field='slug', view_name='experience-detail')

    class Meta:
        model = Experience
        fields = ('url', 'name',)


class ProvincesExperienceListSerializer(serializers.HyperlinkedModelSerializer):
    experiences = ExperienceListSerializer(many=True)
    url = serializers.HyperlinkedIdentityField(lookup_field='slug', view_name='province-detail')

    class Meta:
        model = Province
        fields = ('url', 'name', 'experiences')
