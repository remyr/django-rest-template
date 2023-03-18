from allauth.account.adapter import DefaultAccountAdapter as BaseDefaultAccountAdapter
from allauth.utils import build_absolute_uri
from django.urls import reverse


class DefaultAccountAdapter(BaseDefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        if 'activate_url' in context:
            path = reverse(
                'account_confirm_email_custom',
                args=[context['key']],
            )
            url = build_absolute_uri(None, path)
            context['activate_url'] = url
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
