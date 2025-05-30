from multiprocessing import Pool
from scipy import integrate
import time

def integrant(x: int) -> int:
    return x**2 + 5*(x**(2/4)) + 6*(x**(3/5))

def work(integration_limits: tuple):
    return integrate.quad(integrant, integration_limits[0], integration_limits[1])

def main():
    print("Bez podziału na pod-przediały:")
    start = time.time()
    result_wo_split = work((0, 10000))[0]
    end = time.time()
    t_ms = (end-start)*1000
    print("wynik: ", result_wo_split, "; otrzymano w ", f"{(end-start)*1000:.6}", " ms")

    print("Z podziałem na 10 podprzedziałów:")
    work_pool = Pool(processes=10)
    ranges = [(a, a + 1000) for a in range(0, 10000, 1000)]
    start = time.time()
    results = work_pool.map(work, ranges)
    work_pool.close()
    end = time.time()
    dt = ((end-start)*1000) / t_ms
    result = 0
    for r in results:
        result += r[0]
    print("wynik: ", result, "; otrzymano w ", f"{(end-start)*1000:.6}", " ms")

    print("wsp. przyśpieszenia: ", dt)

if __name__ == "__main__":
    main()