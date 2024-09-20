# Clusters

Types:

```python
from inferencing.types import ClusterListResponse
```

Methods:

- <code title="get /api/v1/clusters">client.clusters.<a href="./src/inferencing/resources/clusters.py">list</a>() -> <a href="./src/inferencing/types/cluster_list_response.py">ClusterListResponse</a></code>

# Inference

## Checkpoints

Types:

```python
from inferencing.types.inference import (
    CheckpointRetrieveResponse,
    CheckpointListResponse,
    CheckpointDelResponse,
)
```

Methods:

- <code title="get /api/v1/inference/checkpoints/{filename}">client.inference.checkpoints.<a href="./src/inferencing/resources/inference/checkpoints.py">retrieve</a>(filename) -> <a href="./src/inferencing/types/inference/checkpoint_retrieve_response.py">CheckpointRetrieveResponse</a></code>
- <code title="get /api/v1/inference/checkpoints">client.inference.checkpoints.<a href="./src/inferencing/resources/inference/checkpoints.py">list</a>() -> <a href="./src/inferencing/types/inference/checkpoint_list_response.py">CheckpointListResponse</a></code>
- <code title="get /api/v1/inference/checkpoints/{filename}/del">client.inference.checkpoints.<a href="./src/inferencing/resources/inference/checkpoints.py">delete</a>(filename) -> <a href="./src/inferencing/types/inference/checkpoint_del_response.py">CheckpointDelResponse</a></code>

## Tasks

Types:

```python
from inferencing.types.inference import TaskCreateResponse, TaskRetrieveResponse, TaskListResponse
```

Methods:

- <code title="post /api/v1/inference/tasks">client.inference.tasks.<a href="./src/inferencing/resources/inference/tasks.py">create</a>(\*\*<a href="src/inferencing/types/inference/task_create_params.py">params</a>) -> <a href="./src/inferencing/types/inference/task_create_response.py">TaskCreateResponse</a></code>
- <code title="get /api/v1/inference/tasks/{id}">client.inference.tasks.<a href="./src/inferencing/resources/inference/tasks.py">retrieve</a>(id) -> <a href="./src/inferencing/types/inference/task_retrieve_response.py">TaskRetrieveResponse</a></code>
- <code title="get /api/v1/inference/tasks">client.inference.tasks.<a href="./src/inferencing/resources/inference/tasks.py">list</a>(\*\*<a href="src/inferencing/types/inference/task_list_params.py">params</a>) -> <a href="./src/inferencing/types/inference/task_list_response.py">TaskListResponse</a></code>
- <code title="get /api/v1/inference/tasks/{id}/cancel">client.inference.tasks.<a href="./src/inferencing/resources/inference/tasks.py">cancel</a>(id) -> None</code>
