import json
from django.forms import widgets
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.conf import settings


GLOBAL_OPTIONS = getattr(settings, 'REDACTORJS_OPTIONS', {})

INIT_JS = """
<script type="text/javascript">
$(function()
{{
    $("#{id}").redactor(
        {options}
    );
}});
</script>
"""


class RedactorjsTextarea(widgets.Textarea):

    class Media:
        js = [
            'http://code.jquery.com/jquery-latest.min.js',
            'redactor/redactor.min.js',
        ]
        css = {
            'all': ('redactor/redactor.css',)
        }

    def __init__(self, *args, **kwargs):
        self.custom_options = kwargs.pop('redactor_options', {})
        super(RedactorjsTextarea, self).__init__(*args, **kwargs)

    def get_upload_params(self):
        kwargs = {}
        return {
            'imageUpload': reverse('redactorjs:image_upload', kwargs=kwargs),
            'fileUpload': reverse('redactorjs:file_upload', kwargs=kwargs)
        }

    def get_options(self):
        options = GLOBAL_OPTIONS.copy()
        options.update(self.get_upload_params())
        options.update(self.custom_options)
        return options

    def render(self, name, value, attrs=None):
        html = super(RedactorjsTextarea, self).render(name, value, attrs)
        final_attrs = self.build_attrs(attrs)

        html = INIT_JS.format(
            id=final_attrs.get('id'),
            options=json.dumps(self.get_options())
        ) + html

        return mark_safe(html)
