import lxml.etree as et
from Evtx.Evtx import Evtx
from eventcodes import EVENT_CODES

with Evtx('WindowsEvents.evtx') as ev:
    for i, rec in enumerate(ev.records(), 1):  # loop over records

        xml_element = rec.lxml()  # get lxml Element obj
        ns = xml_element.nsmap    # get XML namespace
        # Dump XML of entire record:
        # print(et.tostring(xml_element, pretty_print=True).decode())
        # print("-" * 60)
        # if i == 10:
        #     break
        # continue
        event_id = xml_element.findtext('.//EventID', namespaces=ns)
        if event_id == "10016":
            continue

        print(f"Record {i}:")

        execution_element = xml_element.find('.//Execution', namespaces=ns)
        if execution_element is not None:
            process_id = execution_element.get('ProcessID')
        else:
            process_id = 'N/A'
        print("\tProcess ID:", process_id)

        computer = xml_element.findtext('.//Computer', namespaces=ns)
        print("\tComputer:", computer)
        record_id = xml_element.findtext('.//EventRecordID', namespaces=ns)
        print("\tRecord ID:", record_id)
        time_created_element = xml_element.find('.//TimeCreated', namespaces=ns)
        if time_created_element is not None:
            system_time = time_created_element.get('SystemTime')
        else:
            system_time = 'N/A'
        print("\tSystem time:", system_time)
        print("\tEvent ID:", event_id)
        if event_id in EVENT_CODES:
            print("\t\t{}".format(EVENT_CODES[event_id]))
        print()
