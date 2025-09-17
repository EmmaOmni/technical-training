from odoo import fields, models


class EstateOffer(models.Model):
    _name = "estate.offer"
    _description = "Offer"
    price = fields.Float(string="Price", required=True)
    property = fields.One2many("estate.property", string="Property")
