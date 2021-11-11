open_file = open('CupcakeInvoices.csv')

for line in open_file:
    print(line)

open_file.close()

open_file = open('CupcakeInvoices.csv')

for line in open_file:
    line_words = line.rstrip('\n').split(',')
    print(line_words[2])

open_file.close()


open_file = open('CupcakeInvoices.csv')

for line in open_file:
    line_words = line.rstrip('\n').split(',')

    quantity = int(line_words[3])
    price = float(line_words[4])

    total_before_rounding = quantity * price
    final_total = round(total_before_rounding,2)
    print(final_total)

open_file.close()

