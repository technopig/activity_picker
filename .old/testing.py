import hydrofunctions as hf
herring = hf.NWIS('400052105144101', 'dv', period='P55D')
print(herring)
