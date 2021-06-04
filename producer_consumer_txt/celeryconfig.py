from producer_consumer_txt.config import envs

broker_url = envs.BROKER
result_backend = envs.BACKEND

broker_connection_max_retries = 4

imports = ["producer_consumer_txt.services.queue"]

task_routes = {
    'producer_consumer_txt.services.queue.task_write_json_to_file': {'queue': 'write_json'}
}
