from django.views.generic import (CreateView, UpdateView)
from django.urls import reverse_lazy
from . import models
from . import forms


class SurveyCreateView(CreateView):
    """
    Class-based view to show the survey create template
    (which is also the welcome template)
    """
    template_name = 'researchdata/survey-create.html'
    model = models.Survey
    form_class = forms.SurveyCreateForm

    def form_valid(self, form):
        """
        Set the geolocation fields
        """
        form.instance.geolocation_latitude = form.data['geolocation_latitude']
        form.instance.geolocation_longitude = form.data['geolocation_longitude']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('researchdata:survey-update', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = models.Location.objects.all()
        context['emotions'] = models.Emotion.objects.all()
        return context


class SurveyUpdateView(UpdateView):
    """
    Class-based view to show the survey create template
    (which is also the welcome template)
    """
    template_name = 'researchdata/survey-update.html'
    model = models.Survey
    form_class = forms.SurveyUpdateForm
    slug_field = 'slug'

    def get_success_url(self):
        return reverse_lazy('researchdata:survey-final', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emotions'] = models.Emotion.objects.all()
        return context


class SurveyFinalUpdateView(UpdateView):
    """
    Class-based view to show the final survey section template
    """
    template_name = 'researchdata/survey-final.html'
    model = models.Survey
    form_class = forms.SurveyFinalForm
    slug_field = 'slug'
    success_url = reverse_lazy('researchdata:survey-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colours'] = models.Colour.objects.all()
        context['times_experienced_effects'] = models.TimesExperiencedEffects.objects.all()
        return context
