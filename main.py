from flask import Flask, jsonify
from google.cloud import datastore

app = Flask(__name__)

# Initialize the Datastore client
datastore_client = datastore.Client()

@app.route('/products', methods=['GET'])
def get_products():
    # Fetch products from Google Datastore
    query = datastore_client.query(kind='Product')
    products = list(query.fetch())

    # Convert the Datastore entity objects to dictionaries
    product_list = []
    for product in products:
        product_dict = dict(product)
        product_list.append(product_dict)

    return jsonify(product_list)

if __name__ == '__main__':
    app.run(debug=True)
