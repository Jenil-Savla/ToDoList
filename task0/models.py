from django.db import models

class User(models.Model):
	name = models.CharField(max_length= 20,default='admin')
	
	def __str__(self):
		return self.name

class Task(models.Model):
    number = models.IntegerField(default =0)
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank=True)

    def __str__(self):
        return (f"({self.number}) {self.title} by :({self.user})")
        