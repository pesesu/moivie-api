from account.models import EmailVerification, User


class EmailVerificationHelper:
    @staticmethod
    def save_token(email: str, token:str):
        user_instance = EmailVerification.objects.filter(email=email)
        if user_instance.exists():
            user = user_instance.first()
            user.token = token
            user.save()
        else:
            EmailVerification.objects.create(email=email, token=token)

    @staticmethod
    def verify_email(email:str, token:str):
        user_instance = EmailVerification.objects.filter(email=email, token=token)
        if user_instance.exists():
            user = user.objects.get(email=email)
            user.is_active = True
            user.save()
            return True
        else:
            return False