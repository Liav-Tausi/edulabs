
# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Movie(models.Model):
    # names the table = movies -> in the documentation
    class Meta:
        db_table = 'movies'

    # by default places a SERIAL PRIMARY KRY id

    # like postgres VARCHAR(256) NOT NULL
    name = models.CharField(db_column="name", max_length=256, null=False)
    # like postgres VARCHAR
    description = models.TextField(db_column='description', null=True)

    duration_in_min = models.IntegerField(db_column='duration_in_min', null=False)

    release_year = models.SmallIntegerField(
        db_column='year',
        null=False,
        validators=[MinValueValidator(1900), MaxValueValidator(2050)]
    )

    pic_url = models.URLField(db_column='pic_url', max_length=256, null=True)


class Rating(models.Model):

    class Meta:
        db_table = 'ratings'

    movie_id = models.ForeignKey(to=Movie, on_delete=models.RESTRICT)

    rating = models.SmallIntegerField(db_column='rating', null=False, validators=[MinValueValidator(1), MaxValueValidator(11)])

    rating_date = models.DateField(db_column='rating_date', null=False)


class Reviews(models.Model):

    class Meta:
        db_table = 'reviews'

    movie_id = models.ForeignKey(to=Movie, on_delete=models.RESTRICT)

    review = models.TextField(db_column='review', null=False)

    review_date = models.DateField(db_column='rating_date', null=False)