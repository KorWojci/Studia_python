import enchant

pwl = enchant.request_pwl_dict("slowa.txt")

print(pwl.suggest('swiat'))