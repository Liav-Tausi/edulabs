import datetime
import os

os.environ["DJANGO_SETTINGS_MODULE"] = "employees.settings"

import django

django.setup()

from employees_app.models import *
import csv
from datetime import datetime, timedelta


def data_to_person(file_path: str, delimiter=',') -> None:
    with open(file=f"{file_path}", mode='r', encoding='utf-8') as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        for row in reader:
            new_person = Person(first_name=row['first_name'],
                                last_name=row['last_name'],
                                personal_email=row['personal_email'],
                                gender=row['gender'],
                                birth_date=datetime.strptime(row['birth_date'], "%m/%d/%Y")
                                )
            new_person.save()


def data_to_company(file_path: str, delimiter=',') -> None:
    with open(file=f"{file_path}", mode='r', encoding='utf-8') as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        for row in reader:
            new_company = Company(company_name=row['company_name'],
                                  country=row['country'],
                                  city=row['city'],
                                  address=row['address'],
                                  phone_num=row['phone_num'],
                                  )
            new_company.save()


def data_to_employees(file_path: str, delimiter=',') -> None:
    with open(file=f"{file_path}", mode='r', encoding='utf-8') as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        for row in reader:
            new_employee = Employee(person_id=Person.objects.get(id=int(row['person_id'])),
                                    company_id=Company.objects.get(id=int(row['company_id'])),
                                    job_title=row['job_title'],
                                    is_current_job=row['is_current_job'].capitalize(),
                                    company_email=row['company_email']
                                    )
            new_employee.save()


def get_person_name_by_id(person_id: int) -> str:
    """
    Given person id, return string that represents person full name
    :param person_id:
    :return:
    """
    person_id = Person.objects.get(id=person_id)
    return person_id


def get_people_by_age(age: int) -> list[Person]:
    """
   Given age in years, return list of persons of this age
   :param age:
   :return:
   """
    return Person.objects.filter(
        birth_date__year=(datetime.now() - timedelta(days=age * 365)).strftime("%m/%d/%Y").split('/')[2])


def get_people_cnt_by_gender(_gender: str) -> list[Person]:
    """
   Given the gender, return list of people of this gender
   :param _gender:
   :return:
   """
    gender = Person.objects.filter(gender=_gender.lower().capitalize())
    return gender


def get_companies_by_country(_country: str) -> list[str]:
    """
   Given country name, return list of companies' names in this country
   :param country:
   :return:
   """
    country = Company.objects.filter(country=_country.lower())
    return country


def get_company_employees(company_id: int, current_only: bool = None) -> list[Person]:
    """
   Given company id, return list of persons whi work(ed) for this company
   :param company_id:
   :param current_only: if True, return only people who are currently work in the company
   :return:
   """
    if current_only:
        employees = Employee.objects.filter(company=company_id, is_current_job=True)
    else:
        employees = Employee.objects.filter(company=company_id)

    return [employee.person for employee in employees]


def get_person_jobs(person_id: int) -> list[dict[str, str]]:
    """
   Given person_id, return list of dictionaries that map from company name to job title
   :param person_id:
   :return:
   """
    jobs: list = list()
    employees = Employee.objects.filter(person=person_id)
    for employee in employees:
        jobs.append({'company_name': employee.company.company_name, 'job_title': employee.job_title})
    return jobs


if __name__ == '__main__':
    # print(get_person_name_by_id(3))
    # print(get_people_by_age(34))
    # print(get_company_employees(3))
    print(get_person_jobs(3))