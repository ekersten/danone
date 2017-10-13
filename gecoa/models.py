from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.
class Period(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Province(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Department(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    province = models.ForeignKey(Province, related_name='departments')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('province', 'slug')


class Property(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Attachment(TimeStampedModel):
    name = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to='attachments', blank=True, null=True)

    def __str__(self):
        return self.name


class Photo(TimeStampedModel):
    image = models.ImageField(upload_to='photos')
    text = models.TextField(blank=True, null=True)


class TechnologyType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Technology(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    learnings = models.TextField(blank=True, null=True)
    materials = models.TextField(blank=True, null=True)
    maintenance = models.TextField(blank=True, null=True)
    reviser = models.CharField(max_length=200, blank=True, null=True)
    types = models.ManyToManyField(TechnologyType, blank=True, null=True)
    photos = models.ManyToManyField(Photo, blank=True, null=True)

    def __str__(self):
        return self.name


class OrganizationType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Organization(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    contact = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    type = models.ForeignKey(OrganizationType, related_name='organizations')

    def __str__(self):
        return self.name


class ExperienceType(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Experience(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    problem = models.TextField(blank=True, null=True)
    porocess = models.TextField(blank=True, null=True)
    learnings = models.TextField(blank=True, null=True)
    methodology = models.TextField(blank=True, null=True)
    province = models.ForeignKey(Province, related_name='experiences')
    attachments = models.ManyToManyField(Attachment, blank=True, null=True)
    types = models.ManyToManyField(ExperienceType, blank=True, null=True)
    organizations = models.ManyToManyField(Organization, through='ExperienceOrganization')
    photos = models.ManyToManyField(Photo, blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True, null=True)

    def __str__(self):
        return self.name


class ExperienceOrganization(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    is_lead = models.BooleanField(default=False)


class Regulation(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    schema = models.TextField(blank=True, null=True)
    organizations_list = models.TextField(blank=True, null=True)
    providers = models.TextField(blank=True, null=True)
    legal_authorizations = models.TextField(blank=True, null=True)
    water_access = models.TextField(blank=True, null=True)
    province = models.ForeignKey(Province, related_name='regulations')
    reviser = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class ToolType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tool(TimeStampedModel):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    download = models.FileField(upload_to='tools', blank=True, null=True)
    tags = models.TextField(blank=True, null=True, help_text='Separated by comas (,)')
    type = models.ForeignKey(ToolType)

    def __str__(self):
        return self.name
