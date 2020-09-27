import datetime
from django import forms


class CouponForm(forms.Form):
    name = forms.CharField(label='Name', max_length=20)
    creator = forms.CharField(label="Creator", max_length=50)
    use_count = forms.IntegerField(label='Use count', min_value=1, max_value=100)
    percent_amount = forms.IntegerField(min_value=1, max_value=100)
    expire_date = forms.DateField(label="Expire date", widget=forms.DateInput)

    def clean(self):
        super(CouponForm, self).clean()

        name = self.cleaned_data.get('name')
        creator = self.cleaned_data.get('creator')
        use_count = self.cleaned_data.get('use_count')
        percent_amount = self.cleaned_data.get('percent_amount')
        expire_date = self.cleaned_data.get('expire_date')

        if not name:
            self._errors['name'] = self.error_class(
                ["The field name is required"])
        if len(name) > 20:
            self._errors['name'] = self.error_class(
                ["The field name must contain maximum of 20 characters"])

        if not creator:
            self._errors['creator'] = self.error_class(
                ["The field creator is required"])
        if len(creator) > 50:
            self._errors['creator'] = self.error_class(
                ["The field creator must contain maximum of 50 characters"])

        if not use_count:
            self._errors['use_count'] = self.error_class(
                ["The field Use count is required"])
        if use_count < 1 or use_count > 100:
            self._errors['use_count'] = self.error_class(
                ["Introduce a value between 1 and 100"])

        if not percent_amount:
            self._errors['percent_amount'] = self.error_class(
                ["The field Percent amount is required"])
        if percent_amount < 1 or percent_amount > 100:
            self._errors['percent_amount'] = self.error_class(
                ["Introduce a value between 1 and 100"])

        if not expire_date:
            self._errors['expire_date'] = self.error_class(
                ["The field Expire date is required"])

        # if datetime.datetime.now().time() > datetime.datetime(expire_date).time():
        #     self._errors['expire_date'] = self.error_class(
        #         ["Can't set expire date in past"])

        return self.cleaned_data
