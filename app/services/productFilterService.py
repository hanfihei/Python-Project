from data.products import products

# products는 더미데이터, filter는 ai가 넘겨준 json자료
def filter_products(products, filters): 
    result = []

    for product in products:
        # 딕셔너리는 .으로 접근 불가능
        if(filters["category"] != ""):
            if (product["category"] != filters["category"]):
                continue
            
        if(filters["weight"] != 0.0):
            if (product["weight"] > filters["weight"]):
                continue
            
        if(filters["price"] != 0):
            if (product["price"] > filters["price"]):
                continue
        
        if filters["tags"]:
            # tags가 하나라도 존재한다면 통과
            if not any(tag in product["tags"] for tag in filters["tags"]):
                continue
                

        result.append(product)
        
    return result