{
    "name": "Estate",  # The name that will appear in the App list
    "version": "16.0.0",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [],
    "installable": True,
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_property_list.xml",
        "views/estate_property_menus.xml",
        "views/estate_property_search.xml",
        "views/estate_property_form.xml",
        "views/estate_offer_form.xml",
    ],
}
