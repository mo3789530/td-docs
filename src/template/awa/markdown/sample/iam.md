# AWS IAM {project_id}  

### Role ({iam_name})  

| Items              | values                      |
| ------------------ | --------------------------- |
| schema_version     | {{data.schema_version}}     |
| arn                | {{data.arn}}                |
| assume_role_policy | {{data.assume_role_policy}} |
| description        | {{data.description}}        |
| tags               | {{data.tags}}               |
| dependencies       | {{data.dependencies}}       |

### aws_iam_policy {{name}}

| Items              | values                      |
| ------------------ | --------------------------- |
| schema_version     | {{data.schema_version}}     |
| arn                | {{data.arn}}                |
| name               | {{data.name}}               |
| assume_role_policy | {{data.assume_role_policy}} |
| description        | {{data.description}}        |
| policy             | {{data.policy}}             |
| tags               | {{data.tags}}               |
| dependencies       | {{data.dependencies}}       |

### aws_iam_policy_document {{name}}

| Items          | values                  |
| -------------- | ----------------------- |
| schema_version | {{data.schema_version}} |
| id             | {{data.id}}             |
| name           | {{data.name}}           |
| json           | {{data.json}}           |
| state          | {{data.state}}          |
| tags           | {{data.tags}}           |
| condition      | {{data.condition}}      |
| principals     | {{data.principals}}     |
| resources      | {{data.resources}}      |

### aws_iam_role_policy_attachment {{name}}
| Items          | values                  |
| -------------- | ----------------------- |
| schema_version | {{data.schema_version}} |
| id             | {{data.id}}             |
| role           | {{data.role}}           |
| policy_arn     | {{data.policy_arn}}     |
| tags           | {{data.tags}}           |
| dependencies   | {{data.dependencies}}   |


### aws_iam_user_policy_attachment {{name}}
| Items          | values                  |
| -------------- | ----------------------- |
| schema_version | {{data.schema_version}} |
| id             | {{data.id}}             |
| policy_arn     | {{data.policy_arn}}     |
| dependencies   | {{data.dependencies}}   |

### aws_iam_user {{name}}
| Items          | values                  |
| -------------- | ----------------------- |
| schema_version | {{data.schema_version}} |
| id             | {{data.id}}             |
| arn            | {{data.arn}}            |
| name           | {{data.name}}           |
| tags           | {{data.tags}}           |
| dependencies   | {{data.dependencies}}   |

### aws_iam_policy_attachment {{name}}
| Items          | values                  |
| -------------- | ----------------------- |
| schema_version | {{data.schema_version}} |
| id             | {{data.id}}             |
| name           | {{data.name}}           |
| policy_arn     | {{data.policy_arn}}     |
| tags           | {{data.tags}}           |
| roles          | {{data.roles}}          |
| users          | {{data.users}}          |
| dependencies   | {{data.dependencies}}   |

