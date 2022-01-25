"""apidemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import S
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI, Schema

from apidemo.visualize import validateData, visualizeData, invalid_data_code

api = NinjaAPI()



@api.post('/visualize', response = {200: SuccessResponse, 400: ResponseMessage, 500:  ResponseMessage})
def visualizePost(request, data: Data = Data(), custom_settings: CustomSettings = CustomSettings()):
    try:
        validation_result = validateData(data)
        if validation_result != 0:
            return 400, {'status': 400, 'message': invalid_data_code[validation_result]}
        else:
            payload = visualizeData(data, custom_settings)
        return 200, {'status': 200, 'message': 'OK', 'payload': payload}
    except Exception as e:
        return 500, {'status': 500, 'message': 'An unexpected error has occured. Error: ' + str(e)}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
