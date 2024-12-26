import json


def get_property_code_desc_map(property):
    property_desc_map = {}
    pid = property["iid"]
    property_desc = property["description"]
    if "value-list" in property:
        value_list = property["value-list"]
        for value in value_list:
            k = pid + "." + value["value"]
            v = property_desc + "," + value["description"]
            property_desc_map[k] = v
    else:
        k = pid
        v = property_desc
        property_desc_map[k] = v

    return property_desc_map


def loop_property_list(property_list):
    property_id_values_map = {}
    for property in property_list:
        property_desc_map = get_property_code_desc_map(property)
        property_id_values_map[property["iid"]] = property_desc_map

    return property_id_values_map


def get_event_detail_desc(event):
    desc = event['']


def main():
    with open("/Users/xixiaoyong/Downloads/spec.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            spec_arr = line.split("\t")
            model_name = spec_arr[0]
            spec_json = json.loads(spec_arr[1])
            desc = spec_json["description"]
            service_list = spec_json["services"]
            for service_item in service_list:
                if "events" in service_item:
                    event_list = service_item["events"]
                    property_id_values_map = loop_property_list(service_item["properties"])
                    for event in event_list:
                        record = get_event_detail_desc(event,property_id_values_map)
                    
                    


if __name__ == "__main__":
    main()
