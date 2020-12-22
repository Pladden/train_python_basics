def get_moldovan_contacts(contacts):
	moldovan_contacts = {}
	for k in contacts:
		v = contacts[k]
		if v.startswith('+373'):
			moldovan_contacts[k] = v
	return moldovan_contacts