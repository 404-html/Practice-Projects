from django.db import models

#This is the questions model for PollsApp
class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text

#This is the Choice model for PollsApp
class Choice(models.Model):
	quesion = models.ForeignKey(Question, on_delete = models.CASCADE)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)
	def __str__(self):
		return self.choice_text
