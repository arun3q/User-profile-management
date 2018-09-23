from django.apps import AppConfig


# class UsersConfig(AppConfig):
#     name = 'users'

#     def ready(self):
#     	import users.signals
    	
class MyAppConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals    	