from django.contrib import admin

from .models import movie_category
from .models import male_actor
from .models import female_actor
from .models import movies


# Register your models here.

class showmovie_cat(admin.ModelAdmin):
    list_display = ('id', 'category_name')


class showM_actor(admin.ModelAdmin):
    list_display = ('id', 'm_name', 'm_dob', 'admin_photo')


class showF_actor(admin.ModelAdmin):
    list_display = ('id', 'f_name', 'f_dob', 'admin_photo')


class showMovies(admin.ModelAdmin):
    list_display = ('id', 'movie_name', 'admin_photo', 'movie_description', 'male_name', 'female_name', 'cat_name')


admin.site.register(movie_category, showmovie_cat)
admin.site.register(male_actor, showM_actor)
admin.site.register(female_actor, showF_actor)
admin.site.register(movies, showMovies)
