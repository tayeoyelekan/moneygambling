
def data_table_vertical_converter(data_table_raw: str):
    data_table_list = data_table_raw.split("|")
    data_table_list = [elem.strip() for elem in data_table_list]
    data_table_list = list(filter(lambda elem: elem != "", data_table_list))
    return {data_table_list[i]: data_table_list[i + 1] for i in range(0, len(data_table_list) - 1, 2)}


def data_table_horizontal_converter(data_table_raw: str):
    data_table_list = data_table_raw.split("|")
    data_table_list = [elem.strip() for elem in data_table_list]
    data_table_list = list(filter(lambda elem: elem != "", data_table_list))
    return {data_table_list[i]: data_table_list[len(data_table_list) // 2 + i] for i in
            range(0, len(data_table_list) // 2, 1)}


