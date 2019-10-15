# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# -------------------------------------
from azure.core.exceptions import ResourceNotFoundError
from devtools_testutils import ResourceGroupPreparer

from secrets_async_preparer import AsyncVaultClientPreparer
from secrets_async_test_case import AsyncKeyVaultTestCase


def print(*args):
    assert all(arg is not None for arg in args)


def test_create_secret_client():
    vault_endpoint = "vault_endpoint"
    # pylint:disable=unused-variable
    # [START create_secret_client]

    from azure.identity.aio import DefaultAzureCredential
    from azure.keyvault.secrets.aio import SecretClient

    # Create a SecretClient using default Azure credentials
    credentials = DefaultAzureCredential()
    secret_client = SecretClient(vault_endpoint, credentials)

    # [END create_secret_client]


class TestExamplesKeyVault(AsyncKeyVaultTestCase):
    @ResourceGroupPreparer()
    @AsyncVaultClientPreparer(enable_soft_delete=True)
    @AsyncKeyVaultTestCase.await_prepared_test
    async def test_example_secret_crud_operations(self, vault_client, **kwargs):
        secret_client = vault_client.secrets

        # [START set_secret]
        from dateutil import parser as date_parse

        expires_on = date_parse.parse("2050-02-02T08:00:00.000Z")

        # create a secret, setting optional arguments
        secret = await secret_client.set_secret("secret-name", "secret-value", enabled=True, expires_on=expires_on)

        print(secret.id)
        print(secret.name)
        print(secret.properties.enabled)
        print(secret.properties.expires_on)

        # [END set_secret]

        secret_version = secret.properties.version
        # [START get_secret]

        # get the latest version of a secret
        secret = await secret_client.get_secret("secret-name")

        # alternatively, specify a version
        secret = await secret_client.get_secret("secret-name", secret_version)

        print(secret.id)
        print(secret.name)
        print(secret.properties.version)
        print(secret.properties.vault_endpoint)

        # [END get_secret]
        # [START update_secret]

        # update attributes of an existing secret
        content_type = "text/plain"
        tags = {"foo": "updated tag"}
        updated_secret_properties = await secret_client.update_secret_properties(
            "secret-name", content_type=content_type, tags=tags
        )

        print(updated_secret_properties.version)
        print(updated_secret_properties.updated_on)
        print(updated_secret_properties.content_type)
        print(updated_secret_properties.tags)

        # [END update_secret]
        # [START delete_secret]

        # delete a secret
        deleted_secret = await secret_client.delete_secret("secret-name")

        print(deleted_secret.name)

        # if the vault has soft-delete enabled, the secret's deleted_date,
        # scheduled purge date and recovery id are set
        print(deleted_secret.deleted_date)
        print(deleted_secret.scheduled_purge_date)
        print(deleted_secret.recovery_id)

        # [END delete_secret]

    @ResourceGroupPreparer()
    @AsyncVaultClientPreparer(enable_soft_delete=True)
    @AsyncKeyVaultTestCase.await_prepared_test
    async def test_example_secret_list_operations(self, vault_client, **kwargs):
        secret_client = vault_client.secrets

        for i in range(7):
            await secret_client.set_secret("key{}".format(i), "value{}".format(i))

        # [START list_secrets]

        # gets a list of secrets in the vault
        secrets = secret_client.list_properties_of_secrets()

        async for secret in secrets:
            # the list doesn't include values or versions of the secrets
            print(secret.id)
            print(secret.name)
            print(secret.enabled)

        # [END list_secrets]
        # [START list_secret_versions]

        # gets a list of all versions of a secret
        secret_versions = secret_client.list_secret_versions("secret-name")

        async for secret in secret_versions:
            # the list doesn't include the versions' values
            print(secret.id)
            print(secret.enabled)
            print(secret.updated_on)

        # [END list_secret_versions]
        # [START list_deleted_secrets]

        # gets a list of deleted secrets (requires soft-delete enabled for the vault)
        deleted_secrets = secret_client.list_deleted_secrets()

        async for secret in deleted_secrets:
            # the list doesn't include values or versions of the deleted secrets
            print(secret.id)
            print(secret.name)
            print(secret.scheduled_purge_date)
            print(secret.recovery_id)
            print(secret.deleted_date)

        # [END list_deleted_secrets]

    @ResourceGroupPreparer()
    @AsyncVaultClientPreparer()
    @AsyncKeyVaultTestCase.await_prepared_test
    async def test_example_secrets_backup_restore(self, vault_client, **kwargs):
        secret_client = vault_client.secrets
        created_secret = await secret_client.set_secret("secret-name", "secret-value")
        secret_name = created_secret.name
        # [START backup_secret]

        # backup secret
        secret_backup = await secret_client.backup_secret(secret_name)

        # returns the raw bytes of the backed up secret
        print(secret_backup)

        # [END backup_secret]

        await secret_client.delete_secret(created_secret.name)
        await self._poll_until_exception(
            secret_client.get_secret, created_secret.name, expected_exception=ResourceNotFoundError
        )

        # [START restore_secret_backup]

        # restores a backed up secret
        restored_secret = await secret_client.restore_secret_backup(secret_backup)
        print(restored_secret.id)
        print(restored_secret.version)

        # [END restore_secret_backup]

    @ResourceGroupPreparer()
    @AsyncVaultClientPreparer(enable_soft_delete=True)
    @AsyncKeyVaultTestCase.await_prepared_test
    async def test_example_secrets_recover(self, vault_client, **kwargs):
        secret_client = vault_client.secrets
        created_secret = await secret_client.set_secret("secret-name", "secret-value")
        await secret_client.delete_secret(created_secret.name)

        await self._poll_until_no_exception(
            secret_client.get_deleted_secret, created_secret.name, expected_exception=ResourceNotFoundError
        )

        # [START get_deleted_secret]
        # gets a deleted secret (requires soft-delete enabled for the vault)
        deleted_secret = await secret_client.get_deleted_secret("secret-name")
        print(deleted_secret.name)

        # [END get_deleted_secret]
        # [START recover_deleted_secret]

        # recover deleted secret to the latest version
        recovered_secret = await secret_client.recover_deleted_secret("secret-name")
        print(recovered_secret.id)
        print(recovered_secret.name)

        # [END recover_deleted_secret]
