class Iam:
    iam_type = ["aws_iam_instance_profile", "aws_iam_role",
                "aws_iam_policy", "aws_iam_policy_document"]

    def __init__(self) -> None:
        pass

    # aws_iam_role
    def role_parser(self, json: dict, iam_type: str) -> dict:
        schema_version = "schema_version"
        attributes = "attributes"
        attributes_arn = "arn"
        attributes_assume_role_policy = "assume_role_policy"
        attributes_description = "description"
        attributes_tags = "tags"
        dependencies = "dependencies"

        return {
            "type": iam_type,
            schema_version: json.get(schema_version),
            attributes_arn: json.get(attributes).get(attributes_arn),
            attributes_assume_role_policy: json.get(attributes).get(attributes_assume_role_policy),
            attributes_description: json.get(attributes).get(attributes_description),
            attributes_tags: json.get(attributes).get(attributes_tags),
            dependencies: json.get(dependencies)
        }

    # aws_iam_policy
    def policy_parser(self, json: dict, iam_type: str) -> dict:
        schema_version = "schema_version"
        attributes = "attributes"
        attributes_arn = "arn"
        attributes_assume_role_policy = "assume_role_policy"
        attributes_description = "description"
        attributes_tags = "tags"
        attributes_policy = "policy"
        dependencies = "dependencies"

        return {
            "type": iam_type,
            schema_version: json.get(schema_version),
            attributes_arn: json.get(attributes).get(attributes_arn),
            attributes_assume_role_policy: json.get(attributes).get(attributes_assume_role_policy),
            attributes_description:        json.get(attributes).get(attributes_description),
            attributes_tags:               json.get(attributes).get(attributes_tags),
            attributes_policy:             json.get(attributes).get(attributes_policy),
            dependencies:                  json.get(dependencies)
        }

    # aws_iam_instance_profile
    def instance_profile_parser(self, json: dict, iam_type: str) -> dict:
        pass

    # aws_iam_policy_document
    def policy_document_parser(self, json: dict, iam_type: str) -> dict:
        schema_version = "schema_version"
        attributes = "attributes"
        attributes_id = "id"
        attributes_json = "json"
        attributes_state = "statement"
        attributes_tags = "tags"
        attributes_condition = "condition"
        attributes_principals = "principals"
        resources = "resources"

        return {
            "type":                iam_type,
            attributes_id:         json.get(attributes).get(attributes_id),
            attributes_json:       json.get(attributes).get(attributes_json),
            attributes_state:      json.get(attributes).get(attributes_state),
            attributes_condition:  json.get(attributes).get(attributes_condition),
            attributes_tags:       json.get(attributes).get(attributes_tags),
            attributes_principals: json.get(attributes).get(attributes_principals),
            resources:             json.get(resources)
        }

    # unknow type
    def unknown_type(self, json: dict, iam_type: str):
        print(f"{iam_type} is not defined")
        raise Exception(f"{iam_type} is not defined in iam type")

    switcher = {
        "aws_iam_instance_profile": instance_profile_parser,
        "aws_iam_role": role_parser,
        "aws_iam_policy": policy_parser,
        "aws_iam_policy_document": policy_document_parser,
    }

    def parse(self, json: dict, iam_type: str):
        return self.switcher.get(iam_type, self.unknown_type)(self=self, json=json, iam_type=iam_type)
