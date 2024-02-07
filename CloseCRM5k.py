from closeio_api import Client

api_key = "api_56jHdTycRKafCDuj5pAbId.22x40ffVNYjxSGNwVgA8aK"

# създаваме клиент
client = Client(api_key)


# функция за ъпдейтване на стойността на валюто
def update_opportunity_value(opportunity_id, value):
    client.put(f'opportunity/{opportunity_id}/', {'value': value})


# Фетчваме всички лийдове
def get_all_leads():
    all_leads = []
    next_url = 'lead'
    while next_url:
        response = client.get(next_url)
        leads_data = response.get('data', [])
        all_leads.extend(leads_data)
        next_url = response.get('next_page_url')
    return all_leads


# взимаме лийдовете
all_leads = get_all_leads()

# принтваме всички детайли
if all_leads:
    for lead in all_leads:
        lead_id = lead.get('id', 'N/A')
        lead_name = lead.get('name', 'N/A')
        print(f"Lead ID: {lead_id}")

        # взимаме конкретното ъпъртюнити от конкретния лийд
        opportunities = client.get('opportunity/', params={'lead_id': lead_id})
        if 'data' in opportunities:
            opportunities_data = opportunities['data']
            for opportunity in opportunities_data:
                status_type = opportunity.get('status_type', 'N/A')
                if status_type == 'active':
                    opportunity_id = opportunity.get('id', 'N/A')
                    opportunity_value = opportunity.get('value', 'N/A')

                    update_opportunity_value(opportunity_id, 500000)

        else:
            print("No opportunities found for this lead.")
else:
    print("No leads found.")
