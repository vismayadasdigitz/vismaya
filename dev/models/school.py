from OpenSSL.crypto import verify

from odoo import fields,models,api
from odoo.api import onchange
from odoo.tools.populate import compute


class School(models.Model):
    _name = 'school.student'

    name=fields.Char(string='Name')
    age=fields.Integer(string='Age')
    teacher=fields.Many2one('school.teacher',string="Teacher")
    teachers=fields.Many2many('school.teacher',string="Teachers")
    color=fields.Integer(string="color")
    state=fields.Selection(
        selection=[
            ('draft',"draft"),
            ('done',"done"),
            ('success',"success"),
        ],
        string="status",
        readonly=True,copy=False,index=True,
        tracking=3,
        default='draft'

    )
    payment_status=fields.Selection(selection=[('payment_pending','payment_pending'),('payment_success','payment_success')],
                                    string='payment_status',onchange='_onchange_payment_status')
    parents_ids=fields.One2many('student.details','teacher',string='parent_id')
    image_1920=fields.Image(string="image")

    @api.onchange('payment_status')
    def _onchange_payment_status(self):
        if self.payment_status=='payment_pending':
            self.state='done'
        elif self.payment_status == 'payment_success':
            self.state = 'success'

    def draft(self):
        self.write({'state':'draft'})


    def done(self):
        self.write({'state': 'done'})

    def success(self):
        self.write({'state': 'success'})

class Teacher(models.Model):
    _name = 'school.teacher'

    name=fields.Char(string='teacher_name')
    age=fields.Integer(string='Age')
    teacher_ids=fields.One2many('fee.details','teacher',string='Teacher')




class Student(models.Model):
    _name = 'student.details'

    name=fields.Char(string="Name")
    parents_name=fields.Char(string="parents name")
    address=fields.Char(string='Address')
    phone_number=fields.Integer(string="Phone number")
    teacher=fields.Many2one('school.student', string="Teacher")

class Fee(models.Model):
    _name = 'fee.details'

    fee=fields.Float(string="fee")
    month=fields.Integer(string="month")
    total_fee = fields.Integer(string="total_fee",compute="_compute_total_fee")
    teacher=fields.Many2one('school.teacher', string="Teacher")

    @api.depends('fee', 'month')
    def _compute_total_fee(self):
        for record in self:
            record.total_fee= record.fee * record.month



