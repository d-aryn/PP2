def convert(grams):
    return grams*28.3495231

grams = 150
ounces = convert(grams)
print(f"You need to take {ounces} ounces")


#A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams