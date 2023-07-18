from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView, CreateView, View
from .models import Resident
from .forms import CreateResidentForm


class LandingPageView(LoginRequiredMixin, TemplateView, PermissionRequiredMixin):
    template_name = 'resident_app/landing_page.html'
    permission_required = 'accounts.CustomUser'


class ResidentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Resident
    template_name = 'resident_app/listing.html'
    context_object_name = 'records'
    paginate_by = 10  # Number of items per page
    permission_required = 'resident_app.view_resident'  # Required permission

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-pk')
        # Add any additional filtering or ordering here
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = context['records']
        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('accounts_app:login')  # Redirect to login page
        else:
            groups = self.request.user.groups.all()
            # Iterate over the groups
            for group in groups:
                print(group.name)
            return redirect('resident_app:no_perm')
        

class ResidentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Resident
    template_name = 'resident_app/resident_detail.html'
    context_object_name = 'record'
    permission_required = 'resident_app.view_resident'  # Required permission

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data if needed
        return context
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('accounts_app:login')
        else:
            return redirect('resident_app:no_perm')


class ResidentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Resident
    form_class = CreateResidentForm
    template_name = 'resident_app/create.html'
    success_url = 'resident_app:resident_list'
    permission_required = 'resident_app.add_resident'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('accounts_app:login')
        else:
            return redirect('resident_app:no_perm')


class ResidentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'resident_app.delete_resident'  # Required permission
    
    def post(self, request, pk):
        my_model = Resident.objects.get(pk=pk)
        my_model.delete()
        return redirect('resident_app:resident_list')
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('accounts_app:login')  # Redirect to login page
        else:
            return redirect('resident_app:no_perm')
        

class ResidentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'resident_app.change_resident'  # Required permission
    
    def get(self, request, pk):
        resident = get_object_or_404(Resident, pk=pk)
        form = CreateResidentForm(instance=resident)
        return render(request, 'resident_app/update_resident.html', {'form': form, 'res_id': pk})
    
    def post(self, request, pk):
        resident = get_object_or_404(Resident, pk=pk)
        print('pk--', pk)
        form = CreateResidentForm(request.POST, instance=resident)
        if form.is_valid():
            form.save()
            print('ran1---')
            return redirect('resident_app:resident_detail', pk=resident.pk)
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('accounts_app:login')  # Redirect to login page
        else:
            return redirect('resident_app:no_perm')