from django.apps import AppConfig


class CollegeConfig(AppConfig):
    name = 'college'
    def ready(self):
        import college.mysignals
        # this is the syntax of signal throwing
        # it will be received at signals.py