# -*- coding: utf-8 -*-

from __future__ import print_function

from __future__ import unicode_literals

from django.db import models

from django.utils import timezone
import datetime


# Create your models here.

##class Pregunta (models.Model):
##    asunto = models.CharField(max_length = 200)
##    descripcion = models.TextField()
##    fecha_publicacion = models.DataTimeField(auto_now_add=True)
##
##class Respuesta (models.Model):
##    Pregunta = models. ForeingKey(Pregunta)
##    contenido = models.TextField()
##    mejor_respuesta = models.BooleanFiel("Su respuesta de prueba")


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__ (self):              # __unicode__ on Python 3
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__ (self):              # __str__ on Python 3
        return self.choice_text
