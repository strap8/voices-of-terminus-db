from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.conf import settings
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from django.contrib.auth.models import update_last_login


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)
        token, created = Token.objects.get_or_create(user=user)

        groups = Group.objects.all()
        guildMember = user.is_recruit or user.is_junior_member or user.is_officer or user.is_senior_member or user.is_general_officer or user.is_council or user.is_advisor or user.is_leader

        defaultGroup = Group.objects.get(name='Default')
        defaultGroup.user_set.add(user)

        if(guildMember):
            guildMemberGroup = Group.objects.get(name="Guild Member")
            guildMemberGroup.user_set.add(user)

        return Response({
            'token': token.key,
            'id': user.pk,
            'profile_image': user.profile_image,
            # 'profile_image': request.build_absolute_uri(user.profile_image.url),
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'bio': user.bio,
            'is_active': user.is_active,
            'last_login': user.last_login,
            'opt_in': user.opt_in,
            'lfg': user.lfg,

            'is_superuser': user.is_superuser,
            'is_staff': user.is_staff,
            'is_moderator': user.is_moderator,
            'is_leader': user.is_leader,
            'is_advisor': user.is_advisor,
            'is_council': user.is_council,
            'is_general_officer': user.is_general_officer,
            'is_officer': user.is_officer,
            'is_senior_member': user.is_senior_member,
            'is_junior_member': user.is_junior_member,
            'is_recruit': user.is_recruit,

            'is_raid_leader': user.is_raid_leader,
            'is_banker': user.is_banker,
            'is_recruiter': user.is_recruiter,
            'is_class_lead': user.is_class_lead,
            'is_crafter_lead': user.is_crafter_lead,
            'is_host': user.is_host,
            'is_lore_master': user.is_lore_master,

            'date_joined': user.date_joined,
            'discord_url': user.discord_url,
            'twitter_url': user.twitter_url,
            'twitch_url': user.twitch_url,
            'youtube_url': user.youtube_url,
            'experience_points': user.experience_points,
            'guild_points': user.guild_points
        })


# class TokenAuthenticationView(ObtainAuthToken):
#     """Implementation of ObtainAuthToken with last_login update"""

#     def post(self, request):
#         result = super(TokenAuthenticationView, self).post(request)
#         try:
#             request_user, data = requests.get_parameters(request)
#             user = requests.get_user_by_username(data['username'])
#             update_last_login(None, user)
#         except Exception as exc:
#             return None
#         return result
