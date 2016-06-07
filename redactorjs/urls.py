from django.conf.urls import url

from redactorjs.views import DefaultRedactorUploadView, upload

# Using simple view function
# urlpatterns = [
#     url('^image_upload/$', upload, {'type': 'image'}, name='image_upload'),
#     url('^file_upload/$', upload, {'type': 'file'}, name='file_upload')
# ]

# Using class-based view
urlpatterns = [
    url('^image_upload/$', DefaultRedactorUploadView.as_view(), {'type': 'image'}, name='image_upload'),
    url('^file_upload/$', DefaultRedactorUploadView.as_view(), {'type': 'file'}, name='file_upload')
]
