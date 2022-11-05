# AWS IAM {project_id}  

### aws_iam_role ({iam_name})  

| Items              | values                    |
| ------------------ | ------------------------- |
| schema_version     | {{data.schema_version     | default("None") }} |
| arn                | {{data.arn                | default("None") }} |
| assume_role_policy | {{data.assume_role_policy | default("None") }} |
| description        | {{data.description        | default("None") }} |
| tags               | {{data.tags               | default("None") }} |
| dependencies       | {{data.dependencies       | default("None") }} |

### aws_iam_policy {{name}}

| Items              | values                    |
| ------------------ | ------------------------- |
| schema_version     | {{data.schema_version     | default("None")}} |
| arn                | {{data.arn                | default("None")}} |
| name               | {{data.name               | default("None")}} |
| assume_role_policy | {{data.assume_role_policy | default("None")}} |
| description        | {{data.description        | default("None")}} |
| policy             | {{data.policy             | default("None")}} |
| tags               | {{data.tags               | default("None")}} |
| dependencies       | {{data.dependencies       | default("None")}} |

### aws_iam_policy_document {{name}}

| Items          | values                |
| -------------- | --------------------- |
| schema_version | {{data.schema_version | default("None")}} |
| id             | {{data.id             | default("None")}} |
| name           | {{data.name           | default("None")}} |
| json           | {{data.json           | default("None")}} |
| state          | {{data.state          | default("None")}} |
| tags           | {{data.tags           | default("None")}} |
| condition      | {{data.condition      | default("None")}} |
| principals     | {{data.principals     | default("None")}} |
| resources      | {{data.resources      | default("None")}} |

### aws_iam_role_policy_attachment {{name}}
| Items          | values                |
| -------------- | --------------------- |
| schema_version | {{data.schema_version | default("None")}} |
| id             | {{data.id             | default("None")}} |
| role           | {{data.role           | default("None")}} |
| policy_arn     | {{data.policy_arn     | default("None")}} |
| tags           | {{data.tags           | default("None")}} |
| dependencies   | {{data.dependencies   | default("None")}} |


### aws_iam_user_policy_attachment {{name}}
| Items          | values                |
| -------------- | --------------------- |
| schema_version | {{data.schema_version | default("None")}} |
| id             | {{data.id             | default("None")}} |
| policy_arn     | {{data.policy_arn     | default("None")}} |
| dependencies   | {{data.dependencies   | default("None")}} |

### aws_iam_user {{name}}
| Items          | values                |
| -------------- | --------------------- |
| schema_version | {{data.schema_version | default("None")}} |
| id             | {{data.id             | default("None")}} |
| arn            | {{data.arn            | default("None")}} |
| name           | {{data.name           | default("None")}} |
| tags           | {{data.tags           | default("None")}} |
| dependencies   | {{data.dependencies   | default("None")}} |

### aws_iam_policy_attachment {{name}}
| Items          | values                |
| -------------- | --------------------- |
| schema_version | {{data.schema_version | default("None")}} |
| id             | {{data.id             | default("None")}} |
| name           | {{data.name           | default("None")}} |
| policy_arn     | {{data.policy_arn     | default("None")}} |
| tags           | {{data.tags           | default("None")}} |
| roles          | {{data.roles          | default("None")}} |
| users          | {{data.users          | default("None")}} |
| dependencies   | {{data.dependencies   | default("None")}} |

