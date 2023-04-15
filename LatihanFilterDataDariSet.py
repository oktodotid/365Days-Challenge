name = [{'name': 'okto', 'umur': '24', 'jurusan': 'teknik mesin'},
        {'name': 'capung', 'umur': '24', 'jurusan': 'teknik informatika'},
        {'name': 'bokis', 'umur': '24', 'jurusan': 'teknik ngocok'}]


def filter_name(name, search):
    def iterator(x):
        for v in x.values():
            if search in v:
                return True
        return False
    return filter(iterator, name)


hasil = filter_name(name, 'ngocok')

print(list(hasil))
