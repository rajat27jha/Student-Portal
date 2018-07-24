from django.contrib import admin

# Register your models here.
from college.models import Branch, Student, Notice, Assignment, Result, Attendance, Feedback

admin.site.register(Branch)


class NoticeAdmin(admin.ModelAdmin):
    list_filter = ['branch', 'cr_date']
    list_display = ['subject', 'branch', 'cr_date']
    search_fields = ['message', 'subject']


admin.site.register(Notice, NoticeAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_filter = ['branch', 'sem', 'skills']
    list_display = ['name', 'branch', 'sem', 'phone_no']
    search_fields = ['name', 'branch', 'rn']


admin.site.register(Student, StudentAdmin)


class AssignmentAdmin(admin.ModelAdmin):
    list_filter = ['branch', 'cr_date', 'duedate']
    list_display = ['subject', 'branch', 'cr_date', 'duedate']
    search_fields = ['subject', 'message']


admin.site.register(Assignment, AssignmentAdmin)


class ResultAdmin(admin.ModelAdmin):
    list_filter = ['subject', 'marks']
    list_display = ['subject', 'student', 'marks']
    search_fields = ['subject', 'student']


admin.site.register(Result, ResultAdmin)


class AttendanceAdmin(admin.ModelAdmin):
    list_filter = ['subject', 'attend']
    list_display = ['subject', 'student', 'total_classes', 'attend']
    search_fields = ['subject', 'student']


admin.site.register(Attendance, AttendanceAdmin)


class Feedbackadmin(admin.ModelAdmin):
    list_display = ["name", "subject", "message", "user"]
    list_filter = ["name", "user", "subject"]


admin.site.register(Feedback, Feedbackadmin)
