from core.models import User, Campaing


class Tools:
    """manage tools for payment modules"""

    def __init__(self):
        pass

    def validate_user(self, c_user):
        try:

            if not c_user:
                msg = 'user required'
                return msg

            user = User.objects.get(id=c_user)
            return user

        except User.DoesNotExist as err:
            return err

    def validate_campaing(self, c_camp):
        try:

            if not c_camp:
                msg = 'campaing required'
                return msg

            campaing = Campaing.objects.get(id=c_camp)
            return campaing

        except Campaing.DoesNotExist as err:
            return err
