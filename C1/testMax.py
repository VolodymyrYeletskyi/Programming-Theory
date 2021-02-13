from urm.engine import program, run

prgm = program("max.urm")
for ic in range(0, 10):
    for jc in range(0, 10):
        print("Max of {} and {} is {}".format(ic, jc, run(prgm, ic, jc)))

