from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CourseMaster(models.Model):
    course_name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)
    genre = models.CharField(max_length=255, blank=False)
    icon = models.BinaryField(blank=True, null=True)
    
    def __str__(self):
        return self.course_name

    class Meta:
        db_table = 'course_master'

class Reserver(models.Model):
    reserver_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    tel = PhoneNumberField()
    reservation_date = models.DateTimeField(blank=False)
    course = models.ForeignKey(CourseMaster, to_field='id', on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.reservation_date)

    class Meta:
        db_table = 'reserver'
