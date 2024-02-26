from django.shortcuts import render

from allegro.forms import ProfileForm


def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            # Formdagi ma'lumotlarni saqlash
            form.save()
            # Qo'shilgan ma'lumotlarni qaytarish yoki boshqa sahifaga yo'naltirish
    else:
        form = ProfileForm()
    return render(request, 'my_template.html', {'form': form})




