# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class empresa(models.Model):
#     _name = 'empresa.empresa'
#     _description = 'empresa.empresa'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import models, fields, api
#hace falta para _get_annios(self)
from dateutil.relativedelta import *
from datetime import date

class cliente(models.Model):
    _name = 'empresa.cliente'
    _description = 'Características de un cliente'

    name = fields.Char('Dni', required = True, size=9)
    nombre = fields.Char(string='Nombre', required = True)
    fechaNacimiento = fields.Date('Fecha', required = True, default = fields.Date.today())
    edad = fields.Integer('Edad', required = True, compute='_get_annios') 
    direccion = fields.Text('Direccion', required = True)
    telefono = fields.Integer('Telefono', required = True, size=9)#api.constraints
    

    @api.constrains('dni','telefono')
    def _check_value(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if (self.telefono < 600000000 or self.telefono > 700000000):
            raise ValidationError('tfno incorrecto')
        if (len(self.dni) != 9 or letras[int(self.dni[:8]) % 23] != self.dni[8]):
            raise ValidationError('dni incorrecto')

    @api.depends('fechaNacimiento') 
    def _get_annios(self): 
        for cliente in self: 
            hoy = date.today()
            cliente.edad = relativedelta(hoy, cliente.fechaNacimiento).years
    
    factura_ids = fields.One2many('empresa.factura', 'cliente_id', string='cliente-factura')


class factura(models.Model):
    _name='empresa.factura'
    _description = 'Características de una factura'

    name = fields.Integer('NumFactura', required = True) 
    fechaEmision = fields.Date('FechaEmision', required = True, default = fields.Date.today())
    total = fields.Float('Total',(7,2), required = True) 

    @api.constrains('total')
    def _check_value(self):
        if len(str(self.total))>7:
            raise ValidationError('Debe tener 4 números naturales y 2 decimales o menos')
    #Campos relacionales
    cliente_id = fields.Many2one('empresa.cliente', string='DniCliente')
    producto_ids = fields.One2many('empresa.producto', 'factura_id', string='factura-producto')

        
class producto(models.Model):
    _name = 'empresa.producto'
    _description = 'Caracteristicas de un producto'

    identificador = fields.Integer('Identificador', required = True)
    nombre = fields.Char(string='Nombre', required = True)
    descripcion = fields.Text('Descripcion', required = True)
    precio = fields.Float('Precio', help='Coste total de producto') # 4 números naturales más 2 decimales
    stock = fields.Integer('Stock', required = True)

    @api.constrains('precio')
    def _check_value(self):
        if len(str(self.precio))>7:
            raise ValidationError('Debe tener 4 números naturales y 2 decimales o menos')

    #Campos relacionales
    factura_id = fields.Many2one('empresa.factura', string='numFactura')
    categoria_id = fields.Many2one('empresa.categoria', string='Categoria')
    proveedor_id = fields.Many2one('empresa.proveedor', string='nifProveedor')


class categoria(models.Model):
    _name = 'empresa.categoria'
    _description = 'Caracteristicas de una categoria'

    name = fields. Selection (string = 'Nombre', selection =[('o','Ordenadores'),('s','Smartphones'),('a','Audiovisual'), ('p','Periféricos'),('t','Televisores'), ('g','Gaming'), ('so','Software'), ('aam','Aplicaciones a medida'), ('r','Reparaciones'), ('pda','PDAs')], default='o')
    
    producto_ids = fields.One2many('empresa.producto', 'categoria_id', string='categoria-producto')

class proveedor(models.Model):
    _name = 'empresa.proveedor'
    _description = 'Características de un proveedor'

    name = fields.Char('Nif', required = True, size=9)
    nombre = fields.Char(string='Nombre', required = True)
    direccion = fields.Text('Direccion', required = True)
    telefono = fields.Integer('Telefono', required = True, size=9)

    producto_ids = fields.One2many('empresa.producto', 'proveedor_id', string='proveedor-producto')


    @api.constrains('telefono')
    def _check_value(self):
        if self.telefono < 600000000 or self.telefono > 700000000:
            raise ValidationError('Debe empezar por 6 o 7 y tener longitud 9')