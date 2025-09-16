from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    name = fields.Char(required=True)
    description = fields.Text(string="Description")
    date_availability = fields.Date()
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
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
