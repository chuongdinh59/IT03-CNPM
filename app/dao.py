import  json
import  os
from app import app


def load_cate():
    with open(os.path.join(app.root_path, 'data/categories.json'), encoding='utf-8') as f:
        return json.load(f)
def load_product(cate_id = None):
    with open(os.path.join(app.root_path, 'data/product.json'), encoding='utf-8') as f:
        products = json.load(f)
    if cate_id:
        products = [p for p in products if p['category_id'] == int(cate_id)]
    return products