from app import app
from flask import render_template, request
import  requests
from app import dao
@app.route("/")
def index():
    categories = dao.load_cate()
    cate_id = request.args.get('cate')
    products = dao.load_product(cate_id = cate_id)
    return render_template('index.html', categories = categories, products = products)

@app.route("/products")
def getAllProduct():
    products = dao.load_product()
    return render_template('product.html', products = products)
@app.route("/products/<int:id>")
def getDetail(id):
    products = dao.load_product()
    product = products[id - 1]
    return render_template('product-detail.html', product = product)
if __name__ == '__main__':
    app.run(debug=True)