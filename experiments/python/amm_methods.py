#!/bin/env/python

from . import amm, vq_amm

METHOD_EXACT = 'Exact'
METHOD_SKETCH_SQ_SAMPLE = 'SketchSqSample'
METHOD_SVD = 'SVD'  # truncated SVD run on the matrix at test time
METHOD_FD_AMM = 'FD-AMM'
METHOD_COOCCUR = 'CooccurSketch'
METHOD_PCA = 'PCA'  # PCA projection, with PCA basis learned at train time
METHOD_SPARSE_PCA = 'SparsePCA'  # like above, using sklearn SparsePCA
METHOD_RANDGAUSS = 'RandGauss'
METHOD_ORTHOGAUSS = 'OrthoGauss'
METHOD_HADAMARD = 'Hadamard'
METHOD_RADEMACHER = 'Rademacher'
METHOD_FASTJL = 'FastJL'
METHOD_HASHJL = 'HashJL'
METHOD_OSNAP = 'OSNAP'
METHOD_OPQ = 'OPQ'
METHOD_BOLT = 'Bolt'
METHOD_BOLT_PERM = 'Bolt+Perm'
METHOD_BOLT_CORRPERM = 'Bolt+CorrPerm'
METHOD_BOLT_SPLITS = 'BoltSplits'
METHOD_BOLT_MULTISPLITS = 'Bolt+MultiSplits'
METHOD_BOLT_PERM_MULTISPLITS = 'Bolt+Perm+MultiSplits'
METHOD_PQ = 'PQ'
METHOD_PQ_PERM = 'PQ+Perm'
METHOD_PQ_MULTISPLITS = 'PQ+MultiSplits'
METHOD_PQ_PERM_MULTISPLITS = 'PQ+Perm+MultiSplits'
METHOD_MITHRALPQ = 'MithralPQ'
METHOD_MITHRAL = 'Mithral'

# these are for trying out different perm options
METHOD_BOLT_GEHT_COV_TOPK = 'Bolt_CovTopk'
METHOD_BOLT_GEHT_COV_SAMP = 'Bolt_CovSamp'
METHOD_BOLT_GEHT_COR_TOPK = 'Bolt_CorTopk'
METHOD_BOLT_GEHT_COR_SAMP = 'Bolt_CorSamp'

# DEFAULT_METHODS = (METHOD_EXACT, METHOD_SVD, METHOD_FD_AMM,
#                    METHOD_COOCCUR, METHOD_PCA, METHOD_PQ,
#                    METHOD_BOLT, METHOD_MITHRALPQ)

METHOD_TO_ESTIMATOR = {
    METHOD_EXACT: amm.ExactMatMul,
    METHOD_SKETCH_SQ_SAMPLE: amm.SketchSqSample,
    METHOD_SVD: amm.SvdSketch,
    METHOD_FD_AMM: amm.FdAmm,
    METHOD_COOCCUR: amm.CooccurSketch,
    METHOD_PCA: amm.TrainedPcaSketch,
    METHOD_SPARSE_PCA: amm.TrainedSparsePcaSketch,
    METHOD_RANDGAUSS: amm.RandGaussSketch,
    METHOD_ORTHOGAUSS: amm.RandOrthoGaussSketch,
    METHOD_HADAMARD: amm.HadamardSketch,
    METHOD_RADEMACHER: amm.RandRademacherSketch,
    METHOD_FASTJL: amm.FastJlSketch,
    METHOD_HASHJL: amm.HashJlSketch,
    METHOD_OSNAP: amm.OsnapSketch,
    METHOD_PQ: vq_amm.PQMatmul,
    METHOD_BOLT: vq_amm.BoltMatmul,
    METHOD_OPQ: vq_amm.OPQMatmul,
    METHOD_BOLT_CORRPERM: vq_amm.GEHTBoltMatmul_CorrTopk,
    METHOD_BOLT_GEHT_COV_TOPK: vq_amm.GEHTBoltMatmul_CovTopk,
    METHOD_BOLT_GEHT_COV_SAMP: vq_amm.GEHTBoltMatmul_CovSamp,
    METHOD_BOLT_GEHT_COR_TOPK: vq_amm.GEHTBoltMatmul_CorrTopk,
    METHOD_BOLT_GEHT_COR_SAMP: vq_amm.GEHTBoltMatmul_CorrSamp,
    METHOD_BOLT_PERM: vq_amm.GEHTBoltMatmul_CovTopk,
    METHOD_BOLT_SPLITS: vq_amm.BoltSplits,
    METHOD_BOLT_MULTISPLITS: vq_amm.BoltMultiSplits,
    METHOD_BOLT_PERM_MULTISPLITS: vq_amm.BoltPermMultiSplits,
    METHOD_PQ_PERM: vq_amm.PQPerm,
    METHOD_PQ_MULTISPLITS: vq_amm.PQMultiSplits,
    METHOD_PQ_PERM_MULTISPLITS: vq_amm.PQPermMultiSplits,
    METHOD_MITHRALPQ: vq_amm.MithralPQ,
    METHOD_MITHRAL: vq_amm.MithralMatmul
}
ALL_METHODS = sorted(list(METHOD_TO_ESTIMATOR.keys()))
ALL_METHODS.remove(METHOD_SKETCH_SQ_SAMPLE),  # always terrible results
ALL_METHODS.remove(METHOD_OPQ)  # takes forever to train, more muls than exact
# these were just for playing with different permuation options
ALL_METHODS.remove(METHOD_BOLT_GEHT_COV_TOPK)
ALL_METHODS.remove(METHOD_BOLT_GEHT_COV_SAMP)
ALL_METHODS.remove(METHOD_BOLT_GEHT_COR_TOPK)
ALL_METHODS.remove(METHOD_BOLT_GEHT_COR_SAMP)

RANDOM_SKETCHING_METHODS = (
    METHOD_FASTJL, METHOD_HASHJL, METHOD_OSNAP, METHOD_RANDGAUSS,
    METHOD_ORTHOGAUSS, METHOD_HADAMARD, METHOD_RADEMACHER)

DENSE_SKETCH_METHODS = (
    METHOD_FASTJL, METHOD_RANDGAUSS, METHOD_ORTHOGAUSS, METHOD_RADEMACHER)

FAST_SKETCH_METHODS = RANDOM_SKETCHING_METHODS + (
    METHOD_PCA, METHOD_SPARSE_PCA)
# SLOW_SKETCH_METHODS = (METHOD_SVD, METHOD_FD_AMM, METHOD_COOCCUR)
SLOW_SKETCH_METHODS = (METHOD_FD_AMM, METHOD_COOCCUR, METHOD_SVD)
SKETCH_METHODS = FAST_SKETCH_METHODS + SLOW_SKETCH_METHODS
# VQ_METHODS = (METHOD_PQ, METHOD_BOLT, METHOD_OPQ)
# VQ_METHODS = (METHOD_PQ, METHOD_BOLT)
BOLT_METHODS = (METHOD_BOLT, METHOD_BOLT_PERM,
                METHOD_BOLT_CORRPERM, METHOD_BOLT_SPLITS,
                METHOD_BOLT_MULTISPLITS, METHOD_BOLT_PERM_MULTISPLITS)
PQ_METHODS = (METHOD_PQ, METHOD_PQ_PERM, METHOD_PQ_MULTISPLITS,
              METHOD_PQ_PERM_MULTISPLITS)
MITHRAL_METHODS = (METHOD_MITHRALPQ, METHOD_MITHRAL)
VQ_METHODS = PQ_METHODS + BOLT_METHODS + MITHRAL_METHODS
NONDETERMINISTIC_METHODS = (METHOD_SKETCH_SQ_SAMPLE, METHOD_SVD) + VQ_METHODS



USE_METHODS = ((METHOD_MITHRAL, METHOD_MITHRALPQ, METHOD_EXACT, METHOD_BOLT) +
               # FAST_SKETCH_METHODS + SLOW_SKETCH_METHODS)
               FAST_SKETCH_METHODS)  # slow methods too bad; mess up the plots
