from django.db import models


# Create your models here.
from django.utils.safestring import mark_safe


class movie_category(models.Model):
    category_name = models.CharField(max_length=30)


class male_actor(models.Model):
    m_name = models.CharField(max_length=30)
    # m_dob = models.IntegerField(max_length=30)
    m_dob = models.DateField(max_length=30)
    m_pic = models.ImageField(upload_to='photos')

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.m_pic.url))

    admin_photo.allow_tags = True

    def __str__(self):
        return self.m_name


class female_actor(models.Model):
    f_name = models.CharField(max_length=30)
    f_dob = models.DateField(max_length=30)
    f_pic = models.ImageField(upload_to='photos')

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.f_pic.url))

    admin_photo.allow_tags = True

    def __str__(self):
        return self.f_name




class movies(models.Model):
    movie_name = models.CharField(max_length=30)
    movie_pic = models.ImageField(upload_to='photos')
    movie_description = models.TextField()
    male_name = models.ForeignKey(male_actor,on_delete=models.CASCADE)
    female_name = models.ForeignKey(female_actor,on_delete=models.CASCADE)
    cat_name =  models.ForeignKey(movie_category,on_delete=models.CASCADE)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.movie_pic.url))

    admin_photo.allow_tags = True

    def __str__(self):
        return self.movie_name

