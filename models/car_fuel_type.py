from odoo import fields,models
class fuel_type(models.Model):
    _name="fuel.type"
    _description="Cars Fuel Type"
    
    name=fields.Char("Title",required=True)
    color=fields.Integer("Color",default=1)

    
    #Constraints
    _sql_constraints=[('Check_Name','unique(name)','Fuel Type already exist')]