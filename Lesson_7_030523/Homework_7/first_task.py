exchange_rate = 28.0

with open('test_file.csv') as us_salary_doc:
    header = us_salary_doc.readline().strip()
    output_header = header.replace('(USD)', '(UAH)')
    output_rows = [output_header]
    for line in us_salary_doc:
        columns = line.strip().split(',')
        employee = columns[0]
        salary_uah = [str(round(float(s) * exchange_rate)) for s in columns[1:]]
        output_row = ','.join([employee] + salary_uah)
        output_rows.append(output_row)

with open('salaries_uah.csv', 'w') as outfile:
    outfile.write('\n'.join(output_rows))
