from django.contrib import admin

from .models import * 
from django.http.response import HttpResponseRedirect

# Register your models here.

class ItemInline(admin.TabularInline):
    model = Item
    fields = [
      ('product', 'quantity'),
    ]

class OrderAdmin(admin.ModelAdmin):
  change_form_template = 'admin/change_form.html'
  inlines = [ItemInline]
  fieldsets = (
      ('Покупатель', {'fields': ['user']}),
      ('Детали заказа', {'fields': 
      [
	  ('order_source'),
        ('name' , 'phone', 'address',), 
        ('delivery', 'payment'),
        'delivery_discount_use',
        'coupon',
        'status', 
        ('bonus_gained', 'user_append_bonus',),
        'bonus_used', 
        'amount', 
      ]}),
  )
  autocomplete_fields = ['user',]

  list_display = ['user_info', 'created_at', 'status', 'amount']

  def user_info(self, obj):
        current_user = obj.user
        if (current_user):
          source = ''
          if obj.order_source:
            source += obj.get_order_source_display() + ', '
          return source + current_user.name + ', ' + current_user.phone
        else:
          result = ''
          if obj.order_source:
            result += obj.get_order_source_display() + ', '
          return result + 'Не авторизованный пользователь'


  def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['user'].label = 'Клиент'
        form.base_fields['amount'].label = 'Сумма заказа'
        form.base_fields['name'].label = 'Имя клиента'
        form.base_fields['phone'].label = 'Телефон клиента'
        form.base_fields['delivery'].label = 'Способ доставки'
        form.base_fields['address'].label = 'Адрес доставки'
        form.base_fields['payment'].label = 'Способ оплаты'
        form.base_fields['bonus_gained'].label = 'Клиент получит бонусов с заказа'
        form.base_fields['bonus_used'].label = 'Оплачено бонусами'
        form.base_fields['coupon'].label = 'Промокод'
        form.base_fields['status'].label = 'Статус заказа'
        form.base_fields['delivery_discount_use'].label = 'Использовать скидку на доставку'
        form.base_fields['user_append_bonus'].label = 'Начислить бонусы клиенту (по завершению заказа)'
        return form

  def response_change(self, request, obj):
        if "_count_amount" in request.POST:
            # obj.save()
            obj.amount = obj.calc_amount()
            if obj.user:
              if obj.user_append_bonus:
                obj.bonus_gained = calc_bonus_gained(obj.user, obj.amount)
              else:
                obj.bonus_gained = 0  
            else:
              obj.bonus_gained = 0
            obj.save()
            # matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            # matching_names_except_this.delete()
            # obj.is_unique = True
            # obj.save()
            self.message_user(request, "Заказ сохранен и посчитан")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)
  


admin.site.register(Order, OrderAdmin)
# admin.site.register(ViewedProduct)
# admin.site.register(Promocode)
# admin.site.register(Cart)
admin.site.register(Coupon)
# admin.site.register(Item)


