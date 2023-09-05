from django.contrib import admin
from .models import KnapsackResults


class KnapsackResult(admin.ModelAdmin):
    list_display = ('appliance1', 'appliance2', 'appliance3', 'appliance4', 'appliance5', 'appliance6', 'appliance7',
                    'appliance8', 'appliance9', 'appliance10',  'price_of_electricity', 'price_of_high_tariffs')


admin.site.register(KnapsackResults, KnapsackResult)

