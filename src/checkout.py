def _item_category(item):
    if item["qty"] <= 0:
        return "empty"
    if item["price"] > 100:
        return "big"
    if item["price"] > 50:
        return "medium"
    return "small"


def process_orders(orders):
    results = []
    for order in orders:
        status = order["status"]
        if status == "paid":
            results.extend(_item_category(item) for item in order["items"])
        elif status == "pending":
            if order["items"] and order["urgent"]:
                results.append("rush")
        else:
            results.append("skip")
    return results


def order_total(items):
    return sum(item["qty"] * item["price"] for item in items)
