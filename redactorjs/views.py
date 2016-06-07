from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.views.generic import View
from django.views.generic.edit import FormMixin, ProcessFormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from redactorjs.forms import ImageForm, FileForm
from redactorjs.models import RedactorjsFile

def save_file(file_, is_image=False):
    fileobj = RedactorjsFile.objects.create(upload=file_, is_image=type == 'image')
    return {
        'url':  fileobj.upload.url,
        'id': fileobj.id,
        'name': file_.name
    }



# Simple view function

@csrf_exempt
@require_POST
#@login_required
def upload(request, type='file'):

    if 'file' not in request.FILES:
        return JsonResponse({'error': True, 'message': 'Bad request'}, safe=False)

    file_ = request.FILES['file']
    response_data = save_file(file_, is_image=type == 'image')
    return JsonResponse(response_data, safe=False)



# Class-based view

REDACTOR_UPLOAD_FORMS = {
    'image': ImageForm,
    'file': FileForm
}

class BaseRedactorUploadView(FormMixin, ProcessFormView, View):
    http_method_names = ['post']
    file_storage = default_storage

    def _get_type(self):
        return self.kwargs.get('type', 'file')

    def get_form_class(self):
        return REDACTOR_UPLOAD_FORMS.get(self._get_type())

    def form_valid(self, form):
        file_ = form.cleaned_data['file']
        response_data = save_file(file_, is_image=self._get_type == 'image')
        return JsonResponse(response_data, safe=False)

    def form_invalid(self, form):
        return JsonResponse({
            'error': True,
            'message': 'Bad request'
        }, safe=False)


class DefaultRedactorUploadView(BaseRedactorUploadView):
    @method_decorator(csrf_exempt)
    #@method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(DefaultRedactorUploadView, self).dispatch(request, *args, **kwargs)
