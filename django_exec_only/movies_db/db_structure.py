
# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Rating(models.Model):

    class Meta:
        db_table = 'ratings'

    movie_id = models.ForeignKey(to='Movie', on_delete=models.RESTRICT)

    rating = models.SmallIntegerField(db_column='rating',
                                      null=False,
                                      blank=False,
                                      db_index=True,
                                      validators=[MinValueValidator(1), MaxValueValidator(11)])

    rating_date = models.DateField(db_column='rating_date',
                                   null=False,
                                   blank=False)




class Reviews(models.Model):

    class Meta:
        db_table = 'reviews'

    movie_id = models.ForeignKey(to='Movie', on_delete=models.RESTRICT)

    review = models.TextField(db_column='review', null=False, blank=False)

    review_date = models.DateField(db_column='rating_date', null=False, blank=False)




class Actor(models.Model):

    class Meta:
        db_table = 'actors'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=256, db_column='name', null=False, blank=False)
    birth_year = models.IntegerField(db_column='birth_year', null=False)




class Movie(models.Model):
    # names the table = movies -> in the documentation
    class Meta:
        db_table = 'movies'

    def __str__(self):
        return self.name

    # by default places a SERIAL PRIMARY KRY id

    # like postgres VARCHAR(256) NOT NULL
    name = models.CharField(db_column="name", max_length=256, null=False, blank=False, db_index=True)
    # like postgres VARCHAR
    description = models.TextField(db_column='description', null=True)

    duration_in_min = models.IntegerField(db_column='duration_in_min', null=False, blank=False)

    release_year = models.SmallIntegerField(
        db_column='year',
        null=False,
        blank=False,
        validators=[MinValueValidator(1900), MaxValueValidator(2050)]
    )

    pic_url = models.URLField(db_column='pic_url', max_length=256, null=True)
    actors = models.ManyToManyField(Actor, through='MovieActor')




class MovieActor(models.Model):

    class Meta:
        db_table = 'movie_actors'

    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    salary = models.IntegerField()
    main_role = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return f"{self.actor.name} in movie {self.movie.name}"










