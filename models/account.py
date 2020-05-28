# -*- encoding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.exceptions import Warning

from datetime import datetime
from lxml import etree
import base64
import logging
import zeep

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    firma_fel = fields.Char('Firma FEL', copy=False)
    serie_fel = fields.Char('Serie FEL', copy=False)
    numero_fel = fields.Char('Numero FEL', copy=False)
    factura_original_id = fields.Many2one('account.invoice', string="Factura original FEL")
    consignatario_fel = fields.Many2one('res.partner', string="Consignatario o Destinatario FEL")
    comprador_fel = fields.Many2one('res.partner', string="Comprador FEL")
    exportador_fel = fields.Many2one('res.partner', string="Exportador FEL")
    incoterm_fel = fields.Char(string="Incoterm FEL")
    pdf_fel = fields.Binary('PDF FEL', copy=False)
    pdf_fel_name = fields.Char('Nombre PDF FEL', default='pdf_fel.pdf', size=32)
    documento_xml_fel = fields.Binary('Documento xml FEL', copy=False)
    documento_xml_fel_name = fields.Char('Nombre doc xml FEL', default='documento_xml_fel.xml', size=32)
    resultado_xml_fel = fields.Binary('Resultado xml FEL', copy=False)
    resultado_xml_fel_name = fields.Char('Resultado doc xml FEL', default='resultado_xml_fel.xml', size=32)

    def invoice_validate(self):
        for factura in self:
            if factura.journal_id.generar_fel and not factura.firma_fel:

                stdTWS = etree.Element("stdTWS", xmlns="FEL")

                TrnEstNum = etree.SubElement(stdTWS, "TrnEstNum")
                TrnEstNum.text = factura.journal_id.codigo_establecimiento_fel
                TipTrnCod = etree.SubElement(stdTWS, "TipTrnCod")
                TipTrnCod.text = factura.journal_id.tipo_documento_fel
                TrnNum = etree.SubElement(stdTWS, "TrnNum")
                TrnNum.text = str(factura.id)
                TrnFec = etree.SubElement(stdTWS, "TrnFec")
                TrnFec.text = str(factura.date_invoice)
                MonCod = etree.SubElement(stdTWS, "MonCod")
                MonCod.text = "GTQ"
                TrnBenConNIT = etree.SubElement(stdTWS, "TrnBenConNIT")
                TrnBenConNIT.text = factura.partner_id.vat.replace('-', '') or ''
                TrnFec = etree.SubElement(stdTWS, "TrnExp")
                TrnFec.text = "1" if factura.tipo_gasto == "importacion" else "0"
                TrnFec = etree.SubElement(stdTWS, "TrnExento")
                TrnFec.text = "0"
                TrnFec = etree.SubElement(stdTWS, "TrnFraseTipo")
                TrnFec.text = "0"
                TrnFec = etree.SubElement(stdTWS, "TrnEscCod")
                TrnFec.text = "1" if factura.tipo_gasto == "importacion" else "0"
                TrnEFACECliCod = etree.SubElement(stdTWS, "TrnEFACECliCod")
                TrnEFACECliNom = etree.SubElement(stdTWS, "TrnEFACECliNom")
                TrnEFACECliNom.text = factura.partner_id.name
                TrnEFACECliDir = etree.SubElement(stdTWS, "TrnEFACECliDir")
                TrnEFACECliDir.text = factura.partner_id.street or ''
                TrnObs = etree.SubElement(stdTWS, "TrnObs")
                TrnEMail = etree.SubElement(stdTWS, "TrnEmail")
                if factura.partner_id.email:
                    TrnEMail.text = factura.partner_id.email
                TrnCampAd01 = etree.SubElement(stdTWS, "TrnCampAd01")
                TrnCampAd02 = etree.SubElement(stdTWS, "TrnCampAd02")
                TrnCampAd03 = etree.SubElement(stdTWS, "TrnCampAd03")
                TrnCampAd04 = etree.SubElement(stdTWS, "TrnCampAd04")
                TrnCampAd05 = etree.SubElement(stdTWS, "TrnCampAd05")
                TrnCampAd06 = etree.SubElement(stdTWS, "TrnCampAd06")
                TrnCampAd07 = etree.SubElement(stdTWS, "TrnCampAd07")
                TrnCampAd08 = etree.SubElement(stdTWS, "TrnCampAd08")
                TrnCampAd09 = etree.SubElement(stdTWS, "TrnCampAd09")
                TrnCampAd10 = etree.SubElement(stdTWS, "TrnCampAd10")
                TrnCampAd11 = etree.SubElement(stdTWS, "TrnCampAd11")
                TrnCampAd12 = etree.SubElement(stdTWS, "TrnCampAd12")
                TrnCampAd13 = etree.SubElement(stdTWS, "TrnCampAd13")
                TrnCampAd14 = etree.SubElement(stdTWS, "TrnCampAd14")
                TrnCampAd15 = etree.SubElement(stdTWS, "TrnCampAd15")
                TrnCampAd16 = etree.SubElement(stdTWS, "TrnCampAd16")
                TrnCampAd17 = etree.SubElement(stdTWS, "TrnCampAd17")
                TrnCampAd18 = etree.SubElement(stdTWS, "TrnCampAd18")
                TrnCampAd19 = etree.SubElement(stdTWS, "TrnCampAd19")
                TrnCampAd20 = etree.SubElement(stdTWS, "TrnCampAd20")
                TrnCampAd21 = etree.SubElement(stdTWS, "TrnCampAd21")
                TrnCampAd22 = etree.SubElement(stdTWS, "TrnCampAd22")
                TrnCampAd23 = etree.SubElement(stdTWS, "TrnCampAd23")
                TrnCampAd24 = etree.SubElement(stdTWS, "TrnCampAd24")
                TrnCampAd25 = etree.SubElement(stdTWS, "TrnCampAd25")
                TrnCampAd26 = etree.SubElement(stdTWS, "TrnCampAd26")
                TrnCampAd27 = etree.SubElement(stdTWS, "TrnCampAd27")
                TrnCampAd28 = etree.SubElement(stdTWS, "TrnCampAd28")
                TrnCampAd29 = etree.SubElement(stdTWS, "TrnCampAd29")
                TrnCampAd30 = etree.SubElement(stdTWS, "TrnCampAd30")
                
                stdTWSD = etree.SubElement(stdTWS, "stdTWSD")

                num = 1
                for linea in factura.invoice_line:
                    stdTWSDIt = etree.SubElement(stdTWSD, "stdTWS.stdTWSCIt.stdTWSDIt")

                    TrnLiNum = etree.SubElement(stdTWSDIt, "TrnLiNum")
                    TrnLiNum.text = str(num)
                    num += 1
                    TrnArtCod = etree.SubElement(stdTWSDIt, "TrnArtCod")
                    if linea.product_id.default_code:
                        TrnArtCod.text = linea.product_id.default_code
                    else:
                        TrnArtCod.text = str(linea.product_id.id)
                    TrnArtNom = etree.SubElement(stdTWSDIt, "TrnArtNom")
                    TrnArtNom.text = linea.name
                    TrnCan = etree.SubElement(stdTWSDIt, "TrnCan")
                    TrnCan.text = str(linea.quantity)
                    TrnVUn = etree.SubElement(stdTWSDIt, "TrnVUn")
                    TrnVUn.text = str(linea.price_unit)
                    TrnUniMed = etree.SubElement(stdTWSDIt, "TrnUniMed")
                    TrnUniMed.text = "UNIDAD"
                    TrnVDes = etree.SubElement(stdTWSDIt, "TrnVDes")
                    TrnVDes.text = str(( linea.price_unit * linea.quantity ) *  ( linea.discount / 100 ) )
                    TrnArtBienSer = etree.SubElement(stdTWSDIt, "TrnArtBienSer")
                    if linea.product_id.type == 'product':
                        TrnArtBienSer.text = "B"
                    else:
                        TrnArtBienSer.text = "S"
                    TrnArtImpAdiCod = etree.SubElement(stdTWSDIt, "TrnArtImpAdiCod")
                    TrnArtImpAdiCod.text = "0"
                    TrnArtImpAdiUniGrav = etree.SubElement(stdTWSDIt, "TrnArtImpAdiUniGrav")
                    TrnArtImpAdiUniGrav.text = "0"
                    TrnDetCampAd01 = etree.SubElement(stdTWSDIt, "TrnDetCampAdi01")
                    TrnDetCampAd02 = etree.SubElement(stdTWSDIt, "TrnDetCampAdi02")
                    TrnDetCampAd03 = etree.SubElement(stdTWSDIt, "TrnDetCampAdi03")
                    TrnDetCampAd04 = etree.SubElement(stdTWSDIt, "TrnDetCampAdi04")
                    TrnDetCampAd05 = etree.SubElement(stdTWSDIt, "TrnDetCampAdi05")

                if factura.journal_id.tipo_documento_fel == "FCAM":
                    stdTWSCam = etree.SubElement(stdTWS, "stdTWSCam")
                    stdTWSCamIt = etree.SubElement(stdTWSCam, "stdTWS.stdTWSCam.stdTWSCamIt")
                    TrnAbonoNum = etree.SubElement(stdTWSCamIt, "TrnAbonoNum")
                    TrnAbonoNum.text = "1"
                    TrnAbonoFecVen = etree.SubElement(stdTWSCamIt, "TrnAbonoFecVen")
                    TrnAbonoFecVen.text = str(factura.date_due)
                    TrnAbonoMonto = etree.SubElement(stdTWSCamIt, "TrnAbonoMonto")
                    TrnAbonoMonto.text = str(factura.amount_total)

                xmls = etree.tostring(stdTWS, xml_declaration=True, encoding="UTF-8")
                logging.warn(xmls.decode('utf8'))

                wsdl = "http://pruebas.ecofactura.com.gt:8080/fel/adocumento?wsdl"
                if factura.company_id.pruebas_fel:
                    wsdl = "http://pruebas.ecofactura.com.gt:8080/fel/adocumento?wsdl"
                client = zeep.Client(wsdl=wsdl)

                logging.warn(factura.company_id.vat)
                resultado = client.service.Execute(factura.company_id.vat, factura.company_id.usuario_fel, factura.company_id.clave_fel, factura.company_id.vat, xmls)
                logging.warn(resultado)
                resultadoBytes = bytes(bytearray(resultado, encoding='utf-8'))
                resultadoXML = etree.XML(resultadoBytes)

                if resultadoXML.xpath("/DTE"):
                    dte = resultadoXML.xpath("/DTE")
                    factura.firma_fel = dte[0].get("NumeroAutorizacion")
                    factura.serie_fel = dte[0].get("Serie")
                    factura.numero_fel = dte[0].get("Numero")
                    factura.documento_xml_fel = base64.b64encode(xmls)
                    factura.pdf_fel = resultadoXML.xpath("/DTE/Pdf")[0].text
                    factura.resultado_xml_fel = resultadoXML.xpath("/DTE/Xml")[0].text
                else:
                    raise Warning(resultado)

        return super(AccountInvoice, self).invoice_validate()

class AccountJournal(models.Model):
    _inherit = "account.journal"

    generar_fel = fields.Boolean('Generar FEL')
    codigo_establecimiento_fel = fields.Char('Numero Establecimiento FEL')
    tipo_documento_fel = fields.Selection([('FACT', 'FACT'), ('FCAM', 'FCAM'), ('FPEQ', 'FPEQ'), ('FCAP', 'FCAP'), ('FESP', 'FESP'), ('NABN', 'NABN'), ('RDON', 'RDON'), ('RECI', 'RECI'), ('NDEB', 'NDEB'), ('NCRE', 'NCRE')], 'Tipo de Documento FEL',)

class ResCompany(models.Model):
    _inherit = "res.company"

    usuario_fel = fields.Char('Usuario FEL')
    clave_fel = fields.Char('Clave FEL')
    pruebas_fel = fields.Boolean('Pruebas FEL')
