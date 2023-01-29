
from django.db import models


# Create your models here.
class Person(models.Model):
    class Meta:
        db_table = 'person'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    first_name = models.CharField(db_column='first_name', max_length=128, null=False)
    last_name = models.CharField(db_column='last_name', max_length=128, null=False)
    personal_email = models.EmailField(db_column='personal_email', max_length=256, null=False)
    M = 'M'
    F = 'F'
    GENDER_CHOICES = (
        (M, 'Male'),
        (F, 'Female')
    )
    gender = models.CharField(db_column='gender', choices=GENDER_CHOICES, max_length=128 , null=False)
    birth_date = models.DateField(db_column='birth_date', null=False)



class Company(models.Model):
    class Meta:
        db_table = 'companies'

    def __str__(self):
        return self.company_name

    company_name = models.CharField(db_column='company_name', max_length=128, null=False)
    country = models.CharField(db_column='country', max_length=128, null=False)
    city = models.CharField(db_column='city', max_length=128, null=False)
    address = models.CharField(db_column='address', max_length=256, null=False)
    phone_num = models.CharField(db_column='phone_num', max_length=36, null=False)
    employees = models.ManyToManyField(Person, through='Employee')



class Employee(models.Model):
    class Meta:
        db_table = 'employees'

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title = models.CharField(db_column='job_title', max_length=128, null=False)
    is_current_job = models.BooleanField(db_column='is_current_job', null=False)
    company_email = models.EmailField(db_column='company_email', max_length=128, null=False)




