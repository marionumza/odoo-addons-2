# Copyright 2019 Mentxu Isuskitza - AvanzOSC
# Copyright 2019 Oihana Larrañaga - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Fleet Route",
    "version": "12.0.2.0.0",
    "license": "AGPL-3",
    "depends": [
        "fleet",
        "hr",
        "resource",
    ],
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "category": "Human Resources",
    "data": [
        "data/fleet_route_data.xml",
        "security/ir.model.access.csv",
        "views/fleet_route_view.xml",
        "views/fleet_route_stop_view.xml",
        "views/fleet_vehicle_view.xml",
        "views/fleet_route_menu_view.xml",
    ],
    "installable": True,
}
