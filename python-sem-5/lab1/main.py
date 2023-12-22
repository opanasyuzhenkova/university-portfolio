import tests

from package import precision as pr
from package import input_print as ip
from package import log as l
from package import calculate as cl

# from  math import sqrt


def call():
    args = ip.input_args()
    # print(args)
    r = cl.calculate(*args)

    res = pr.output(r)
    ip.print_results(args[0], args[1], args[2], res)
    l.write_log(args[0], args[1], action=args[2], result=res)


call()
tests.all_tests()
