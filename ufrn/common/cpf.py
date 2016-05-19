

def cpf_digits(cpf):
    return ''.join(filter(lambda x: x.isdigit(), cpf))


def is_valid(cpf):
    cpf_valido = False
    # Left only digits at cpf
    cpf_aux = cpf_digits(cpf)

    if len(cpf_aux) == 11:
        cpf_valido = True
        # Check for repeat values 00000000000, 11111111111
        cpf_invalidos = [11*str(i) for i in range(10)]
        if cpf not in cpf_invalidos:
            # Get CPF without DV
            cpf_aux = cpf[:9]

            while len(cpf_aux) < 11:
                sum_cpf = 0
                for i in range(0, len(cpf_aux)):
                    sum_cpf += int(cpf_aux[i]) * ((len(cpf_aux) + 1) - i)
                res = sum_cpf % 11

                dig = '0'
                if res > 1:
                    dig = str(11 - res)

                cpf_aux += dig

            cpf_valido = cpf_aux == cpf_digits(cpf)

    return cpf_valido


def format(cpf):
    cpf_aux = cpf_digits(cpf)
    return "%s.%s.%s-%s" % ( cpf_aux[0:3], cpf_aux[3:6], cpf_aux[6:9], cpf_aux[9:11] )
