from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django import forms

from scioly_volunteers.authentication.models import User
from scioly_volunteers.volunteers.models import State


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label="First name",
        max_length=150,
        required=True,
    )

    last_name = forms.CharField(
        label="Last name",
        max_length=150,
        required=True,
    )

    email = forms.EmailField(
        label="Email",
        max_length=254,
        required=True,
    )

    username = forms.CharField(
        label="Username",
        max_length=150,
        required=True,
    )

    password = forms.CharField(
        label="Password",
        min_length=8,
        max_length=150,
        required=True,
        widget=forms.PasswordInput,
    )

    password_confirm = forms.CharField(
        label="Confirm password",
        min_length=8,
        max_length=150,
        required=True,
        widget=forms.PasswordInput,
    )

    states = forms.ModelMultipleChoiceField(
        queryset=State.objects.all(), required=False
    )

    years_of_experience = forms.IntegerField(required=False)

    bio = forms.CharField(max_length=2000, required=False)

    publish_data = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")

    def save(self):
        user = User.objects.create_user(
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            email=self.cleaned_data["email"],
            username=self.cleaned_data["username"],
            password=self.cleaned_data["password"],
            years_of_experience=self.cleaned_data["years_of_experience"],
            bio=self.cleaned_data["bio"],
            publish_data=self.cleaned_data["publish_data"],
        )
        user.states.set(self.cleaned_data["states"])

        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "registrationForm"
        self.helper.form_class = "registrationForm"
        self.helper.form_method = "post"
        self.helper.form_action = "register"

        self.helper.add_input(Submit("submit", "Submit"))
