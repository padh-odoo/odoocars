from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError
from dateutil.relativedelta import relativedelta


class car_feature(models.Model):
    _name="car.feature"
    _description="Features of Cars"
    _inherit=["mail.thread","mail.activity.mixin"]
    
    name=fields.Char("Car",required=True)
    description=fields.Text("Description")
    selling_price=fields.Integer("Selling Price",tracking=True)
    engine=fields.Integer("Engine")
    boot_space=fields.Integer("Boot Space")
    seating_capacity=fields.Integer("Seating Capacity")
    state=fields.Selection(selection=[("INS","REGISTERED"),("S","APPLIED")],default="INS")
    mileage=fields.Integer("Mileage")
    model=fields.Char("Model",tracking=True)
    transmission_type=fields.Selection(selection=[("manual","Manual"),("auto","Automatic")], string="Transmission Type",default="manual")
    category=fields.Many2one("car.categories", string="Category")
    fuel_id=fields.Selection(selection=[("H","Hybrid"),("P","Petrol")])
    brand=fields.Many2one("brand.type",string="Car Brand")
    offer_id=fields.Many2many("car.offer",string="Offer")
    image=fields.Image("Image")
    registration_number=fields.Char("Registration Number")
    chassis_number=fields.Char("Chassis Number")
    length=fields.Float("Length")
    gst=fields.Selection(selection=[('gst12',"GST 12%"),("gst28","GST 28%")],string="GST")
    total_airbags=fields.Integer("Total AirBags",compute="_compute_airbags",store=True)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Customer', index=True)


    
    # bool fields
    fog_lights=fields.Boolean("Fog Lights")
    airbag=fields.Boolean("Air Bag")
    airbag_passenger=fields.Boolean("Passenger AirBag")
    alloys=fields.Boolean("Alloys")
    abs=fields.Boolean("ABS")
    total=fields.Integer("Total Price",compute="_total_price",store=True)
    
    
    # Fiels for odoo wrap
    employee_id = fields.Many2one('hr.employee', string="Employee")
    mobile=fields.Char(related="employee_id.mobile_phone")
    name_imp=fields.Char(related="employee_id.name")
    email=fields.Char(related="employee_id.work_email")
    job_title=fields.Many2one(related="employee_id.job_id")
    department=fields.Many2one(related="employee_id.department_id")
    date_deadline=fields.Date("Renewal On",compute="_create_deadline")
    tenure=fields.Integer("Tenure",default=2,readonly=True)
    wrap=fields.Boolean("Wrap",default=False)
    wraping=fields.Selection(selection=[("F","Full Wraping"),("L","Light Wraping")])
    amount=fields.Integer("Amount", compute="_calculate_amount")

    
    
    #To calculate renewal deadline
    @api.depends('tenure','create_date')
    def _create_deadline(self):
        for i in self:
            i.date_deadline = ( (i.create_date.date() if i.create_date else fields.Date.today()) + relativedelta(years=i.tenure))
            
    
    # To calculate price to be paid
    @api.depends('wraping')
    def _calculate_amount(self):
        for i in self:
            if i.wraping=="F":
                i.amount=100000
            elif i.wraping=="L":
                i.amount=20000
            else:
                i.amount=0


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
        print(".................................", self.employee_id.name)
        if self.state=="INS":
          self.state="S"
        else:
         raise UserError("You cannot sold")
     
     
     
    # To calculate price after tax inclusion and  offer
    @api.depends('fuel_id','selling_price','gst','offer_id')
    def _total_price(self):
        for i in self:
            if (i.fuel_id=="H"):
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
    
    
    def wizard(self):
        return{
		    'type': 'ir.actions.act_window',
			'res_model': 'odoocars.wizard',
			'view_mode': 'form',
			'target': 'new',	
		}	
    