from odoo import fields, models
class odoocars_wizard(models.TransientModel):
    _name="odoocars.wizard"
    _description = "Odoocars Wizard"
    
    category=fields.Many2one("car.categories", string="Category")
    new_name=fields.Char(" Category Name")
    
    
    
   
        
            
             
		
        
    