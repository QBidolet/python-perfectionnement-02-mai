# trace permet de suivre l'exécution du code ligne par ligne.
# Il affiche les fonctions exécutées et les fonctions appelées.

import trace


def recursive_function(n):
    if n <= 0:
        return 0
    else:
        return n + recursive_function(n - 1)


tracer = trace.Trace(count=True, trace=True)
tracer.runfunc(recursive_function, 5) # 5 étant l'argument n

results = tracer.results()
results.write_results(coverdir="trace_report", show_missing=True, summary=True)
