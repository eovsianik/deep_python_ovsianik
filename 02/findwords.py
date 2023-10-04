import json


def parse_json(
    json_str: str, required_fields=None, keywords=None, keyword_callback=None
):
    if keyword_callback is not None:
        available_dict = json.loads(json_str)
        if required_fields is None:
            required_fields = list(available_dict.keys())
        for field in required_fields:
            if field in available_dict.keys():
                all_words = list(available_dict[field].split())
                if keywords is not None:
                    for keyword in keywords:
                        for all_w in all_words:
                            if keyword.lower() == all_w.lower():
                                keyword_callback(field, all_w)
                else:
                    for all_w in all_words:
                        keyword_callback(field, all_w)
