# forms.py
from django import forms
from .models import CourseMaster, Reserver

class ReserverForm(forms.ModelForm):
    class Meta:
        model = Reserver
        fields = ['reserver_name', 'email', 'tel', 'reservation_date']
    course_id = forms.ModelChoiceField(queryset=CourseMaster.objects.all(), to_field_name='id',label="course_name")
    
    def clean_course_id(self):
        course_name = self.cleaned_data['course_id']
        try:
            # 入力されたコース名に対応するCourseMasterを取得
            course_master = CourseMaster.objects.get(course_name=course_name)
            return course_master.id
        except CourseMaster.DoesNotExist:
            # 存在しない場合は適切に処理
            raise forms.ValidationError(f"Course '{course_name}' does not exist.")