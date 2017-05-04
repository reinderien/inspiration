* Implement these algos:
   * GrayRecurse
   * GrayLoop
   * HeapRecurse
   * HeapLoop
   * GrayHeapRecurse
   * GrayHeapLoop
* See if GrayRecurse can have some of its recursion cut off
* Profiling graphs of:
   * Violin plot - horz n, subhorz density, vert time, for each algo, all or sampled inputs
     * superimposed or separate boxplot
   * Graph of #iterations before finding first soln over all algos
   * Violin plot - horz n, subhorz density, vert soln density (#solns/given inputs)
     * superimposed or separate boxplot
* Choose multithreading and SIMD libraries. My CPU: 
  * Name: Intel(R) Core(TM) i7-4578U CPU @ 3.00GHz (family: 0x6, model: 0x45, stepping: 0x1)
  * Cores = 2
  * [AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#Advanced_Vector_Extensions_2)
    means 256-bit-wide vector extensions.
  * [SSE4.2](https://en.wikipedia.org/wiki/SSE4#SSE4.2) means ...?
  * Mfg link: [Core i7 4578U](http://ark.intel.com/products/83506)
  * [Haswell-ULT Architecture](https://en.wikipedia.org/wiki/Haswell_(microarchitecture))
  
  