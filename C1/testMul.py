from urm.engine import program, run

prgm = program("mul.urm")
for ic in range(0, 10):
    for jc in range(0, 10):
        print("{} * {} = {}".format(ic, jc, run(prgm, ic, jc)))

