from configparser import ConfigParser

def config(file = 'database.ini', section='postgresql'):
    parser = ConfigParser();
    parser.read(file)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('No section found mataching that file'.format(section,filename))
    return db