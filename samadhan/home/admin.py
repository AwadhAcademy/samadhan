from django.contrib import admin
from .models import quote_data
from .models import Carousel_Data
from .models import service
from .models import legal_service
from .models import tax_compliance
from .models import new_registration
from .models import bloging_data
from .models import additional_services
from import_export.admin import ImportExportModelAdmin

@admin.register(quote_data)
class userdat(ImportExportModelAdmin):
    pass
@admin.register(Carousel_Data)
class userdat(ImportExportModelAdmin):
    pass
@admin.register(service)
class userdat(ImportExportModelAdmin):
    pass
@admin.register(legal_service)
class userdat(ImportExportModelAdmin):
    pass
@admin.register(tax_compliance)
class userdat(ImportExportModelAdmin):
    pass
@admin.register(new_registration)
class userdat(ImportExportModelAdmin):
    pass

@admin.register(bloging_data)
class userdat(ImportExportModelAdmin):
    pass

@admin.register(additional_services)
class userdat(ImportExportModelAdmin):
    pass
# Register your models here.