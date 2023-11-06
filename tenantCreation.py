from acitoolkit.acitoolkit import *

tenant = Tenant("OXXO-Test")
description = "Testing"

creds= Credentials('apic', description)
creds.add_argument('--delete', action = 'store_true',
	help='delete the config from the apic')
args = creds.get()

if args.delete:
	tenant.mark_as_deleted()

session = Session(args.url, args.login, args.password)
session.login()
resp = tenant.push_to_apic(session)
if resp.ok:
	print("success!")
print('URL: ', tenant.get_url())
print('JSON: ', tenant.get_json())

