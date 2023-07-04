from odoo import models,fields,api
class car_feature(models.Model):
    _name="car.feature"
    _description="Features of Cars"
    
    name=fields.Char("Title",required=True)
    description=fields.Text("Description",required=True)
    selling_price=fields.Integer("Selling Price")
    engine=fields.Integer("Engine")
    boot_space=fields.Integer("Boot Space")
    seating_capacity=fields.Integer("Seating Capacity")
    mileage=fields.Integer("Mileage")
    transmission_type=fields.Selection(selection=[("manual","Manual"),("auto","Automatic")], string="Transmission Type",default="manual")
    category=fields.Many2one("car.categories", string="Category")
    fuel_id=fields.Many2many("fuel.type",string="Fuel Type")
    brand=fields.Many2one("brand.type",string="Car Brand")
    
    # @api.depends('transmission_type')
    # def _compute_selling_price(self):
    #     for i in self:
    #         if i.transmission_type=='auto':
    #             i.sellingprice+=100000
                
    
    