#!/usr/bin/env python
from wger_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def get_user_profile(self) -> dict:
        """Get the current user's profile."""
        result = self._get("userprofile")
        if isinstance(result, dict) and "results" in result:
            return result["results"][0] if result["results"] else result
        return result

    def update_user_profile(self, **kwargs) -> dict:
        """Update user profile. Fields: age, height, gender, etc."""
        profile = self.get_user_profile()
        if "id" in profile:
            return self._patch(f"userprofile/{profile['id']}", data=kwargs)
        return self._patch("userprofile", data=kwargs)

    def get_user_statistics(self) -> dict:
        """Get user statistics (workout count, etc.)."""
        return self._get("user-statistics")

    def get_trophies(self, limit: int | None = None, offset: int | None = None) -> dict:
        """List available trophies."""
        return self._list("trophy", limit=limit, offset=offset)

    def get_user_trophies(
        self, limit: int | None = None, offset: int | None = None
    ) -> dict:
        """List user's earned trophies."""
        return self._list("user-trophy", limit=limit, offset=offset)

    def get_languages(
        self, limit: int | None = None, offset: int | None = None
    ) -> dict:
        """List available languages."""
        return self._list("language", limit=limit, offset=offset)

    def get_licenses(self, limit: int | None = None, offset: int | None = None) -> dict:
        """List content licenses."""
        return self._list("license", limit=limit, offset=offset)

    def get_deletion_log(
        self, limit: int | None = None, offset: int | None = None
    ) -> dict:
        """List deletion log entries."""
        return self._list("deletion-log", limit=limit, offset=offset)

    def get_repetition_units(
        self, limit: int | None = None, offset: int | None = None
    ) -> dict:
        """List repetition unit settings."""
        return self._list("setting-repetitionunit", limit=limit, offset=offset)

    def get_weight_unit_settings(
        self, limit: int | None = None, offset: int | None = None
    ) -> dict:
        """List weight unit settings."""
        return self._list("setting-weightunit", limit=limit, offset=offset)
