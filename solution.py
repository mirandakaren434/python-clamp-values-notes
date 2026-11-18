

def solve(value):
    return min(max(value["number"], value["low"]), value["high"]) if value["low"] <= value["high"] else (_ for _ in ()).throw(ValueError("reversed bounds"))
