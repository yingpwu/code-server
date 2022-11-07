from importlib import resources


def read(name: str) -> str:
    with resources.open_text('demoresouces.text', f'{name}.txt') as f:
        return f.read()


print(read("file"))
print("=" * 40)
print(read("package"))
print("=" * 40)
print(read('resouce'))


import csv


class NotFoundZipcode(Exception):
    ...


def get_zipcode(city: str) -> str:
    with resources.open_text('demoresouces.data', 'zipcode.csv') as res:
        rows = csv.DictReader(res)

        for row in rows:
            if row['city'] == city:
                return row['zipcode']
        raise NotFoundZipcode(f'{city}的邮政编码不存在!')


print(get_zipcode("北京"))
print(get_zipcode("上海"))
print(get_zipcode("大连"))
