from django.db import models
from django.utils.translation import ugettext_lazy as _

class Question(models.Model):
    question_text = models.CharField(_("Question"), max_length=50)
    expire_in = models.DateTimeField(_("Expires"))

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question + ' - ' + self.choice_text
    
