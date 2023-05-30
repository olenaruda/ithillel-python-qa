#  NOTES
import argparse
import self as self


class UrlAnalyzer:

    def __new__(cls, *args, **kwargs):
        analyzer = super().__new__(cls)
        if not args and not kwargs:
            analyzer.url = cls.user_input
            analyzer.count = 8
        return analyzer

    def __init__(self, url=None):
        if url:
            self.url = url
        self.link_analyzer = LinkAnalyzer(self.url)

    @classmethod
    def user_input(cls):
        parse = argparse.ArgumentParser()
        parse.add_argument('-url', help='Please set url for parsing')
        args = parse.parse_args()
        if args.url:
            return args.url
        else:
            url = input('Please set url for parsing')
            return url

    def info_from_link(self, url):
        self.link_analyzer.check_link(url)

    def get_links_from_url(self, url) -> list:
        return re.findall('', url)



class LinkAnalyzer:

    def __init__(self, url):
        self.url = url

    def check_link(self, link):
        pass

    def check_links(self, links):
        for link in links:
            self.check_link(link)

#
# if __name__ == "__main__":
#     # url = UrlAnalyzer('www.google.com')
#     url_1 = UrlAnalyzer()


# def user_input():
#     parse = argparse.ArgumentParser()
#     parse.add_argument('-url', help='')
#     args = parse.parse_args()
#     print(args.url)

#_________________________________________________________________________________________________________________

# class A:
#
#     def __init__(self, name):
#         self.name = name
#
#
# a = A('Joe')
# print(a.name)
#
# a.name = "Marta"
# print(a.name)
#
# a.last_name = 'Tomas'
# print(a.last_name)


#_________________________________________________________________________________________________________________

# Регулярні вирази - шаблони для пошуку фрагменту тексту

import re

# pattern = 'This'
# my_string = 'This is my text. Text is good'
#
# result = re.match(pattern, my_string)
# print(result.regs)

# ----

# date_string = '12.12.2020'
#
# date_format = r'^[\d.-]+$'
#
# result_2 = re.match(date_format, date_string)
# print(result_2.regs)

# # --
# phone_string = '(099)-333-33-33'
#
# phone_format = r'^[\d+\-()]+$'
#
# result_3 = re.match(phone_format, phone_string)
# print(result_3)
# print(result_3.regs)

# ----
# pattern = 'This'
# my_string = 'This is my text. text is good (099)-333-33-33'
# phone_format = r'[\d+\-()]+$'
#
# search_result = re.search(phone_format, my_string)
# print(search_result)
# # <re.Match object; span=(30, 45), match='(099)-333-33-33'>
#
# find_all_result = re.findall('text', my_string)
# print(find_all_result)
#
# result_split = re.split('is', my_string, maxsplit=1)
# print(result_split)
#
# result_sub = re.sub('text', 'python', my_string)
# print(result_sub)

# ---

match_result = re.match(r'^[a-z0-9A-Z_-]{6-16}$', 'aSdcs_d-4dawd')
print(match_result)


# python main.py -a=5 -b=7 -c=1