
# Configuration for Training BabyGPT on C Code
dataset = 'code_generation'
out_dir = 'out-code-generation'
eval_interval = 250
eval_iters = 200
log_interval = 10

# Model architecture (Consistent with your Task 3 best findings)
n_layer = 7
n_head = 6  # Use your best head count from Task 3
n_embd = 420
block_size = 256

# Training settings
batch_size = 32
gradient_accumulation_steps = 1
max_iters = 1000
learning_rate = 1e-3
lr_decay_iters = 1000
min_lr = 1e-4
beta2 = 0.99
warmup_iters = 100

device = 'cuda'
compile = False
