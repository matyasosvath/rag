from typing import Union

import time

import os
import torch

from src.logging import logger
from src import typing


NUM_WORKERS = os.cpu_count()
NUM_GPUS = torch.cuda.device_count()
CUDA_AVAILABLE = torch.cuda.is_available()
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
DEVICES = [f"cuda:{i}" for i in range(NUM_GPUS)] if NUM_GPUS else ["cpu"]


def log_startup_diagnostics() -> None:
    logger.info(f"Number of CPU Workers: {NUM_WORKERS}")
    logger.info(f"Number of GPUs available: {NUM_GPUS}")
    logger.info(f"Is CUDA available: {CUDA_AVAILABLE}")
    logger.info(f"Selected device: {DEVICE}")
    logger.info(f"Available devices: {DEVICES}")
    log_memory_usage() if CUDA_AVAILABLE else None


def log_memory_usage() -> None:
    for device in DEVICES:
        get_memory_alloc(device)


def get_memory_alloc(device: Union[str, torch.device], divisor: int = 1024 ** 3) -> float:
    free_memory, total_memory = torch.cuda.mem_get_info(device)
    f_memory, t_memory = free_memory / divisor, total_memory / divisor
    memory_allocated = t_memory - f_memory
    logger.info(
        f"Memory statistics for {device} device: "
        f"allocated: {memory_allocated:.2f}/ {t_memory:.2f} GB, "
        f"free: {f_memory:.2f}/ {t_memory:.2f} GB"
    )
    return memory_allocated


def record_start_time(model_name: typing.Models, inference: bool = False) -> float:
    start_time = time.time()
    logger.info(f"Model {model_name} started inference!")
    return start_time


def log_completion_time(model_name: typing.Models, start_time: float) -> float:
    total_time = time.time() - start_time
    logger.info(f"Model {model_name} finished generating text in {total_time:.3f} seconds.")
    return total_time
