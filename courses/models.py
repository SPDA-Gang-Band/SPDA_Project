from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CourseRequest(models.Model):
    surname = models.CharField(_('surname'), max_length=256)
    name = models.CharField(_('name'), max_length=256)
    course_name = models.CharField(_('course name'), max_length=256)
    link = models.CharField(_('link'), max_length=512)
    price = models.CharField(_('price'), max_length=256, blank=True)
    start_date = models.CharField(_('start date'), max_length=256, blank=True)
    study_quarter = models.IntegerField(_('study quarter'), default=1)
    description = models.TextField(_('description'), blank=True)
    status = models.CharField(_('status'), max_length=256, default='Ждёт одобрения')
