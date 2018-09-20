from .models import Account
from rest_framework import generics
from .serializers import AccountSerializer

class AccountMixin:
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
 
 
class AccountList(AccountMixin, generics.ListCreateAPIView):
    """
    Returns list of all Users or create a new User
    """
    # def update_profile(request, user_id):
    #     user = User.objects.get(pk=user_id)
    #     user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    #     user.save()
    # pass
 
 
class AccountDetails(AccountMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a specific User, updates it or deletes it.
    """
    pass