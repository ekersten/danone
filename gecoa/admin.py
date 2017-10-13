from django.contrib import admin

from .models import Period
from .models import Province
from .models import Department
from .models import Property

from .models import Attachment
from .models import Photo

from .models import TechnologyType
from .models import Technology

from .models import OrganizationType
from .models import Organization

from .models import ExperienceType
from .models import Experience

from .models import Regulation

from .models import ToolType
from .models import Tool



# Register your models here.
admin.site.register(Period)
admin.site.register(Province)
admin.site.register(Department)
admin.site.register(Property)

admin.site.register(Attachment)
admin.site.register(Photo)

admin.site.register(TechnologyType)
admin.site.register(Technology)

admin.site.register(OrganizationType)
admin.site.register(Organization)

admin.site.register(ExperienceType)
admin.site.register(Experience)

admin.site.register(Regulation)

admin.site.register(ToolType)
admin.site.register(Tool)