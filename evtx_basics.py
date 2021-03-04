import lxml.etree as et
from Evtx.Evtx import Evtx

with Evtx('../DATA/WindowsEvents.evtx') as ev:
    for i, rec in enumerate(ev.records(), 1):  # loop over records
        print(f"Record {i}:")

        xml_element = rec.lxml()  # get XML object
        ns = xml_element.nsmap    # get XML namespace
        # Dump XML of entire record:
        # print(et.tostring(xml_element, pretty_print=True).decode())
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
        print()
