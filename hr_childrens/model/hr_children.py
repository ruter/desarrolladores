
#LFPV

from odoo import osv, fields


class HrEmployee(osv.Model):
    """Inherit hr_employee to add date_start and to add yours childrens
    """
    _inherit = "hr.employee"

    _columns = {
        'date_start': fields.date('Date Start'),
        'children_ids': fields.one2many(
            'hr.children', 'employee_id', 'Childrens')
    }


class HrChildren(osv.Model):
    """Class to add object of childrens to employee
    """
    _name = "hr.children"

    _order = 'name'

    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'date_of_birth': fields.date('Date of birth'),
        'schooling': fields.selection(
            [('elementary', 'Elementary'),
             ('high_school', 'High School'),
             ('preparatory', 'Preparatory'),
             ('university', 'University')], 'Schooling'),
        'employee_id': fields.many2one('hr.employee', 'Employee')
    }
