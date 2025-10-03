from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Country
from .forms import CountryForm

# --------------------------
# LISTAR con búsqueda, filtros y paginación
# --------------------------
def country_list(request):
    search = request.GET.get('q')  # búsqueda por nombre o abreviatura
    status_filter = request.GET.get('status')  # filtro por estado

    countries = Country.objects.all().order_by('name')

    # Filtro por nombre o abreviatura
    if search:
        countries = countries.filter(name__icontains=search) | countries.filter(abbrev__icontains=search)

    # Filtro por estado
    if status_filter in ['1', '0']:
        countries = countries.filter(status=(status_filter == '1'))

    # Paginación: 5 países por página
    paginator = Paginator(countries, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'banking_app/country_list.html', {
        'page_obj': page_obj,
        'search': search,
        'status_filter': status_filter,
    })


# --------------------------
# CREAR
# --------------------------
def country_create(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'País creado correctamente.')
            return redirect('banking_app:country_list')
    else:
        form = CountryForm()
    return render(request, 'banking_app/country_form.html', {'form': form, 'action': 'Crear'})


# --------------------------
# EDITAR
# --------------------------
def country_edit(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            messages.success(request, 'País actualizado correctamente.')
            return redirect('banking_app:country_list')
    else:
        form = CountryForm(instance=country)
    return render(request, 'banking_app/country_form.html', {'form': form, 'action': 'Editar'})


# --------------------------
# ELIMINAR con confirmación
# --------------------------
def country_delete(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == "POST":
        country.delete()
        messages.success(request, f"País {country.name} eliminado correctamente.")
        return redirect('banking_app:country_list')
    return render(request, 'banking_app/country_confirm_delete.html', {'country': country})
