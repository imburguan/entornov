# -*- coding: utf-8 -*-

from __future__ import print_function

from __future__ import unicode_literals

from django.db import models

from django.utils import timezone
import datetime





class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__ (self):              # __unicode__ on Python 3
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    #def primary_key(self):
        #return self.id

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'



class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__ (self):              # __str__ on Python 3
        return self.choice_text


class Faixas(models.Model):
    faixa_text = models.CharField(max_length=200)
    print ("Hola hola hola")

    def __unicode__ (self):              # __str__ on Python 3
        return self.faixas_text


#
# class Pessoas(models.Model):
#     nome = models.CharField(max_length=200)
#     id_faixa = models.ForeignKey(Faixas)
#
#     def __unicode__ (self):              # __str__ on Python 3
#         return self.nome
