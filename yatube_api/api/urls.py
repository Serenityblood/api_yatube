from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import GroupViewSet, PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>[\w.@+-]+)/comments',
    CommentViewSet,
    basename='comments'
)

app_name = 'api'

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token)
]
