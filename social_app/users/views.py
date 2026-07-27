from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from . forms import RoleAssignmentForm
from django.contrib.auth import get_user_model

User= get_user_model()

@staff_member_required
def assign_roles(request,user_id):
    user_obj=get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        form=RoleAssignmentForm(request.POST,instance=user_obj)
        if form.is_valid():
            form.save()
            messages.success(request,f"Roles updated for {user_obj.email}")
            return redirect("user-list")
        else:
            form=RoleAssignmentForm(instance=user_obj)

        return render(request,"users/assign_roles.html",{
            "form":form,
            "user_obj":user_obj
        })