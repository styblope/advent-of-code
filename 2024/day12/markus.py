# region is a set of plots, each plot encoded as r+1j*c
# ds stores all unit directions
        
def area(region):
    return len(region)

def perimeter(region):
    return sum(p+d not in region for p in region for d in ds)

def sides(region):
    edges = [(p,d) for p in region for d in ds if p+d not in region]
    return sum((p+1j*d, d) not in edges for p,d in edges)

print("*", sum(area(r)*perimeter(r) for r in regions))
print("**", sum(sides(r)*area(r) for r in regions))
