import codecs

for file_name in ['D_MEGA.HTM']:
    source_file = 'raw/{}'.format(file_name)
    dest_file = 'normalized/{}'.format(file_name)

    with codecs.open(source_file, "r",encoding='utf-8', errors='ignore') as fdata:
        html = fdata.read()

    with open(dest_file, 'w') as outfile:
        outfile.write(html)
