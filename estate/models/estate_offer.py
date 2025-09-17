from odoo import fields, models
from odoo.exceptions import UserError


class EstateOffer(models.Model):
    _name = "estate.offer"
    _description = "Offer"
    accepted = fields.Boolean(string="Accepted")
    refused = fields.Boolean(string="Refused")
    price = fields.Float(string="Price", required=True)
    property_id = fields.Many2one("estate.property", string="Property")

    def action_accept_offer(self):
        for offer in self:
            offer.accepted = True
            if offer.property_id.cancelled:
                raise UserError("The property is already cancelled")

            if offer.property_id.sold:
                raise UserError("The property is already sold")

            offer.property_id.cancelled = False
            offer.property_id.sold = True
            offer.property_id.selling_price = offer.price
        return True
