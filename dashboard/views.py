from django.shortcuts import render

# Create your views here.
app_name = "dashboard"
app_path = "dashboard/patient/"


def home(request):
    return render(request, f"{app_path}dashboard.html", locals())
