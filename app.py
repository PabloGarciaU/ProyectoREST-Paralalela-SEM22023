from flask import Flask, jsonify

app = Flask(__name__)

from products import products

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message" : "Pong!"}), 200

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": products, "message": "Product list"}), 200

@app.route('/products/<string:product_name>', methods=['GET'])
def get_product(product_name):
    products_found = [product for product in products if product['name'] == product_name]
    if (len(products_found) > 0):
        return jsonify({"product": products_found[0]}), 200
    return jsonify({"message": "Product not found"}), 404

@app.route('/products', methods=['POST']) 
def addProduct():
    new_product = {
        "name": "diuca",
        "price": 800,
        "quantity": 4
    }
    products.append(new_product)
    return jsonify({"message": "Product added successfully", "products": products}), 200

@app.route('/products/<string:product_name>', methods=['PUT']) 
def editProduct(product_name):
    product_found = [product for product in products if product['name'] == product_name]
    if (len(product_found) > 0):
        product_found[0]['name'] = request.json['name']
        product_found[0]['price'] = request.json['price']
        product_found[0]['quantity'] = request.json['quantity']
        return jsonify({"message": "Product updated", "product": product_found[0]}), 200
    return jsonify({"message": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)