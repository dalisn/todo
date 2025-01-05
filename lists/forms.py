from django import forms

def widget_attrs(placeholder):
    return {"class": "u-full-width", "placeholder": placeholder}


def form_kwargs(widget, label="", max_length=128):
    return {"widget": widget, "label": label, "max_length": max_length}



class TodoForm(forms.Form):
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("urgent", "Urgent"),
    ]

    description = forms.CharField(
        widget=forms.TextInput(attrs={"class": "u-full-width", "placeholder": "Enter your todo"}),
        label="Description",
        max_length=128,
    )
    limit_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "u-full-width"}),
        required=True,
        label="Expiration Date",
    )
    priority = forms.ChoiceField(
        choices=PRIORITY_CHOICES,
        widget=forms.Select(attrs={"class": "u-full-width"}),
        required=True,
        label="Priority",
    )




class TodoListForm(forms.Form):
    title = forms.CharField(
        **form_kwargs(
            widget=forms.TextInput(
                attrs=widget_attrs("Enter a title to start a new todolist")
            )
        )
    )
