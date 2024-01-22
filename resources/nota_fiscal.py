from flask import request
from flask_restplus import Resource, fields

from models.nota_fiscal import NotaFiscalModel
from schema.nota import  NotaSchema

from server.instance import server

book_ns = server.book_ns

ITEM_NOT_FOUND = "Nota não encontrada"


book_schema = NotaSchema()
nota_list_schema = NotaSchema(many=True)

# Model required by flask_restplus for expect
item = book_ns.model('Book', {
    'title': fields.String('Book title'),
    'pages': fields.Integer(0),
})


class Book(Resource):
    pass

  