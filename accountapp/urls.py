from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    #as_view()를 적어줘야 함수형 헬로월드처럼 반응함.
    path('create/', AccountCreateView.as_view(), name='create'),
]
