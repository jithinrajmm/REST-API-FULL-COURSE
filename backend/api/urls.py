from django.urls import path
from api import views


urlpatterns = [
    path('',views.home,name='home'), # localhost:8000/api/,
    path('products/',views.models_data_get,name='model_data'),
    # rest view
    path('rest_fun/',views.rest_view,name='rest_fun'),
]