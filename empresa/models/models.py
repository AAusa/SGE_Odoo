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

from odoo import models, fields, api

#hace falta para _get_annios(self)
from dateutil.relativedelta import *
from datetime import date

class cliente(models.Model):
    _name = 'empresa.cliente'
    _description = 'Características de un cliente'

    dni = fields.Char('Dni', required = True, size=9)
    nombre = fields.Char(string='Nombre', required = True)
    fechaNacimiento = fields.Date('Fecha', required = True, default = fields.Date.today())
    edad = fields.Integer('Edad', required = True, compute='_get_annios') 
    direccion = fields.Text('Direccion', required = True)
    telefono = fields.Char('Telefono', required = True, size=9)#api.constraints

    @api.depends('fechaNacimiento') 
    def _get_annios(self): 
        for cliente in self: 
            hoy = date.today()
            edad.edad = relativedelta(hoy, cliente.fechaNacimiento).years
    
    factura_ids = fields.One2many('empresa.factura', 'cliente_id', string='cliente-factura')


class factura(models.Model):
    _name='empresa.factura'
    _description = 'Características de una factura'

    numFactura = fields.Integer('numFactura', required = True) 
    fechaEmision = fields.Date('fechaEmision', required = True, default = fields.Date.today())
    total = fields.Integer('numFactura', required = True) 
    
    #Campos relacionales
    cliente_id = fields.Many2one('empresa.cliente', string='factura-cliente')
    producto_ids = fields.One2many('empresa.producto', 'factura_id', string='factura-producto')

        
class producto(models.Model):
    _name = 'empresa.producto'
    _description = 'Caracteristicas de un producto'

    identificador = fields.Integer('Identificador', required = True)
    nombre = fields.Char(string='Nombre', required = True)
    descripcion = fields.Text('Descripcion', required = True)
    precio = fields.Float('Precio', (8,2), help='Coste total de producto') # 5 números naturales más 2 decimales
    stock = fields.Integer('Stock', required = True)

    #Campos relacionales
    factura_id = fields.Many2one('empresa.factura', string='producto-factura')
    categoria_id = fields.Many2one('empresa.categoria', string='producto-categoria')
    proveedor_id = fields.Many2one('empresa.proveedor', string='producto-proveedor')


class categoria(models.Model):
    _name = 'empresa.categoria'
    _description = 'empresa.empresa'

    nombre = fields. Selection (string = 'Nombre', selection =[('o','Ordenadores'),('s','Smartphones'),('a','Audiovisual'), ('p','Periféricos'),('t','Televisores'), ('g','Gaming')], default='l')
    
    producto_ids = fields.One2many('empresa.producto', 'categoria_id', string='categoria-producto')

class proveedor(models.Model):
    _name = 'empresa.proveedor'
    _description = 'Características de un proveedor'

    nif = fields.Char('Dni', required = True, size=9)
    nombre = fields.Char(string='Nombre', required = True)
    direccion = fields.Text('Direccion', required = True)
    telefono = fields.Char('Telefono', required = True, size=9)

    producto_ids = fields.One2many('empresa.producto', 'proveedor_id', string='proveedor-producto')
