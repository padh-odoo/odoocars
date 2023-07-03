from odoo import models,fields
class car_feature(models.Model):
    _name="car.feature"
    _description="Features of Cars"
    
    name=fields.Char("Title",required=True)
    description=fields.Text("Description",required=True)
    
    