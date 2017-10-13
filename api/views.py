from rest_framework.viewsets import ModelViewSet

from gecoa.models import Province
from gecoa.models import Experience

from .serializers import ExperienceListSerializer
from .serializers import ProvincesExperienceListSerializer
from .serializers import ProvinceSerializer



class ProvinceViewSet(ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    lookup_field = 'slug'


# Create your views here.
class ExperienceViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceListSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        if self.action == 'list':
            return Province.objects.all()
        else:
            return Experience.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProvincesExperienceListSerializer
        else:
            return ExperienceListSerializer
