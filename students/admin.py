from django.contrib import admin

from students.models import Student


class GroupListFilter(admin.SimpleListFilter):
	from groups.models import Group

	title = 'group'
	parameter_name = 'group_filter'

	def lookups(self, request, model_admin):
		groups = self.Group.objects.all().order_by('name')
		data = [(group.pk, group.name) for group in groups]
		data.insert(0, (0, '----------'))
		return tuple(data)

	def queryset(self, request, queryset):
		if self.value() is None:
			students = Student.objects.all()
		elif self.value() == '0':
			students = Student.objects.filter(group__isnull=True)
		else:
			students = Student.objects.filter(group=self.Group.objects.get(pk=int(self.value())))

		return students.order_by('first_name', 'last_name')


class StudentAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'get_group_info')
	list_display_links = list_display
	list_per_page = 15
	list_filter = (GroupListFilter, )
	search_fields = ('first_name', 'last_name')

	def get_group_info(self, instance):
		if instance.group:
			return instance.group.name
		else:
			return ''

	get_group_info.short_description = 'group'

	fieldsets = (
		('Personal info', {'fields': ('first_name', 'last_name')}),
		('Born', {'fields': ('birthday', 'get_age')}),
		('Contact', {'fields': ('email', 'city')}),
		(' ', {'fields': ('group', )}),
	)

	def get_age(self, instance):
		return f'Age: {instance.get_age()} year(s)'

	def get_form(self, request, obj=None, change=False, **kwargs):
		form = super().get_form(request, obj, change, **kwargs)
		form.base_fields['group'].widget.can_add_related = False
		form.base_fields['group'].widget.can_change_related = False
		form.base_fields['group'].widget.can_view_related = False
		form.base_fields['group'].widget.can_delete_related = False
		return form

	readonly_fields = ('get_age', )

	get_age.short_description = 'Age'


admin.site.register(Student, StudentAdmin)
