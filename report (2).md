# SEEM3650 Practical Exam Report

## Task 2: Shakespeare Character-level Model Samples
First 5 lines of generated output:
```
Overriding: out_dir = out-shakespeare-char
number of parameters: 10.65M
Loading meta from data/shakespeare_char/meta.pkl...

And they bring with the sorrow
```

## Task 3: Model Architecture Exploration
Configuration: XYZ mod 4 = 2
Fixed parameter: Layers = 7
Results:
- Heads=2: Val Loss=1.8873
- Heads=3: Val Loss=1.8684
- Heads=5: Val Loss=1.8477
- Heads=7: Val Loss=1.8581

**Best configuration:** Layers=7, Heads=5
**Lowest validation loss:** 1.8477

### First 20 Lines of Generated Code Samples
```
Overriding: out_dir = out-code-generation
Overriding: num_samples = 1
Overriding: max_new_tokens = 1000
number of parameters: 14.87M
Loading meta from data/code_generation/meta.pkl...

        flushAppendOnlyFiles, it is a commands of a command is disabled. */
        addReplyBulkCString(c, "replushing");
    }
    if (c->replaced_by) {
        /* If there is a changed and actual Redis not in command */
        break;

       char busy_posted = retval;
        if (retval) return 1;
        if (redisCommandSds(c->legacy_range, c->replsroPeR_CHILD_DEFINE, c->lastvalue)) {
            c->lag = &resetCommandData(da = c->last_lazy_timeout | c->last_refer_enabled;
               strerror(res;);
             }
            serverAssert(&c->flags & CMD_LASTER_ALLOW);
```

### Favorite Generated Code Snippet
The most coherent/interesting snippet from the generated code:
```c

        flushAppendOnlyFiles, it is a commands of a command is disabled. */
        addReplyBulkCString(c, "replushing");
    }
    if (c->replaced_by) {
        /* If there is a changed and actual Redis not in command */
        break;

       char busy_posted = retval;
        if (retval) return 1;
```
