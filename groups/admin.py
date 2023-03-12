from django import forms
from django.contrib import admin

from groups.models import Group


class StudentsInlineTable(admin.TabularInline):
    from students.models import Student
    model = Student
    fields = ('first_name', 'last_name', 'email')
    extra = 0
    readonly_fields = fields

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class TeachersInlineTable(admin.TabularInline):
    from teachers.models import Teacher
    model = Group.teachers.through
    extra = 0
    fields = ('get_first_name', 'get_last_name', 'get_salary')
    readonly_fields = fields

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_first_name(self, instance):
        return self.Teacher.objects.get(pk=instance.teacher_id).first_name

    def get_last_name(self, instance):
        return self.Teacher.objects.get(pk=instance.teacher_id).last_name

    def get_salary(self, instance):
        return self.Teacher.objects.get(pk=instance.teacher_id).salary

    get_first_name.short_description = 'first_name'
    get_last_name.short_description = 'last_name'
    get_salary.short_description = 'salary'


class GroupAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman'].choices = [(s.pk, f'{s.first_name} {s.last_name}') for s in self.instance.students.all()]
        self.fields['headman'].choices.insert(0, (0, '-------'))

        self.fields['headman'].widget.can_add_related = False
        self.fields['headman'].widget.can_change_related = False
        self.fields['headman'].widget.can_view_related = False
        self.fields['headman'].widget.can_delete_related = False

    class Meta:
        model = Group
        fields = '__all__'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    list_display = ('name', 'start', 'end')
    fields = (
        'name',
        ('start', 'end'),
        'headman',
        'teachers',
        ('created', 'updated'),
    )

    readonly_fields = ('created', 'updated')
    inlines = [StudentsInlineTable, TeachersInlineTable]
