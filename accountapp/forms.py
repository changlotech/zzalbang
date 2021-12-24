from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #UserCreationForm 이라는 장고가 제공하는 폼을 이용하는데 한가지 기능을 추가할 것이다
        #아이디는 바꿀수 없게 하겠다.
        self.fields['username'].disabled =True


