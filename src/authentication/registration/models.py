from django.conf import settings
from django.core import signing
from django.core.mail import EmailMessage
from django.core.signing import SignatureExpired, BadSignature
from django.template.loader import render_to_string
from django.utils.encoding import force_str

from administration.models import User

EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
SALT = "account"


class EmailConfirmationHMAC:
    def __init__(self, user: User):
        self.user = user

    @property
    def key(self):
        return signing.dumps(obj=self.user.pk, salt=SALT)

    @classmethod
    def from_key(cls, key):
        try:
            max_age = 60 * 60 * 24 * EMAIL_CONFIRMATION_EXPIRE_DAYS
            pk = signing.loads(key, max_age=max_age, salt=SALT)
            ret = EmailConfirmationHMAC(User.objects.get(pk=pk))
        except (SignatureExpired, BadSignature):
            return None
        return ret

    def confirm(self):
        if not self.user.is_email_confirmed:
            self.user.is_email_confirmed = True
            self.user.save()

    def build_absolute_uri(self, request):
        host = request.get_host()
        return f"http://{host}/auth/confirm-email?key={self.key}"

    def send(self, request, signup=True):
        ctx = {
            "user": self.user,
            "activate_url": self.build_absolute_uri(request),
            "key": self.key,
        }
        if signup:
            email_template = "authentication/email/email_confirmation_signup"
        else:
            email_template = "authentication/email/email_confirmation"
        msg = self.render_mail(email_template, self.user.email, ctx, request)
        msg.send()

    @staticmethod
    def render_mail(template_prefix, email, context, request):
        to = [email] if isinstance(email, str) else email
        subject = render_to_string(f"{template_prefix}_subject.html", context)
        # remove superfluous line breaks
        subject = " ".join(subject.splitlines()).strip()
        subject = force_str(subject)
        from_email = settings.DEFAULT_FROM_EMAIL

        template_name = f"{template_prefix}_message.html"
        body = render_to_string(
            template_name,
            context,
            request,
        ).strip()
        msg = EmailMessage(subject, body, from_email, to)
        msg.content_subtype = "html"
        return msg
