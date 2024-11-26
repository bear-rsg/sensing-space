from django.views.generic import TemplateView


class AboutTemplateView(TemplateView):
    """
    Class-based view to show the about template
    """
    template_name = 'general/about.html'


class CampusTemplateView(TemplateView):
    """
    Class-based view to show the campus template
    """
    template_name = 'general/campus.html'


class CookiesTemplateView(TemplateView):
    """
    Class-based view to show the cookies template
    """
    template_name = 'general/cookies.html'
