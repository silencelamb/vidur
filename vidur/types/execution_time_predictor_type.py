from vidur.types.base_int_enum import BaseIntEnum


class ExecutionTimePredictorType(BaseIntEnum):
    DUMMY = 1
    RANDOM_FORREST = 2
    LINEAR_REGRESSION = 3
    AMMU = 4  # AMMU Layer-3 seam — implemented out-of-tree in perf_sim/ammu_backend/
