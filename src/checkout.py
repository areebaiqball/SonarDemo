def process_orders(orders):
    results = []
    for order in orders:
        if order["status"] == "paid":
            for item in order["items"]:
                if item["qty"] > 0:
                    if item["price"] > 100:
                        results.append("big")
                    elif item["price"] > 50:
                        results.append("medium")
                    else:
                        results.append("small")
                else:
                    results.append("empty")
        elif order["status"] == "pending":
            if order["items"] and order["urgent"]:
                results.append("rush")
        else:
            results.append("skip")
    return results


def order_total(items):
    return sum(item["qty"] * item["price"] for item in items)
