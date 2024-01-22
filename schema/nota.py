from ma import ma
from models.nota_fiscal import NotaFiscalModel


class NotaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NotaFiscalModel
        load_instance = True