from django.shortcuts import render


def index(request):
    return render(request, 'Dashboard/index.html')

def CoordinatorDashboard(request):
    return render(request, 'Dashboard/coordinator-dashboard.html')