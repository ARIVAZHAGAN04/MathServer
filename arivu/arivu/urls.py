from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
path('admin/', admin.site.urls),
path('areaofrectangle/',views.surfacerightcylarea,name="surfaceareaofrightcylinder"),
path('',views.surfacerightcylarea,name="surfaceareaofrightanglecylinder")
     ]
