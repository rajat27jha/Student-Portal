from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, CreateView

from college.forms import StudentForm
from college.models import Notice, Branch, Assignment, Result, Attendance, Student, Feedback


def home(request):
    return render(request, "home.html")


def chkstu(request):
    name2 = request.GET.get("name")
    if name2 == None or name2 == "":
        return render(request, 'chkstu.html', {"err2":""})
    else:
        st = Student.objects.filter(name=name2)
        if len(st)>0:
            return render(request, 'chkstu.html', {"err2": "Username already taken. Pick another ;)"})
        else:
            return render(request, 'chkstu.html', {"err2": ""})


@method_decorator(login_required, name='dispatch')
class NoticeList(ListView):
    model = Notice

    def get_queryset(self):
        si = self.request.GET.get('si')
        if si == None:
            si = ''
        if self.request.user.is_superuser:
            return Notice.objects.all().filter(subject__icontains=si).order_by('-id')
        else:
            bid = Branch.objects.all().filter(name='All')[0].id
            st = Student.objects.filter(user=self.request.user.id)[0]
            return Notice.objects.all().filter(branch__in=(st.branch.id, bid), sem__in=(st.sem, 0),
                                               subject__icontains=si).order_by('-id')

    paginate_by = 5


@method_decorator(login_required, name='dispatch')
class NoticeDetail(DetailView):
    model = Notice


@method_decorator(login_required, name='dispatch')
class ResultList(ListView):
    model = Result

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Result.objects.all().filter().order_by('-id')
        else:
            st = Student.objects.filter(user=self.request.user.id)[0]
            return Result.objects.all().filter(student_id=st.id).order_by('-id')

    paginate_by = 5


@method_decorator(login_required, name='dispatch')
class ResultDetail(DetailView):
    model = Result


@method_decorator(login_required, name='dispatch')
class AttendanceList(ListView):
    model = Attendance

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Attendance.objects.all().filter().order_by('-id')
        else:
            st = Student.objects.filter(user=self.request.user.id)[0]
            return Attendance.objects.all().filter(student_id=st.id).order_by('-id')

    paginate_by = 5


@method_decorator(login_required, name='dispatch')
class AttendanceDetail(DetailView):
    model = Attendance


@method_decorator(login_required, name='dispatch')
class AssignmentList(ListView):
    model = Assignment

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Assignment.objects.all().filter().order_by('-id')
        else:
            bid = Branch.objects.all().filter(name='All')[0].id
            st = Student.objects.filter(user=self.request.user.id)[0]
            return Assignment.objects.all().filter(branch__in=(st.branch.id, bid), sem__in=(st.sem, 0)).order_by('-id')

    paginate_by = 5


@method_decorator(login_required, name='dispatch')
class AssignmentDetail(DetailView):
    model = Assignment


@method_decorator(login_required, name='dispatch')
class MyList(TemplateView):
    template_name = "student.html"

    def get_context_data(self, **kwargs):
        st = None
        if not self.request.user.is_superuser:
            st = Student.objects.filter(user=self.request.user.id)[0]
        context = TemplateView.get_context_data(self, **kwargs)
        if st == None:
            context["notices"] = Notice.objects.all().order_by('-id')[:5]
            context["assignments"] = Assignment.objects.all().order_by('-id')[:5]
            context["results"] = Result.objects.all().order_by('-id')[:5]
            context["attendances"] = Attendance.objects.all().order_by('-id')[:5]
        else:
            bid = Branch.objects.all().filter(name='All')[0].id
            notices = Notice.objects.all().filter(branch__in=(st.branch.id, bid), sem__in=(st.sem, 0)).order_by('-id')[
                      :5]
            # or operator sample #    notices = Notice.objects.all().filter(Q(branch=st.branch.id, sem =st.sem) |
            #  Q (branch=st.branch.id, sem =0)).order_by('-id')[:5]
            assigns = Assignment.objects.all().filter(branch__in=(st.branch.id, bid), sem__in=(st.sem, 0)).order_by('-id')[
                      :5]
            res = Result.objects.all().filter(student_id=st.id).order_by('-id')[:5]
            ats = Attendance.objects.all().filter(student_id=st.id).order_by('-id')[:5]
            context["notices"] = notices
            context["assignments"] = assigns
            context["results"] = res
            context["attendances"] = ats
        return context


@method_decorator(login_required, name='dispatch')
class StudentUpdate(UpdateView):
    #     fields=["branch", "sem"]
    form_class = StudentForm
    model = Student
    success_url = reverse_lazy('student')


class FeedCreate(CreateView):
    success_url = reverse_lazy('subFeed')
    model = Feedback
    fields = ['name', 'email', 'mobno', 'subject', 'message']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FeedCreate, self).form_valid(form)


def SubmitFeedback(request):
    return render(request, "submit_feedback.html")
