import json

data = json.load(open('sample-data.json', 'r', encoding='utf-8'))
arr = data['imdata']

print('Interface Status')
print('='*80)
print(f"{'DN':<50} {'Description':<20}  {'Speed':<7}  {'MTU':<6}")
print(f"{'-'*50} {'-'*20}  {'-'*6}  {'-'*6}")

for item in arr:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    description = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
