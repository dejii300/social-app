from django.urls import path
from .views import *

app_name = 'profiles'

urlpatterns = [
    path('', ProfileListView.as_view(), name='all-profiles-view'),
    path('myprofile/', my_profile_view, name='my-profile-view'),
    path('my-invites/', invites_recieved_view, name='my-invites-view'),
    path('to-invite/', invite_profile_list_view, name='invite-profiles-view'),
    path('send-invite/', send_invataion, name='send-invite'),
    path('remove-friend/', remove_from_friends, name='remove-friend'),
    path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),
    path('my-invites/accept/', accept_invatation, name='accept-invite'),
    path('my-invites/reject/', reject_invatation, name='reject-invite'),
]