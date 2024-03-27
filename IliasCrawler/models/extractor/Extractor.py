import yaml
import os
from IliasCrawler.models.extractor.Element import Element
from IliasCrawler.models.extractor.Type import Type


class Extractor:

    def __init__(self, jsonPath: str) -> None:
        yaml_data = Extractor.combine_yaml_files(jsonPath)
        self.root_type = Extractor.create_type_graph_from_yaml(yaml_data)

    @staticmethod
    def combine_yaml_files(directory_path):
        combined_data = {}
        if not os.path.isdir(directory_path):
            raise ValueError("The specified directory path does not exist.")
        for filename in os.listdir(directory_path):
            if filename.endswith(".yaml") or filename.endswith(".yml"):
                file_path = os.path.join(directory_path, filename)
                with open(file_path, "r") as yaml_file:
                    data = yaml.safe_load(yaml_file)
                    if data is not None:
                        combined_data.update(data)
        return combined_data

    def create_type_graph_from_yaml(yaml_data):
        if 'root' not in yaml_data:
            raise ValueError("The 'root' node is not present in the aggregated YAML data.")

        types = {}

        for type_name, type_data in yaml_data.items():
            types[type_name] = Type(type_name, type_data)

        for type_name, type_data in yaml_data.items():
            current_type = types[type_name]
            for child_type in type_data.get("childTypes", []):
                child_type_obj = types[child_type]
                current_type.add_child_type(child_type_obj)

        return types["root"]

    def extract_data(self, parent: Element):
        leafs = []
        for type in parent.type.child_types:
            elements = type.extract(parent)
            if type.is_leaf:
                leafs.extend(elements)
            else:
                for page in elements:
                    leafs.extend(self.extract_data(page))
                    page.delete_soup()
        return leafs