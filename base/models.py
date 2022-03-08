from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Customuser(AbstractUser):
    phone = PhoneNumberField(unique=True, blank=True, null=True)


class Artist(models.Model):
    artist_name = models.CharField(max_length=150, blank=True, null=True)
    artist_country = models.CharField(max_length=150, blank=True, null=True)
    artist_image = models.ImageField(null=True, blank=True)
    artistry = RichTextField(blank=True, null=True)
    education = RichTextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.artist_name


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Medium(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    rating = models.DecimalField(max_digits=5, default=0, decimal_places=1)

    def __str__(self):
        return str(self.rating)


class Painting(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    main_image = models.ImageField(null=True, blank=True)
    wall_image = models.ImageField(null=True, blank=True)
    artist = models.ForeignKey(
        Artist, related_name='artist', on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.CASCADE)
    introduction = RichTextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    shipping = RichTextField(blank=True, null=True)
    like = models.IntegerField(null=True, blank=True, default=0)
    views = models.IntegerField(null=True, blank=True)
    is_feature = models.BooleanField(null=True, blank=True, default=False)
    is_popular = models.BooleanField(null=True, blank=True, default=False)
    is_new = models.BooleanField(null=True, blank=True, default=False)
    is_sale = models.BooleanField(null=True, blank=True, default=False)
    sale_percentage = models.IntegerField(null=True, blank=True)
    style = models.ManyToManyField(Style,  blank=True)
    subject = models.ManyToManyField(Subject,  blank=True)
    medium = models.ManyToManyField(Medium,  blank=True)
    material = RichTextField(max_length=150, blank=True, null=True)
    specification = RichTextField(max_length=150, blank=True, null=True)
    size = RichTextField(max_length=150, blank=True, null=True)
    orientation = models.CharField(max_length=150, blank=True, null=True)
    color = RichTextField(max_length=150, blank=True, null=True)
    created_year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    rating = models.ForeignKey(
        Review, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Photography(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    main_image = models.ImageField(null=True, blank=True)
    wall_image = models.ImageField(null=True, blank=True)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.CASCADE)
    introduction = models.TextField(max_length=150, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    shipping = models.CharField(max_length=150, blank=True, null=True)
    like = models.IntegerField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    is_feature = models.BooleanField(null=True, blank=True, default=False)
    is_popular = models.BooleanField(null=True, blank=True, default=False)
    is_new = models.BooleanField(null=True, blank=True, default=False)
    is_sale = models.BooleanField(null=True, blank=True, default=False)
    sale_percentage = models.IntegerField(null=True, blank=True)
    style = models.ManyToManyField(Style)
    subject = models.ManyToManyField(Subject)
    medium = models.ManyToManyField(Medium)
    material = models.TextField(max_length=150, blank=True, null=True)
    size = models.TextField(max_length=150, blank=True, null=True)
    orientation = models.TextField(max_length=150, blank=True, null=True)
    color = models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Drawing(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    main_image = models.ImageField(null=True, blank=True)
    wall_image = models.ImageField(null=True, blank=True)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.CASCADE)
    introduction = models.TextField(max_length=150, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    shipping = models.CharField(max_length=150, blank=True, null=True)
    like = models.IntegerField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    is_feature = models.BooleanField(null=True, blank=True, default=False)
    is_popular = models.BooleanField(null=True, blank=True, default=False)
    is_new = models.BooleanField(null=True, blank=True, default=False)
    is_sale = models.BooleanField(null=True, blank=True, default=False)
    sale_percentage = models.IntegerField(null=True, blank=True)
    style = models.ManyToManyField(Style)
    subject = models.ManyToManyField(Subject)
    medium = models.ManyToManyField(Medium)
    material = models.TextField(max_length=150, blank=True, null=True)
    size = models.TextField(max_length=150, blank=True, null=True)
    orientation = models.TextField(max_length=150, blank=True, null=True)
    color = models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Sculpture(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    main_image = models.ImageField(null=True, blank=True)
    wall_image = models.ImageField(null=True, blank=True)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.CASCADE)
    introduction = models.TextField(max_length=150, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    shipping = models.CharField(max_length=150, blank=True, null=True)
    like = models.IntegerField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    is_feature = models.BooleanField(null=True, blank=True, default=False)
    is_popular = models.BooleanField(null=True, blank=True, default=False)
    is_new = models.BooleanField(null=True, blank=True, default=False)
    is_sale = models.BooleanField(null=True, blank=True, default=False)
    sale_percentage = models.IntegerField(null=True, blank=True)
    style = models.ManyToManyField(Style)
    subject = models.ManyToManyField(Subject)
    medium = models.ManyToManyField(Medium)
    material = models.TextField(max_length=150, blank=True, null=True)
    size = models.TextField(max_length=150, blank=True, null=True)
    orientation = models.TextField(max_length=150, blank=True, null=True)
    color = models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Prints(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    main_image = models.ImageField(null=True, blank=True)
    wall_image = models.ImageField(null=True, blank=True)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.CASCADE)
    introduction = models.TextField(max_length=150, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    shipping = models.CharField(max_length=150, blank=True, null=True)
    like = models.IntegerField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    is_feature = models.BooleanField(null=True, blank=True, default=False)
    is_popular = models.BooleanField(null=True, blank=True, default=False)
    is_new = models.BooleanField(null=True, blank=True, default=False)
    is_sale = models.BooleanField(null=True, blank=True, default=False)
    sale_percentage = models.IntegerField(null=True, blank=True)
    style = models.ManyToManyField(Style)
    subject = models.ManyToManyField(Subject)
    medium = models.ManyToManyField(Medium)
    material = models.TextField(max_length=150, blank=True, null=True)
    size = models.TextField(max_length=150, blank=True, null=True)
    orientation = models.TextField(max_length=150, blank=True, null=True)
    color = models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return str(self.name)
