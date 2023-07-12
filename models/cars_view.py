from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError

class car_feature(models.Model):
    _name="car.feature"
    _description="Features of Cars"
    
    name=fields.Char("Title",required=True)
    description=fields.Text("Description")
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
    image=fields.Image("Image")
    state=fields.Selection(selection=[("INS","IN STOCK"),("S","SOLD")],default="INS")
    length=fields.Float("Length")
    gst=fields.Selection(selection=[('gst12',"GST 12%"),("gst28","GST 28%")],string="GST")
    total_airbags=fields.Integer("Total AirBags",compute="_compute_airbags",store=True)
    
    # bool fields
    fog_lights=fields.Boolean("Fog Lights")
    airbag=fields.Boolean("Air Bag")
    airbag_passenger=fields.Boolean("Passenger AirBag")
    alloys=fields.Boolean("Alloys")
    abs=fields.Boolean("ABS")
    total=fields.Integer("Total Price",compute="_total_price",store=True)
    
    
    # To calculate total airbags
    
    @api.depends('airbag','airbag_passenger')
    def _compute_airbags(self):
        for i in self:
            if i.airbag:
                i.total_airbags=2
                if i.airbag_passenger:
                    i.total_airbags+=4
            else:
                i.total_airbags=0

            
    
    def action_sold(self):
        
        if self.state=="INS":
            self.state="S"
        else:
            raise UserError("You cannot sold")
    
    
    
    # To calculate price after tax inclusion
    @api.depends('fuel_id','selling_price','gst','offer_id')
    def _total_price(self):
        for i in self:
            if (i.fuel_id.name=="Electric"):
                i.total= i.selling_price +i.selling_price*12/100
                i.gst='gst12'  
            else:
                i.total= i.selling_price +i.selling_price*28/100
                i.gst="gst28" 
            """if i.offer_id:
               if (i.offer_id.name=="Launch"):
                i.total=i.selling_price-i.selling_price*10/100
               elif (i.offer_id.name=="Festive"):
                i.total=i.selling_price-i.selling_price*5/100 """
        
    # Python Constrints
    @api.constrains('selling_price')
    def check_selling_price(self):
        if self.selling_price<0:
            raise ValidationError("Selling Price Must be Positive")
    
    
    