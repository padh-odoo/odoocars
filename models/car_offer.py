from odoo import fields,models
class car_offer(models.Model):
    _name="car.offer"
    _description="Cars Offer"
    
    name=fields.Char("Title",required=True)
    discount=fields.Integer("Discount",required=True)

    
    #Constraints
    _sql_constraints=[('Check_Name','unique(name)','Offer Type already exists'),
                      ('check_offer','CHECK(discount<=20)','Offer Discoutn Should be less than 20%')]