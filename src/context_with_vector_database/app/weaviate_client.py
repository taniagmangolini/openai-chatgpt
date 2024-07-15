import weaviate, os


class WeaviateClient:

    def __init__(self, logger, class_name, openai_api_key):
        self.logger = logger
        self.class_name = class_name
        self.url = "http://weaviate:8080"
        self.client = self.get_client(openai_api_key)
 

    def get_client(self, openai_api_key):
        return weaviate.Client(
            url=self.url,
            auth_client_secret={"X-OpenAI-Api-Key": openai_api_key},
        )

    def weaviate_create_schema(self, schema):
        try:
            self.client.schema.create(schema)
            self.logger.info("Schema successfully created.")
        except Exception as e:
            self.logger.error(f"Failed to create schema: {e}")

    def weaviate_delete_data(self):
        try:
            self.client.schema.delete_class(
                class_name=self.class_name
            )
            self.logger.info("Data successfully reset.")
        except Exception as e:
            self.logger.error(f"Error while deleting class: {e}")
            return {"error in weaviate_reset": str(e)}, 500

    def weaviate_nearest_interactions(self, query, certainty, limit):
        try:
            result = (
                self.client.query.get(
                    class_name=self.class_name, properties=["role", "content"]
                )
                .with_near_text({"concepts": [query], "certainty": certainty})
                .with_limit(limit)
                .do()
            )

            data = result["data"]["Get"][self.class_name]
            data = data if data is not None else []
            return {"data": data}

        except Exception as e:
            self.logger.error(f"Error while searching: {e}")

    def weaviate_latest_interactions(self, limit):
        try:
            result = (
                self.client.query.get(
                    class_name=self.class_name, properties=["role", "content"]
                )
                .with_limit(limit)
                .do()
            )

            data = result["data"]["Get"][self.class_name]
            data = data if data is not None else []
            return {"data": data}

        except Exception as e:
            self.logger.error(f"Error while searching: {e}")

    def weaviate_save_data(self, data):
        self.client.batch.configure(batch_size=100)
        with self.client.batch as batch:
            for _, d in enumerate(data):
                properties = {"role": d["role"], "content": d["content"]}
                batch.add_data_object(
                    properties,
                    self.class_name,
                )
