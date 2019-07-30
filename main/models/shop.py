from .base import db, Base

class Shop(Base):
    __tablename__ = "shop"

    shop_name = db.Column(db.String(50), default="")
    tel = db.Column(db.String(50), default="")
    address = db.Column(db.String(200), default="")
    description = db.Column(db.String(255), default="")
