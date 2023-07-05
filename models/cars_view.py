from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError

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
    model=fields.Integer("Model")
    transmission_type=fields.Selection(selection=[("manual","Manual"),("auto","Automatic")], string="Transmission Type",default="manual")
    category=fields.Many2one("car.categories", string="Category")
    fuel_id=fields.Many2many("fuel.type",string="Fuel Type")
    brand=fields.Many2one("brand.type",string="Car Brand")
    total_airbags=fields.Integer("Total AirBags")
    image=fields.Image("Image")
    length=fields.Float("Length")
    gst=fields.Selection(selection=[('gst12',"GST 12%"),("gst28","GST 28%")],string="GST")
    
    # bool fields
    fog_lights=fields.Boolean("Fog Lights")
    airbag=fields.Boolean("Air Bag")
    airbag_passenger=fields.Boolean("Passenger AirBag")
    alloys=fields.Boolean("Alloys")
    abs=fields.Boolean("ABS")
    # total=fields.Integer("Total Price",compute="_total_price")
    
    
    # To calculate total airbags
    
    # @api.depends('airbag','airbag_passenger')
    # def _compute_airbags(self):
    #     for i in self:
    #         if i.airbag==True:
    #             i.total_airbags+=2
    
    
    
    
    # To calculate price after tax inclusion
    # @api.depends('gst','selling_price')
    # def _total_price(self):
    #     for i in self:
    #         if i.gst=="gst12":
    #             i.total+=i.selling_price*12/100
    
    
    @api.constrains('selling_price')
    def check_selling_price(self):
        if self.selling_price<0:
            raise ValidationError("Selling Price Must be Positive")
    
    
    