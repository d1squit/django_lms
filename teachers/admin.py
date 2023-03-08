from django.contrib import admin

from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'salary')
	list_display_links = list_display
	list_per_page = 15
	search_fields = ('first_name', 'last_name')

	fieldsets = (
		('Personal info', {'fields': ('first_name', 'last_name')}),
		('Born', {'fields': ('birthday', 'get_age')}),
		('Contact', {'fields': ('email', 'city')}),
	)

	def get_age(self, instance):
		return f'Age: {instance.get_age()} year(s)'

	readonly_fields = ('get_age', )

	get_age.short_description = 'Age'


admin.site.register(Teacher, TeacherAdmin)
