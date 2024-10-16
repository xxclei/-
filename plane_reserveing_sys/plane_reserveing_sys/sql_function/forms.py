from django import forms
from .models import Traveler
from django.core.exceptions import ValidationError
import re


class TravelerForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ['name', 'gender', 'work_unit', 'id_number', 'travel_date', 'destination', 'file']
    def clean_id_number(self):
        id_number = self.cleaned_data.get('id_number')
        if not re.match(r'^\d{15}$|^\d{18}$', id_number):
            raise ValidationError('身份证号格式不正确，请重新输入。')
        return id_number
    def clean(self):
        cleaned_data = super().clean()  # 调用父类的 clean 方法
        # 可以在这里添加更多的表单级验证
        return cleaned_data