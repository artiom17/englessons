from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('grammar/', include('grammar.urls')),
    path('topic/', include('topic.urls')),
    path('testmain/', include('testmain.urls')),
    path('lessons/', include('lessons.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('english.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
