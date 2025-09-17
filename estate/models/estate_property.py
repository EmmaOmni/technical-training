from odoo import api, fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    name = fields.Char(required=True)
    description = fields.Text(string="Description")
    date_availability = fields.Date()
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", copy=False, required=True)
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    garden = fields.Boolean(string="Garden")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
    )
    garden_area = fields.Integer(string="Garden Area")
    living_area = fields.Integer(string="Living Area")
    cancelled = fields.Boolean(string="Cancelled")
    sold = fields.Boolean(string="Sold")
    offer_ids = fields.One2many("estate.offer", "property_id", string="Offer")

    total_area = fields.Integer(compute="_compute_areas")

    best_offer_price = fields.Integer(compute="_compute_best_offer_price")

    def _compute_areas(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    def _onchange_description(self):
        self.description += "... desc"

    def action_cancel(self):
        for estate_property in self:
            estate_property.cancelled = True
            estate_property.sold = False
        return True
