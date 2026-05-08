from app.services.product_search_service import search_similar_products

if __name__ == "__main__":
    query = "가볍고 저렴한 노트북 추천해줘"

    data = search_similar_products(query)

    for product in data:
        print(product)
