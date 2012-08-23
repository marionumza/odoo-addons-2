# -*- encoding: utf-8 -*-
##############################################################################
#
#    AvanzOSC, Avanzed Open Source Consulting 
#    Copyright (C) 2011-2012 Iker Coranti (www.avanzosc.com). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from osv import osv
from osv import fields

class res_partner_contact(osv.osv):

    _inherit = 'res.partner.contact'
    
    def onchange_type(self, cr, uid, ids, type):
        
        value = {}
        if type == 'student' :
            number=self.pool.get('ir.sequence').get(cr, uid, 'res.partner.contact')
            value.update({
                      'student_number':number
        })
        return {
                'value':value
        } 
    
#    def _stud_code(self, cr, uid, ids, name, args, context=None):
#        res = {}
#        code=''
#        res_partner_contact_obj = self.pool.get('res.partner.contact')
#        for contact in self.browse(cr, uid, ids, context=context):
#            type=contact.type
#            if type == 'student' :
#                print contact.registered
#                if contact.registered == False:
#                    res_partner_contact_obj.write(cr,uid,contact.id,{'registered':True})
#                    code=self.pool.get('ir.sequence').get(cr, uid, 'res.partner.contact')
#            res[contact.id]=code
#        return res
    
    _columns = {
            'type': fields.selection([('student','Student'),('teacher','Teacher'),('other','Other')],'Type'),
            'student_number':fields.char('Student Number', size=64),
            'face_code':fields.char('Face Code', size=64),
            'online_code':fields.char('Online Code', size=64),
            'face':fields.boolean('Face'),
            'online':fields.boolean('Online'),
            'state_id':fields.many2one('res.country.state','State'),
            'profession':fields.char('Profession', size=64),
            'parent_studies':fields.char('Parent studies', size=64),
            'access_year': fields.integer('Access year'),
            'authorized_person_ids':fields.one2many('authorized.person', 'contact_id', "Authorized People"),
            'tutor':fields.many2one('res.partner.contact','Tutor'),
        }
    _defaults = {
#                 'student_code': lambda self,cr,uid,context={}: self.pool.get('ir.sequence').get(cr, uid, 'res.partner.contact'),
#                 'type':lambda *a: 'student',
                 }
res_partner_contact()
