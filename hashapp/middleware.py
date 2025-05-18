
from .modul_loader import get_modules_active
from django.urls import get_resolver, clear_url_caches
from django.utils.deprecation import MiddlewareMixin

class MiddlewareLoadModules(MiddlewareMixin):

    def process_request(self, request):
        clear_url_caches()
        url_resolver = get_resolver()

        # old URL patterns are loaded with the flag is_module=False.
        # if there are active modules, their urls will be added to the new patterns.
        # this solution ensures that the new url_patterns do not use any previously loaded data
        url_resolver.url_patterns = [
            url for url in url_resolver.url_patterns if not getattr(url, 'is_module', False)
        ]
        modules_active = get_modules_active()
        if len(modules_active) > 0:           
            url_modules = [ma for ma in modules_active ]
            url_resolver.url_patterns += url_modules
    

