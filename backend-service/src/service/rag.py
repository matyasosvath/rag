import gc
import traceback
from typing import Any

import torch
from src import helper, typing
from src.logging import logger
from src.service import data_store, generation


def inference(model_name: typing.RagModels, input: typing.Question) -> Any:

    start_time = helper.record_start_time(model_name)

    try:

        context = data_store.retrieve_context(input)
        result = generation.generate(input.text, context)

    except torch.cuda.OutOfMemoryError as e:

        logger.error('Out of memory error occurred: %s', e)
        logger.error(traceback.format_exc())

        raise torch.cuda.OutOfMemoryError

    finally:

        torch.cuda.empty_cache()
        gc.collect()

    helper.log_completion_time(model_name, start_time)

    # suggestion: insert question, context and answert to a database for later analysis

    return result