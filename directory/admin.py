from django.contrib import admin
from .models import *

admin.site.register(CipherSuite)
admin.site.register(Rfc)
admin.site.register(ProtocolVersion)
admin.site.register(KexAlgorithm)
admin.site.register(AuthAlgorithm)
admin.site.register(EncAlgorithm)
admin.site.register(HashAlgorithm)
admin.site.register(Vulnerability)
admin.site.register(StaticPage)
