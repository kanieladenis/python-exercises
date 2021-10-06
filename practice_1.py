def handle_commas(s):
    if ',' in s:
        output = s.replace(',', '')
        if output.isdigit():
            print(output)
            return output
        else:
            print('input not digit')
    elif s.isdigit():
        print(s)
        return s
    else:
        print('invalid')
    
handle_commas('1,23a')