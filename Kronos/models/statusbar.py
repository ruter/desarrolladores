from odoo import models,api,fields

class statusbar(models.Model):

    _name = 'statusbar.statusbar'
    name = fields.Char('Name',requered=True)

    state = fields.Selection([('Basica','Información Basica'),
    ('Tecnica','Información Tecnica'),('Cuantitativas','Caracteristicas Cuantitativas'),
    ('Diseño','Caracteristicas de Diseño'),('Ruta','Ruta de Proceso')],default='Basica')

    referencia_supra = fields.Selection([('prueba','prueba')],string='Referencia Suprapak')

    #This function is triggered when the user clicks on the button 'Set to concept'
    def informacion_basica(self):
        self.write({
            'state': 'Basica',
        })

#This function is triggered when the user clicks on the button 'Set to started'
    def informacion_tecnica(self):
        self.write({
	        'state': 'Tecnica'
        })

#This function is triggered when the user clicks on the button 'In progress'
    def caracteristicas_cuantitativas(self):
        self.write({
	        'state': 'Cuantitativas'
        })

#This function is triggered when the user clicks on the button 'Done'
    def caracteristicas_de_diseño(self):
        self.write({
	        'state': 'Diseño',
        })

    def ruta_de_proceso(self):
        self.write({
            'state': 'Ruta',
        })



