from django.contrib.auth import user_logged_in
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from college.models import Student, Branch

# this will called when a new user is created
from college.myctxproc import set_st


@receiver(post_save, sender=User)  # its the receiver
def save_profile(sender, instance, created, **kwargs):
    if created:
        br = Branch.objects.filter(name='All')[0]  # for default value of branch when new user is created
        Student.objects.create(user=instance, name=instance.username, branch=br)
# post_save is sent before or after a model’s save() method is called
# user is a model of diff module
# set value of sender equals user
# if the value of created is True
# then add a new row in student table taking his name and userid


# this signal will be received whenever a user loggs in
# @receiver(user_logged_in)
# def get_stu_details(sender, user, request, **kwargs):
#     if user.is_staff:
#         st = None
#     else:
#         st = Student.objects.filter(user=request.user.id)[0]
#     set_st(st)
#     # will make a new student profile