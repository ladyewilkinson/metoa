from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
import datetime
from settings import app

db = SQLAlchemy(app)

class ArtObject(db.Model):
    __tablename__ = 'artobjects'
    id = db.Column(db.Integer, primary_key = True)
    is_highlight = db.Column(db.Boolean)
    accession_number = db.Column(db.String(64))
    is_public_domain = db.Column(db.Boolean)
    primary_image = db.Column(db.String(255))
    name = db.Column(db.String(255))
    culture = db.Column(db.String(255))
    object_date = db.Column(db.String(255))
    metadata_date = db.Column(db.DateTime)

    def json(self):
        return {
            'id': self.id,
            'is_highlight': self.is_highlight,
            'accession_number': self.accession_number,
            'is_public_domain': self.is_public_domain,
            'primary_image': self.primary_image,
            'name': self.name,
            'culture': self.culture,
            'object_date': self.object_date,
            'metadata_date': repr(self.metadata_date)
        }

    def add(_id,_ih,_an,_ipd,_pi,_name,_cul,_od,_md):
        new_art_object = ArtObject(id=_id,
                                   is_highlight=_ih,
                                   accession_number = _an,
                                   is_public_domain = _ipd,
                                   primary_image = _pi,
                                   name = _name,
                                   culture = _cul,
                                   object_date = _od,
                                   metadata_date = _md)
        db.session.add(new_art_object)
        db.session.commit()

    def get_all():
        return [ArtObject.json(ao) for ao in ArtObject.query.all()]

    def get_all_ids():
        return [ao.id for ao in ArtObject.query.all()]

    def exists(_id):
        return _id in [ao.id for ao in ArtObject.query.all()]

    def get(_id):
        ao = ArtObject.query.get(_id)
        return(ArtObject.json(ao))

    def delete(_id):
        ArtObject.query.filter_by(id=_id).delete()
        db.session.commit()

    def __repr__(self):
        art_object_object = {
            'id': self.id,
            'is_highlight': self.is_highlight,
            'accession_number': self.accession_number,
            'is_public_domain': self.is_public_domain,
            'primary_image': self.primary_image,
            'name': self.name,
            'culture': self.culture,
            'object_date': self.object_date,
            'metadata_date': repr(self.metadata_date)
        }
        return json.dumps(art_object_object)