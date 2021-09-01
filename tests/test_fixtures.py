import pytest
from airbyte_dto_factory import *
from airbyte_config_model import *

@pytest.fixture
def dummy_source_dto():
    """
    Creates a dummy SourceDto
    """
    source = SourceDto()
    source.source_definition_id = 'ef69ef6e-aa7f-4af1-a01d-ef775033524e'
    source.source_id = '7d95ec85-47c6-42d4-a7a2-8e5c22c810d2'
    source.workspace_id = 'f3b9e848-790c-4cdd-a475-5c6bb156dc10'
    source.connection_configuration = {
        'access_token': '**********'
    }
    source.name = 'apache/superset'
    source.source_name = 'GitHub'
    source.tag = 'tag1'
    return source


@pytest.fixture
def dummy_destination_dto():
    """
    Creates a dummy DestinationDto
    """
    destination = DestinationDto()
    destination.destination_definition_id = '25c5221d-dce2-4163-ade9-739ef790f503'
    destination.destination_id = 'a41cb2f8-fcce-4c91-adfe-37c4586609f5'
    destination.workspace_id = 'f3b9e848-790c-4cdd-a475-5c6bb156dc10'
    destination.connection_configuration = {
        'database': 'postgres',
        'host': 'hostname.com',
        'port': '5432',
        'schema': 'demo',
        'username': 'devrel_master',
        'password': '**********'
    }
    destination.name = 'devrel-rds'
    destination.destination_name = 'Postgres'
    destination.tag = 'tag2'
    return destination


@pytest.fixture
def dummy_connection_dto():
    pass


@pytest.fixture
def dummy_source_definitions():
    """
    Create a dummy source definition (as dict)
    """
    source_definitions = [{'sourceDefinitionId': 'c2281cee-86f9-4a86-bb48-d23286b4c7bd',
                          'name': 'Slack', 'dockerRepository': 'airbyte/source-slack',
                          'dockerImageTag': '0.1.9',
                          'documentationUrl': 'https://docs.airbyte.io/integrations/sources/slack',
                          'icon': 'icon.png'},
                          {'sourceDefinitionId': 'ef69ef6e-aa7f-4af1-a01d-ef775033524e',
                           'name': 'GitHub', 'dockerRepository': 'airbyte/source-github-singer',
                           'dockerImageTag': '0.1.7', 'documentationUrl': 'https://hub.docker.com/r/airbyte/source-github-singer',
                           'icon': None}]
    return source_definitions


@pytest.fixture
def dummy_destination_definitions():
    """
    c=Create a dummy destination definition (as dict)
    """
    destination_definitions = [{'destinationDefinitionId': '22f6c74f-5699-40ff-833c-4a879ea40133',
                                'name': 'BigQuery',
                                'dockerRepository': 'airbyte/destination-bigquery',
                                'dockerImageTag': '0.3.12',
                                'documentationUrl': 'https://docs.airbyte.io/integrations/destinations/bigquery',
                                'icon': None},
                               {'destinationDefinitionId': '25c5221d-dce2-4163-ade9-739ef790f503',
                                'name': 'Postgres',
                                'dockerRepository': 'airbyte/destination-postgres',
                                'dockerImageTag': '0.3.5',
                                'documentationUrl': 'https://docs.airbyte.io/integrations/destinations/postgres',
                                'icon': None}]
    return destination_definitions


@pytest.fixture
def dummy_source_dict():
    """
    Creates a dummy source dict
    """
    source_dict = {
        'sourceDefinitionId': 'ef69ef6e-aa7f-4af1-a01d-ef775033524e',
        'sourceId': '7d95ec85-47c6-42d4-a7a2-8e5c22c810d2',
        'workspaceId': 'f3b9e848-790c-4cdd-a475-5c6bb156dc10',
        'connectionConfiguration': {'access_token': '**********'},
        'name': 'apache/superset',
        'sourceName': 'GitHub',
        'tag': 'tag1'
    }
    return source_dict


@pytest.fixture
def dummy_destination_dict():
    """
    Creates a dummy destination dict
    """
    destination_dict = {
        'destinationDefinitionId': '25c5221d-dce2-4163-ade9-739ef790f503',
        'destinationId': 'a41cb2f8-fcce-4c91-adfe-37c4586609f5',
        'workspaceId': 'f3b9e848-790c-4cdd-a475-5c6bb156dc10',
        'connectionConfiguration': {
            'database': 'postgres',
            'host': 'hostname.com',
            'port': '5432',
            'schema': 'demo',
            'username': 'devrel_master',
            'password': '**********'
        },
        'name': 'devrel-rds',
        'destinationName': 'Postgres',
        'tag': 'tag2'
    }
    return destination_dict


@pytest.fixture
def dummy_connection_dict():
    pass


@pytest.fixture
def dummy_airbyte_dto_factory(dummy_source_definitions, dummy_destination_definitions):
    """
    Create a dummy AirbyteDtoFactory given a set of dummy source and destination definitions
    """
    dto_factory = AirbyteDtoFactory(dummy_source_definitions, dummy_destination_definitions)
    return dto_factory


@pytest.fixture
def dummy_secrets_dict():
    """
    Create dummy secrets for the dummy sources and destinations (as dict)
    """
    secrets_dict = {
        'sources': {
            'GitHub': {'access_token': 'ghp_SECRET_TOKEN'},
            'Slack': {'token': 'SLACK_SECRET_TOKEN'}
        },
        'destinations': {
            'Postgres': {'password': 'SECRET_POSTGRES_PASSWORD'}
        }
    }
    return secrets_dict


@pytest.fixture
def dummy_populated_airbyte_config_model(dummy_source_dto, dummy_destination_dto):
    config_model = AirbyteConfigModel()
    config_model.sources[dummy_source_dto.source_id] = dummy_source_dto
    config_model.destinations[dummy_destination_dto.destination_id] = dummy_destination_dto
    return config_model
