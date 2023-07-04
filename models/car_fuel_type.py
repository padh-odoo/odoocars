from odoo import fields,models
class fuel_type(models.Model):
    _name="fuel.type"
    _description="Cars Fuel Type"
    
    name=fields.Char("Title")