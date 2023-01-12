# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lector(models.Model):
    _name = 'biblioteca.lector'
    _description = 'Representa el lector de un libro'

    dni = fields.Char('Dni', required=True, size=7)
    nombre = fields.Char('Nombre', required=True)
    prestamos = fields.Integer(string='Prestamos', max=10)
    prestamo_ids = fields.One2many('garaje.prestamo', 'dni', string='lector-prestamo')


class prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'Representa el prestamo de un libro'

    identification = fields.Integer(string='Id', max=10) 
    id = fields.id(string='Identificador') 
    fechaInicio = fields.Date(string='Fecha de inicio')
    fechaFin = fields.Date(string='Fecha de fin')
    lector_id = fields.Many2one('garaje.lector', 'id', string='prestamo-lector')


 class libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Representa un libro'

    isbn = fields.Char('Isbn', required=True, size=17)    
    titulo = fields.Char('Titulo', required=True)
    numeroDePaginas = fields.Integer(string='numero de paginas') 
    editorial_ids = fields.One2many('garaje.editorial', 'isbn', string='libro-editorial')
    autor_ids = fields.many2many('garaje.autor', 'isbn', string='libro-autor')
   

 class editorial(models.Model):
    _name = 'biblioteca.editorial'
    _description = 'Representa la editorial de un libro'
    
    nombre = fields.Char('Nombre', required=True)
    editorial_ids = fields.Many2one('garaje.libro', 'nombre', string='editorial-libro')


 class autor(models.Model):
    _name = 'biblioteca.autor'
    _description = 'Representa un autor'

    dni = fields.Char('Dni', required=True, size=7)
    nombre = fields.Char('Nombre', required=True)
    nacimiento = fields.Date(string='Fecha de nacimiento del autor')
    edad = fields.Integer(string='Edad', compute='calculaEdad')
    libro_ids = fields.many2many('garaje.libro', 'dni', string='autor-libro')

    @api.depends
    def calculaEdad(self):
        for autor in self:
            #calculamos edad


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
