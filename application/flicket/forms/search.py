#! usr/bin/python3
# -*- coding: utf8 -*-

from flask_wtf import FlaskForm
from wtforms import SelectField, StringField

from .flicket_forms import does_email_exist
from application.flicket.models.flicket_models import  FlicketCategory, FlicketDepartment, FlicketStatus

class SearchTicketForm(FlaskForm):

    def __init__(self, *args, **kwargs):
        form = super(SearchTicketForm, self).__init__(*args, **kwargs)

        # todo: There must be a better way. See below.
        """ department and category choices are over written by jquery. I can't seem to access the data
        unless I generate the data here. :( """
        self.department.choices = [(d.id, d.department) for d in FlicketDepartment.query.all()]
        self.department.choices.insert(0, (0, 'department'))

        self.category.choices = [(c.id, c.category) for c in FlicketCategory.query.all()]
        self.category.choices.insert(0, (0, 'category'))

        self.status.choices = [(s.id, s.status) for s in FlicketStatus.query.all()]
        self.status.choices.insert(0, (0, 'status'))

    """ Search form. """
    department = SelectField('department', coerce=int)
    category = SelectField('category', coerce=int)
    status = SelectField('status', coerce=int)
    email = StringField('email', validators=[does_email_exist])
    content = StringField('content', validators=[])