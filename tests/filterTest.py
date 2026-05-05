def filter_products(products, filters): 
    result = []

    for product in products:

        if filters["category"] != "":
            if product["category"] != filters["category"]:
                continue
            
        if filters["weight"] != 0.0:
            if product["weight"] > filters["weight"]:
                continue
            
        if filters["price"] != 0:
            if product["price"] > filters["price"]:
                continue

        result.append(product)
        
    return result


if __name__ == "__main__":
    products = [
        {"name": "LG 울트라 슬림", "price": 1300000, "weight": 1.05, "category": "노트북"},
        {"name": "Samsung Galaxy Book Flex", "price": 1800000, "weight": 1.2, "category": "노트북"},
        {"name": "MacBook Air", "price": 1700000, "weight": 1.29, "category": "노트북"},
        {"name": "그램 초경량", "price": 1500000, "weight": 0.99, "category": "노트북"},
        {"name": "아이패드", "price": 900000, "weight": 0.5, "category": "태블릿"}
    ]

    # 테스트 케이스 바꿔가면서 돌려
    filters = {
        "category": "노트북",
        "weight": 1.1,
        "price": 1500000
    }

    result = filter_products(products, filters)

    print("결과:")
    for r in result:
        print(r["name"])