from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'meuprojeto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^exemplo_get', 'petshop.views.exemplo_get',
        name='exemplo_get'),

    url(r'^exemplo_post', 'petshop.views.exemplo_post',
        name='exemplo_post'),
]
