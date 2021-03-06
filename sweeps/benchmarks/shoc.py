#!/usr/bin/env python
# SHOC benchmark definitions

from datatypes import *
from params import *

bb_gemm = Benchmark("bb_gemm", "bb_gemm")
bb_gemm.set_kernels(["bb_gemm"])
bb_gemm.set_main_id(0x00000140)
bb_gemm.add_array("x", 1024, 4)
bb_gemm.add_array("y", 1024, 4)
bb_gemm.add_array("z", 1024, 4)
bb_gemm.add_loop("bb_gemm", "loopi")
bb_gemm.add_loop("bb_gemm", "loopk")
bb_gemm.add_loop("bb_gemm", "loopj")

fft = Benchmark("fft", "fft")
fft.set_kernels(["fft1D_512"])
fft.set_main_id(0x00000150)
fft.add_array("work_x", 512, 4)
fft.add_array("work_y", 512, 4)
fft.add_array("DATA_x", 512, 4)
fft.add_array("DATA_y", 512, 4)
fft.add_array("data_x", 8, 4)
fft.add_array("data_y", 8, 4)
fft.add_array("smem", 576, 4)
fft.add_array("reversed", 8, 4)
fft.add_array("sin_64", 448, 4)
fft.add_array("cos_64", 448, 4)
fft.add_array("sin_512", 448, 4)
fft.add_array("cos_512", 448, 4)
fft.add_loop("step1", "outer")
fft.add_loop("step1", "load")
fft.add_loop("step1", "twiddles")
fft.add_loop("step1", "store")
fft.add_loop("step2", "outer")
fft.add_loop("step2", "load")
fft.add_loop("step3", "outer")
fft.add_loop("step3", "load")
fft.add_loop("step3", "store")
fft.add_loop("step4", "outer")
fft.add_loop("step4", "load")
fft.add_loop("step5", "outer")
fft.add_loop("step5", "load")
fft.add_loop("step5", "store")
fft.add_loop("step6", "outer")
fft.add_loop("step6", "load")
fft.add_loop("step6", "twiddles")
fft.add_loop("step6", "save")
fft.add_loop("step7", "outer")
fft.add_loop("step7", "load")
fft.add_loop("step8", "outer")
fft.add_loop("step8", "load")
fft.add_loop("step8", "store")
fft.add_loop("step9", "outer")
fft.add_loop("step9", "load")
fft.add_loop("step10", "outer")
fft.add_loop("step10", "load")
fft.add_loop("step10", "store")
fft.add_loop("step11", "outer")
fft.add_loop("step11", "load")
fft.add_loop("step11", "store")

md = Benchmark("md", "md")
md.set_kernels(["md"])
md.set_main_id(0x00000160)
md.add_array("d_force_x", 32, 4)
md.add_array("d_force_y", 32, 4)
md.add_array("d_force_z", 32, 4)
md.add_array("position_x", 32, 4)
md.add_array("position_y", 32, 4)
md.add_array("position_z", 32, 4)
md.add_array("NL", 1024, 4)
md.add_loop("md", "loop_i")
md.add_loop("md", "loop_j")

pp_scan = Benchmark("pp_scan", "pp_scan")
pp_scan.set_kernels(["pp_scan"])
pp_scan.set_main_id(0x00000170)
pp_scan.add_array("bucket", 2048, 4)
pp_scan.add_array("bucket2", 2048, 4)
pp_scan.add_array("sum", 16, 4)
pp_scan.add_loop("sum_scan", "loop2")
pp_scan.add_loop("local_scan", "loop1_outer")
pp_scan.add_loop("local_scan", "loop1_inner")
pp_scan.add_loop("last_step_scan", "loop3_outer")
pp_scan.add_loop("last_step_scan", "loop3_inner")

reduction = Benchmark("reduction", "reduction")
reduction.set_kernels(["reduction"])
reduction.set_main_id(0x00000180)
reduction.add_array("in", 2048, 4)
reduction.add_loop("reduction", "sum")

ss_sort = Benchmark("ss_sort", "ss_sort")
ss_sort.set_kernels(["ss_sort"])
ss_sort.set_main_id(0x00000190)
ss_sort.add_array("a", 2048, 4)
ss_sort.add_array("b", 2048, 4)
ss_sort.add_array("bucket", 2048, 4)
ss_sort.add_array("sum", 128, 4)
ss_sort.add_loop("init", "loop1_outer")
ss_sort.add_loop("hist", "loop2")
ss_sort.add_loop("hist", "loop1")
ss_sort.add_loop("local_scan", "loop1_outer")
ss_sort.add_loop("local_scan", "loop1_inner")
ss_sort.add_loop("sum_scan", "loop2")
ss_sort.add_loop("last_step_scan", "loop3_outer")
ss_sort.add_loop("last_step_scan", "loop3_inner")
ss_sort.add_loop("update", "loop3")
ss_sort.add_loop("update", "loop1")

stencil = Benchmark("stencil", "stencil")
stencil.set_kernels(["stencil"])
stencil.set_main_id(0x000001A0)
stencil.add_array("orig", 1024, 4)
stencil.add_array("sol", 1024, 4)
stencil.add_array("filter", 9, 4)
stencil.add_loop("stencil", "outer")
stencil.add_loop("stencil", "inner")

triad = Benchmark("triad", "triad")
triad.set_kernels(["triad"])
triad.set_main_id(0x000001B0)
triad.add_loop("triad", "triad")
triad.add_array("a", 2048, 4)
triad.add_array("b", 2048, 4)
triad.add_array("c", 2048, 4)
