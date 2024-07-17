import weaviate, os
import pandas as pd


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

    def weaviate_semantic_search(self, query, prompt):
        nearText = {
            "concepts": [query],
        }

        properties = ["title", "content", "_additional {distance}"]

        limit = 1

        response = (
            self.client.query.get(
                class_name=self.class_name,
                properties=properties,
            )
            .with_generate(
                single_prompt=prompt
                #grouped_task=prompt
            )
            .with_near_text(nearText)
            .with_limit(limit)
            .do()
        )

        result = response["data"]["Get"][self.class_name]
        return result

    def weaviate_import_data(self, path):
        counter = 0
        interval = 100
        batch = 30

        csv_iterator = pd.read_csv(
            path,
            usecols=["id", "url", "title", "text", "content_vector"],
            chunksize=batch,
            nrows=batch,
        )

        self.client.batch.configure(batch_size=batch)

        with self.client.batch as batch:
            for chunk in csv_iterator:
                for _, row in chunk.iterrows():

                    properties = {
                        "title": row.title,
                        "content": row.text,
                        "url": row.url,
                    }

                    batch.add_data_object(
                        properties,
                        class_name=self.class_name,
                        vector=eval(row.content_vector),
                    )

                    counter += 1
                    if counter % interval == 0:
                        self.logger.debug(f"Processed {counter} articles...")
        self.logger.debug(f"Finished articles importing.")
