```python
from django.db import transaction


try:
    active = True
    with transaction.atomic():
        save_id = transaction.savepoint()
except Exception as e:
    # 失败则回滚
    active = False
    transaction.savepoint_rollback(save_id)
    logger.error('')
# 判断是否提交该次事务
if active:
    transaction.savepoint_commit(save_id)

```
