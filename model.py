"""
RL Fine-Tuning from Scratch: Build the Environment, Train with GRPO

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - eval_rpn
OPS = ["+", "-", "*"]


def eval_rpn(tokens):
    stack = []

    for token in tokens:

        # Case 1: The token is an operator
        if token in OPS:

            if len(stack) < 2:
                return None

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            else:
                result = a * b

            stack.append(result)

        # Case 2: The token is a single digit
        elif isinstance(token, str) and len(token) == 1 and token in "0123456789":
            stack.append(int(token))

        # Case 3: Invalid token
        else:
            return None

    if len(stack) == 1:
        return stack[0]

    return None

# Step 2 - solve (not yet solved)
# TODO: implement

# Step 3 - verify (not yet solved)
# TODO: implement

# Step 4 - make_task (not yet solved)
# TODO: implement

# Step 5 - task_split (not yet solved)
# TODO: implement

# Step 6 - encode_task (not yet solved)
# TODO: implement

# Step 7 - Policy (not yet solved)
# TODO: implement

# Step 8 - sample_completions (not yet solved)
# TODO: implement

# Step 9 - completion_logprobs (not yet solved)
# TODO: implement

# Step 10 - make_demos (not yet solved)
# TODO: implement

# Step 11 - sft_loss (not yet solved)
# TODO: implement

# Step 12 - pretrain (not yet solved)
# TODO: implement

# Step 13 - pass_at_k (not yet solved)
# TODO: implement

# Step 14 - group_rewards (not yet solved)
# TODO: implement

# Step 15 - group_advantages (not yet solved)
# TODO: implement

# Step 16 - kl_k3 (not yet solved)
# TODO: implement

# Step 17 - grpo_loss (not yet solved)
# TODO: implement

# Step 18 - rollout (not yet solved)
# TODO: implement

# Step 19 - train_grpo (not yet solved)
# TODO: implement

# Step 20 - completion_entropy (not yet solved)
# TODO: implement

# Step 21 - evaluate (not yet solved)
# TODO: implement

# Step 22 - build_base (not yet solved)
# TODO: implement

# Step 23 - run_grpo (not yet solved)
# TODO: implement

# Step 24 - rlvr_experiment (not yet solved)
# TODO: implement

