from django import forms
from app.models import Bar, Tapa
from django.contrib.auth.models import User

class BarForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Introduce el nombre del bar.")
    visitas  = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    direccion = forms.CharField(max_length=128,label="Introduce la direccion del bar", help_text="Direccion con formato: <Pais, ciudad, calle>")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Bar
        fields = ('nombre', 'direccion')

class TapaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Introduce el nombre de la tapa.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols': 50}),max_length=200, help_text="Introduce una breve descripcion  de la tapa.")
    votos = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    bar = forms.ModelChoiceField(queryset=Bar.objects.all(),empty_label=None,help_text="Introduce el bar al que pertenece la tapa.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tapa
        fields = ('bar','nombre','descripcion', 'picture')
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        #exclude = ('bar',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

class RegistroForm(forms.Form):
    nombre = forms.CharField(label="Nombre :", widget=forms.TextInput())
    apellido = forms.CharField(label="Apellido :", widget=forms.TextInput())
    username = forms.CharField(label="Cuenta :", widget=forms.TextInput())
    email = forms.EmailField(label="Email :", widget=forms.EmailInput())
    password = forms.CharField(label="password :", widget=forms.PasswordInput(render_value=False),max_length=8,help_text="(numeros y letras hasta 8)")
    password2 = forms.CharField(label="confirmar password :", widget=forms.PasswordInput(render_value=False),max_length=8)

    def clean_username(self):
    	username = self.cleaned_data['username']
    	try:
    		u = User.objects.get(username=username)
    	except User.DoesNotExist:
    		return username
    	raise forms.ValidationError('***Usuario ya existe***')
    def clean_email(self):
    	email = self.cleaned_data['email']
    	try:
    		u = User.objects.get(email=email)
    	except User.DoesNotExist:
    		return email
    	raise forms.ValidationError('***Correo ya registrado***')
    def clean_password2(self):
    	password = self.cleaned_data['password']
    	password2 = self.cleaned_data['password2']
    	if password==password2:
    		pass
    	else:
    		raise forms.ValidationError('***Passwords no coinciden**')
    class Meta:
        model = User
        fields = ( 'nombre','apellido','username','email','password','password2')
