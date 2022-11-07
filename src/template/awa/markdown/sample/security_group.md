# aws_security_group {{name| default("None")}}
| Items                  | values                        |
| ---------------------- | ----------------------------- |
| arn                    | {{data.arn                    | default("None")}} |
| description            | {{data.description            | default("None")}} |
| egress                 | {{data.egress                 | default("None")}} |
| id                     | {{data.id                     | default("None")}} |
| ingress                | {{data.ingress                | default("None")}} |
| name                   | {{data.name                   | default("None")}} |
| name_prefix            | {{data.name_prefix            | default("None")}} |
| owner_id               | {{data.owner_id               | default("None")}} |
| revoke_rules_on_delete | {{data.revoke_rules_on_delete | default("None")}} |
| tags                   | {{data.tags                   | default("None")}} |
| timeouts               | {{data.timeouts               | default("None")}} |
| vpc_id                 | {{data.vpc_id                 | default("None")}} |