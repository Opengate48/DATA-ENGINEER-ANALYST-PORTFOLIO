import re


def stat_from_list(text):
    result = []
    name_list = []
    for name in text:
        first_name = name.split(" ")[1]
        name_list.append(first_name)
    only_uniq_names = []
    for first_name in name_list:
        cnt = 0
        if (first_name in only_uniq_names):
            continue
        for first_name2 in name_list:
            if (first_name2 == first_name):
                cnt += 1
        only_uniq_names.append(first_name)
        result.append((cnt, first_name))
    result.sort(reverse=True)
    for i in range(len(result)):
        freq = result[i][0]
        first_name = result[i][1]
        result[i] = (first_name, freq)
    return result


def get_female_list(listik):
    female_list = []
    for name in listik:
        full_name = name.split(" ")
        second_name = full_name[0]
        first_name = full_name[1]
        s_name_suf = second_name[-3:]
        f_name_suf = first_name[-1:]
        if (
            s_name_suf == "ина"
            or s_name_suf == "ова"
            or s_name_suf == "ева"
            or s_name_suf == "ман"
            or s_name_suf == "ачи"
            or s_name_suf == "нок"
            or s_name_suf == "вич"
            or s_name_suf == "ных"
            or s_name_suf == "кая"
            or s_name_suf == "ван"
            or s_name_suf == "нко"
            or s_name_suf == "ёва"
            or s_name_suf == "кер"
            or s_name_suf == "арь"
            or s_name_suf == "лая"
            or s_name_suf == "йко"
        ) and (f_name_suf == "а" or f_name_suf == "я" or f_name_suf == "ь"):
            female_list.append(name)
    return female_list


def get_male_list(listik):
    male_list = []
    for name in listik:
        full_name = name.split(" ")
        second_name = full_name[0]
        first_name = full_name[1]
        s_name_suf = second_name[-3:]
        f_name_suf = first_name[-1:]
        if not (
            (
                s_name_suf == "ина"
                or s_name_suf == "ова"
                or s_name_suf == "ева"
                or s_name_suf == "ман"
                or s_name_suf == "ачи"
                or s_name_suf == "нок"
                or s_name_suf == "вич"
                or s_name_suf == "ных"
                or s_name_suf == "кая"
                or s_name_suf == "ван"
                or s_name_suf == "нко"
                or s_name_suf == "ёва"
                or s_name_suf == "кер"
                or s_name_suf == "арь"
                or s_name_suf == "лая"
                or s_name_suf == "йко"
            )
            and (f_name_suf == "а" or f_name_suf == "я" or f_name_suf == "ь")
        ):
            male_list.append(name)
    return male_list


def make_stat(filename):
    with open(filename, encoding="cp1251") as file:
        text = file.read()
    yrs_in_pg = re.findall('<h3>(\\d\\d\\d\\d)</h3>', text)
    lists_by_years = re.findall('\\d\\d\\d\\d</h3>[\\d\\w\\W\\D_]*?<h3>', text)
    lists_by_years.append(
        re.search(
            f"<h3>{yrs_in_pg[len(yrs_in_pg) - 1]}[\\d\\w\\W_]*?</center>", text
        )[0]
    )
    stat = []
    full_list = re.findall('<a.*>(.*)</a>', text)
    for list_by_year in lists_by_years:
        stat.append(re.findall('<a.*>(.*)</a>', str(list_by_year)))
    stat = list(reversed(stat))
    stat.append(list(reversed(yrs_in_pg)))
    stat.insert(0, full_list)
    return stat
    pass


def extract_years(stat):
    return stat[len(stat) - 1]
    pass


def extract_general(stat):
    return stat_from_list(stat[0])
    pass


def extract_general_male(stat):
    return stat_from_list(get_male_list(stat[0]))

    pass


def extract_general_female(stat):
    return stat_from_list(get_female_list(stat[0]))
    pass


def extract_year(stat, year):
    year = int(year)
    return stat_from_list(stat[year - 2003])
    pass


def extract_year_male(stat, year):
    year = int(year)
    return stat_from_list(get_male_list(stat[year - 2003]))
    pass


def extract_year_female(stat, year):
    year = int(year)
    return stat_from_list(get_female_list(stat[year - 2003]))
    pass


if __name__ == '__main__':
    pass
