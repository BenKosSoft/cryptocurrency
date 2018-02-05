"""
    Created by mbenlioglu & mertkosan on 12/20/2017
"""
from signature import DSA
from random import randint

_SERIAL_NO_LOWER = 1 << 127
_SERIAL_NO_UPPER = (1 << 128) - 1

_SATOSHI_LOWER = 10
_SATOSHI_UPPER = 500


def gen_tx_block(p, q, g, count, filename=None):
    transaction = ""
    for _ in range(count):
        signed_part = ""
        signed_part += "*** Bitcoin transaction ***\n"
        signed_part += "Serial number: " + str(randint(_SERIAL_NO_LOWER, _SERIAL_NO_UPPER)) + "\n"
        signed_part += "p: " + str(p) + "\n"
        signed_part += "q: " + str(q) + "\n"
        signed_part += "g: " + str(g) + "\n"
        alpha_payer, beta_payer = DSA.key_gen(p, q, g, write_file=False)
        alpha_payee, beta_payee = DSA.key_gen(p, q, g, write_file=False)
        signed_part += "Payer Public Key (beta): " + str(beta_payer) + "\n"
        signed_part += "Payee Public Key (beta): " + str(beta_payee) + "\n"
        signed_part += "Amount: " + str(randint(_SATOSHI_LOWER, _SATOSHI_UPPER)) + " Satoshi\n"
        r, s = DSA.sign_gen(signed_part, p, q, g, alpha_payer, beta_payer)
        transaction += signed_part + "Signature (r): " + str(r) + "\n"
        transaction += "Signature (s): " + str(s) + "\n"

    # write to file
    if filename is not None:
        with open(filename, "wb") as tbf:
            tbf.write(transaction)
            tbf.flush()
    return transaction
