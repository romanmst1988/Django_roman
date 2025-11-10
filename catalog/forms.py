from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import CheckboxInput

from .models import Product

# Запрещённые слова (константа)
FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price", "is_active"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Стилизация: bootstrap-like классы
        for fname, field in self.fields.items():
            # checkbox отдельно
            if isinstance(field, forms.BooleanField):
                field.widget = CheckboxInput(attrs={"class": "form-check-input"})
            else:
                # textarea and inputs
                field.widget.attrs.update(
                    {"class": "form-control", "placeholder": field.label}
                )
                # для Textarea у Django уже будет widget Textarea, class applied above is fine

    def _check_forbidden(self, value):
        if not value:
            return
        lower = value.lower()
        for bad in FORBIDDEN_WORDS:
            if bad in lower:
                raise ValidationError(f'Поле содержит запрещённое слово: "{bad}"')

    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        self._check_forbidden(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        self._check_forbidden(description)
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is None:
            return price
        try:
            if price < 0:
                raise ValidationError("Цена не может быть отрицательной.")
        except TypeError:
            raise ValidationError("Некорректный формат цены.")
        return price
