from django.contrib import admin


class CustomAdminSite(admin.AdminSite):
    def _build_app_dict(self, request, label=None):
        # merge Django's auth.Group into our 'users' app to remove clutter
        app_dict = super()._build_app_dict(request)
        if "auth" in app_dict and "administration" in app_dict:
            app_dict["administration"]["models"].extend(app_dict.pop("auth")["models"])
        if label:
            return app_dict.get(label)
        return app_dict


admin_site = CustomAdminSite()
