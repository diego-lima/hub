from django.conf.urls import include, url
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^$', pagina_inicial_view,name="pagina_inicial_view"),
    url(r'^admin/', admin.site.urls),
    #Experimentos webdesign
    url(r'^experimentos_webdesign/$', experimentos_view, name="experimentos_view"),
    #Apps python
    url(r'^apps_python/$', apps_view, name="apps_view"),
    url(r'^apps_python/torre_de_hanoi/', include('torre_de_hanoi.urls', namespace='torre_de_hanoi')),
    url(r'^apps_python/smartZeus/', include('smartZeus.urls', namespace='smartZeus'))
]
