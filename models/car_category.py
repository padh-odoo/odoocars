from odoo import fields,models
class car_categories(models.Model):
    _name="car.categories"
    _description="Cars Categories"
    _sequence="sequence"
    
    sequence=fields.Integer("Sequence",default=1)
    name=fields.Char("Title",required=True)
    category_ids=fields.One2many("car.feature",'category')
    _sql_constraints=[('Check_Name','unique(name)','Category name already exist')]