import logging
from odoo.upgrade import util

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    util.records.remove_view(cr, xml_id="fel_ecofactura.account_move_form_fel_ecofacturas")
    util.records.remove_view(cr, xml_id="fel_ecofactura.journal_form_gface_ecofacturas")
    util.records.remove_view(cr, xml_id="fel_ecofactura.view_company_form_fel_ecofacturas")
    _logger.info("Vistas viejas borradas")
