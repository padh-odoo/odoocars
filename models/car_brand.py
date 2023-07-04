from odoo import fields,models
class brand_type(models.Model):
    _name="brand.type"
    _description="Cars Brand"
    
    name=fields.Char("Title")
    brand_ids=fields.One2many("car.feature" ,'brand')