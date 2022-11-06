# aws_subnet {{name| default("None")}}
| Items                           | values                                 |
| ------------------------------- | -------------------------------------- |
| arn                             | {{data.arn                             | default("None")}} |
| assign_ipv6_address_on_creation | {{data.assign_ipv6_address_on_creation | default("None")}} |
| availability_zone               | {{data.availability_zone               | default("None")}} |
| availability_zone_id            | {{data.availability_zone_id            | default("None")}} |
| cidr_block                      | {{data.cidr_block                      | default("None")}} |
| id                              | {{data.id                              | default("None")}} |
| ipv6_cidr_block                 | {{data.ipv6_cidr_block                 | default("None")}} |
| ipv6_cidr_block_association_id  | {{data.ipv6_cidr_block_association_id  | default("None")}} |
| map_public_ip_on_launch         | {{data.map_public_ip_on_launch         | default("None")}} |
| outpost_arn                     | {{data.outpost_arn                     | default("None")}} |
| owner_id                        | {{data.owner_id                        | default("None")}} |
| tags                            | {{data.tags                            | default("None")}} |
| timeouts                        | {{data.timeouts                        | default("None")}} |
| vpc_id                          | {{data.vpc_id                          | default("None")}} |