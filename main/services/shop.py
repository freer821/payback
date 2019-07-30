from ..models.shop import Shop
from ..utils.http_helper import getresponsemsg

def get_shop_list():
    shops = Shop.query.all()
    shops_array = []
    for s in shops:
        shops_array.append(s.to_dict())

    return getresponsemsg(200, shops_array)
